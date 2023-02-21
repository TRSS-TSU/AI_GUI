from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "mamabear333"


@app.route("/")
def index():
    flash("")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Your question was:    " +
          str(request.form['name_input']) + "      Your answer would be displayed here.")
    return render_template("index.html")
