from flask import Flask
from src.app.controllers.movie import movies

def routes(app: Flask):
  app.register_blueprint(movies)