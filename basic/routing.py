from flask import Flask
app = Flask(__name__)

@app.route("/") #decorator and "/" is the endpoint of the url
def home():
    return "flask is running"

@app.route("/about")
def about():
    return "About page"
@app.route("/contact")
def contact():
    return "Contact page"

if __name__ == "__main__":
    app.run(debug=True)