from src.app import app, mongo_client
from src.app.models.comments import create_collection_comments
from src.app.models.movies import create_collection_movies
from src.app.routes import routes
from flask.cli import with_appcontext
import click

routes(app)

@click.command(name='create_collections')
@with_appcontext 
def call_command():
  create_collection_movies(mongo_client)
  create_collection_comments(mongo_client)

app.cli.add_command(call_command)

if __name__ == "__main__":
  app.run()