import json
from flask import Blueprint
from flask.wrappers import Response
movies = Blueprint("movies", __name__,  url_prefix="/movies")
from src.app import mongo_client
from bson import json_util

@movies.route("/get_all_movies", methods = ["GET"])
def get_all_movies():
  movies = mongo_client.movies.find({"type": "Movie"})

  return Response(
    response=json_util.dumps({'records' : movies}),
    status=200,
    mimetype="application/json"
  )

@movies.route("/get_all_tv_show", methods = ["GET"])
def get_all_tv_show():
  movies = mongo_client.movies.find({"type": "TV Show"})

  return Response(
    response=json_util.dumps({'records' : movies}),
    status=200,
    mimetype="application/json"
  )