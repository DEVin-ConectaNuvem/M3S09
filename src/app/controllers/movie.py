from flask import Blueprint
from flask.wrappers import Response
from src.app import mongo_client
from bson import json_util
from datetime import datetime

movies = Blueprint("movies", __name__,  url_prefix="/movies")

@movies.route("/get_all_movies", methods = ["GET"])
def get_all_movies():

  movies = mongo_client.movies.aggregate([
    {
        '$lookup': {
            'from': 'comments', 
            'localField': '_id', 
            'foreignField': 'movie_id', 
            'as': 'comments'
        }
    }, {
        '$match': {
            'comments': {
                '$ne': []
            }
        }
    }, {
        '$project': {
            'title': 1,
            'count': {
                '$size': '$comments'
            }
        }
    },
    {
      "$limit": 10
    }
  ])

  return Response(
    response=json_util.dumps({'records' : movies}),
    status=200,
    mimetype="application/json"
  )