import requests
from typing import Optional

def make_get_request(url: str) -> dict:
    response_json = requests.get(url).json()    # Make a GET request to the specified API endpoint

    return response_json

def get_database_total() -> int:
    count = make_get_request("http://127.0.0.1:5000/pokemon/count")["count"]  # Make a GET request to the database API to fetch a count of the pokemon already stored
    return count

def get_pokemon_list(offset: int) -> int:
    url = f"https://pokeapi.co/api/v2/pokemon/?limit=10000&offset={offset}"
    pokemon_list = make_get_request(url)["results"]    # Get a list of pokemon starting from a specified point

    return pokemon_list

def format_request_body(data: dict, data_type: str) -> dict:
    if data_type == "pokemon":    # If the data is for a pokemon, format it to meet the database API's requirements
        body = {
            "name": data["name"],
            "description": f"{data['name'].capitalize()} is {data['height']} decimetres tall and weighs {data['weight']} hectograms.",
            "species": data["species"]["name"],
            "base_experience": data["base_experience"] or 0
        }
    else:    # If the data is not for a pokemon, format it to meet the separate requirements used for types and moves
        body = {
            "name": data["name"]
        }
    return body    # Return the formatted data

def post_data_to_db(endpoint: str, data: Optional[dict]=None) -> dict:
    url = f"http://127.0.0.1:5000/{endpoint}"
    response_json = requests.post(url, json=data).json()    # POST the data as a JSON body to the request url

    return response_json

def check_existing(endpoint: str, name:str):
    url = f"http://127.0.0.1:5000/{endpoint}/{name}"
    try:
        id = make_get_request(url)["id"]    # Get the id of a pokemon by its name, if it exists
        return id
    except:
        return False    # If it does not exist, return False


def collect_new_data():
    db_total = get_database_total()
    pokemon_list = get_pokemon_list(offset=db_total)

    if len(pokemon_list) > 0:
        for pokemon in pokemon_list:
            print(f"--- Making request #{pokemon_list.index(pokemon)+1} of {len(pokemon_list)} ---")
            response_json = make_get_request(pokemon["url"])    # Get the pokemon's data
            if check_existing("pokemon", response_json["name"]) == False:    # Checks if the pokemon already exists
                data = format_request_body(response_json, "pokemon")    # Turn the raw API return into a usable JSON body
                pokemon_id = post_data_to_db("pokemon", data)["id"]    # Post the pokemon data to the database, creating a new pokemon & storing its id
                for move in response_json["moves"]:
                    has_id = check_existing("move", move["move"]["name"])    # For each move the pokemon has, check if it exists and if so, store its id
                    if has_id == False:
                        move_data = format_request_body(move["move"], "move")    # If the move doesn't exist, convert it into a usable JSON body
                        has_id = post_data_to_db("move", move_data)["id"]    # Post the move data to the database, creating a new move & storing its id
                    post_data_to_db(f"pokemon/{pokemon_id}/move/{has_id}")    # Link the move to the pokemon
                for type in response_json["types"]:
                    has_id = check_existing("type", type["type"]["name"])    # For each type the pokemon has, check if it exists and if so, store its id
                    if has_id == False:
                        type_data = format_request_body(type["type"], "type")    # If the type doesn't already exist, convert it into a usable JSON body
                        has_id = post_data_to_db("type", type_data)["id"]    # Post the type data to the database, creating a new type and storing its id
                    post_data_to_db(f"pokemon/{pokemon_id}/type/{has_id}")    # Link the type to the pokemon
    print("--- Database up to date! ---")