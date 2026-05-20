from flask import Flask , render_template

app = Flask(__name__);

@app.route("/")
def home():
    try:
      return render_template("home.html")
    except Exception as e:
      print(f"My Error: {e}")

@app.route("/about")
def about():
    try:
      return render_template("about.html")
    except Exception as e:
      print(f"My Error: {e}")

@app.route("/contact")
def contact():
    try:
      return render_template("contact.html")
    except Exception as e:
      print(f"My Error: {e}")

@app.route("/login")
def login():
   try: 
      return render_template("login.html")
   except Exception as e:
      print(f"My Error: {e}")

@app.route("/register")
def register():
    try:
        return render_template("register.html")
    except Exception as e:
        print(f"My Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)