from flask import Flask, redirect, url_for, render_template
import RandGen

app = Flask(__name__)

@app.route("/")
def home():
    NameList = RandGen.GenerateNames()
    return render_template("index.html", content=NameList)

@app.route("/<anything>")
def reroute(anything):
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()
