# case 1 
# import flask
# app = flask.Flask(__name__)
# case 2
from flask import Flask
app = Flask(__name__)

@app.route("/")
def greet():
   return "hello world"

host = "0.0.0.0"
port = 3000
if __name__ == "__main__":
    
    app.run(host=host, port=port, debug=True)