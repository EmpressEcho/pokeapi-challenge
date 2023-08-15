# pokeapi-challenge

An API built to discover and store all the Pokemon from the PokeAPI

To run the initial update, build and run the docker image, then access http://127.0.0.1:5000/update.

Once the update is complete, you can access each Pokemon either by name or id, or request a list of all pokemon. You can also access each type and move by their id, or request a list of all types or all moves. 

Each pokemon is linked to its corresponding moves and types via a many-to-many relationship, as each pokemon can have multiple of each. Their details also contain their name, a brief generated description, their species, and the base experience received for defeating them. Where no base experience was recorded in the PokeAPI, the value is stored as 0.

Additional documentation can be found at http://127.0.0.1:5000/swagger-ui once the flask app is running.

## Testing

For each endpoint created as part of this project, I created tests prior to development of the endpoint in the Insomnia client. Examples and results of these tests can be found below. Test evidence can be found in the /testing-details directory

| Test                                    | Expected Result               | Actual Result                 |
| --------------------------------------- | ----------------------------- | ----------------------------- |
| Update database                         | 200, Update successful        | 200, Update Successful        |
| Get all moves                           | 200, Returns list of moves    | 200, Returns list of moves    |
| Create a new move with correct data     | 201, Returns new move item    | 201, Returns new move item    |
| Create a new move with incorrect data   | 500, Item not created         | 422, Item not created         |
| Get a move via a valid ID               | 200, Returns move             | 200, Returns move             |
| Get a move via an invalid ID            | 404, Not found                | 404, Not found                |
| Link valid move to valid pokemon        | 201, Move linked              | 201, Move linked              |
| Link invalid move to valid pokemon      | 404, Not found                | 404, Not found                |
| Link valid move to invalid pokemon      | 404, Not found                | 404, Not found                |
| Get a move by a valid name              | 200, Returns move             | 200, Returns move             |
| Get a move by an invalid name           | 404, Not Found                | 200, Returns empty dictionary |
| Get all types                           | 200, Returns list of types    | 200, Returns list of types    |
| Create new type with valid data         | 201, Returns new type item    | 201, Returns new type item    |
| Create new type with invalid data       | 500, Item not created         | 422, Item not created         |
| Get a type by a valid ID                | 200, Returns move             | 200, Returns move             |
| Get a type by an invalid ID             | 404, Not found                | 404, Not found                |
| Link a valid type to a valid pokemon    | 201, Type linked              | 201, Type linked              |
| Link an invalid type to a valid pokemon | 404, Not found                | 404, Not found                |
| Link a valid type to an invalid pokemon | 404, Not found                | 404, Not found                |
| Get a type by a valid name              | 200, Returns type             | 200, Returns type             |
| Get a type by an invalid name           | 404, Not found                | 200, Returns empty dictionary |
| Get all pokemon                         | 200, Returns list of pokemon  | 200, Returns list of pokemon  |
| Create new pokemon with valid data      | 201, Returns new pokemon item | 201, Returns new pokemon item |
| Create new pokemon with invalid data    | 500, Item not created         | 422, Item not created         |
| Get a pokemon by a valid ID             | 200, Returns pokemon          | 200, Returns pokemon          |
| Get a pokemon by an invalid ID          | 404, Not found                | 404, Not found                |
| Get a pokemon by a valid name           | 200, Returns pokemon          | 200, Returns pokemon          |
| Get a pokemon by an invalid name        | 404, Not found                | 200, Returns empty dictionary |
| Get a count of all pokemon              | 200, Returns count            | 200, Returns count            |