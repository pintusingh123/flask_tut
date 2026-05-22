from flask import Flask , render_template, request

app = Flask(__name__);
@app.route("/")
def add():
    try:
      return render_template("add.html")
    except Exception as e:
      print(f"My Error: {e}")

@app.route("/result", methods=["POST"])
def result():
    try:
        number_one = float(request.form["numberOne"])
        number_two = float(request.form["numberTwo"])
        total = number_one + number_two
        return render_template("result.html", total=total)
    except Exception as e:
        print(f"My Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
  