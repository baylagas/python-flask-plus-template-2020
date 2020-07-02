from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route("/", method=["GET", "POST"])
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
