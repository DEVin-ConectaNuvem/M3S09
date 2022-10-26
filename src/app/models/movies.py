def create_collection_movies(mongo_client):
  movies_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "properties": {
            "type": {
              "bsonType": "string",
              "description": "Se é um filme ou uma série",
              "enum": ["Movie", "TV Show"]
            },
            "title": {
              "bsonType": "string",
              "description": "O título",
            },
            "release_year": {
              "bsonType": "int",
              "description": "Ano de lançamento do filme"
            },
            "duration": {
              "bsonType": "string",
              "description": "Duração",
            },
            "description": {
              "bsonType": "string",
              "description": "Descrição sobre o filme",
            },
            "cast": {
              "bsonType": "array",
              "description": "Elenco do filme",
              "items": {
                "bsonType": "string",
                "description": "Pessoa do filme",
              }
            }
        },
    }
  }

  try:
    mongo_client.create_collection("movies")
  except Exception as e:
    print(e)

  mongo_client.command("collMod", "movies", validator=movies_validator)
