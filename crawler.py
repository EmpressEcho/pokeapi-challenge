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

def format_request_body(json: dict, data_type: str) -> dict:
    pass

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
        pass