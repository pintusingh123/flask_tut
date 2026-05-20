from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def rendring():
   try:
     return render_template("index.html")
   except Exception as e:
     print(f"Error: {e}")
@app.route("/about")
def about():
   try:
     return render_template("about.html")
   except Exception as e:
     print(f"Error: {e}")

if __name__ == "__main__":
 app.run(debug = True)