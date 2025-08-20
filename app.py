# python3 -m pip install Flask
from flask import Flask    # dependency

# create an app instance
app = Flask(__name__)

# define the root path of our API
@app.route("/")     # decorator (default method is a GET)
def hello():        # function to run when decorator is interacted with
    return "Hello, DevOps!"
