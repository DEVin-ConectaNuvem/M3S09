import json
from flask import Blueprint
from flask.wrappers import Response

movies = Blueprint("movies", 
__name__,  url_prefix="/movies")

@movies.route("/get_all_movies", 
methods = ["GET"])
def get_all_movies():
  return Response(
    response=json.dumps({"records": [
      {"name": "Senhor dos Aneis", "id": 1},
      {"name": "A volta dos que não foram", "id": 2},
      {"name": "Homem-Aranha 2", "id": 3}
    ]}),
    status=200,
    mimetype="application/json"
  )