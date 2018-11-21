from flask import Flask
from flask import Response
from flask import request
import simplejson as json 

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Index"

# Add another to play with

# Snippet to work with query strings


# Add logic to the query string

# initialize todo's

# Make a route to get all of the Todo items


# Exten the route to add a new item to the todo list


if __name__ == "__main__":
    app.run()

