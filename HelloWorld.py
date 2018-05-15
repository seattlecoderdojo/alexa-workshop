# import necessary packages (of code)
# "from" tells Python to import packages from a specific library
# if there's no "from," it's importing from the PSL (Python Standard Library)
from flask import Flask, render_template
from flask_ask import Ask, statement
import os

# set up the app and the intent
app = Flask(__name__)
ask = Ask(app, '/')

# set up the intent 
@ask.intent('HelloWorld')
def hello():
    return statement("Hello, World!")

# housekeeping to ensure this runs on Cloud9
if __name__ == "__main__":
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 8080))
    app.debug = True
    app.run(host=host, port=port)
