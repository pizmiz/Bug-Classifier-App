from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
import os
import shutil

app = Flask(__name__)

Upload_Path = os.path.dirname(os.path.realpath(__file__)) + "\\File_Upload"

if os.path.exists(Upload_Path):
    shutil.rmtree(Upload_Path)
os.makedirs(Upload_Path)   

app.config['UPLOAD_FOLDER'] = Upload_Path

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/uploader", methods=['GET', 'POST'])
def Upload():
    if os.path.exists(Upload_Path):
        shutil.rmtree(Upload_Path)
        os.makedirs(Upload_Path) 
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return redirect(url_for("home"))


@app.route("/<anything>")
def reroute(anything):
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()
