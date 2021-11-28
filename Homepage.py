from flask import Flask, redirect, url_for, render_template, send_file, request
from werkzeug.utils import secure_filename
import os
import shutil
import zipfile
import AILogic
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

app = Flask(__name__)

Upload_Path = os.path.dirname(os.path.realpath(__file__)) + "\\File_Upload"
Test_Path = os.path.dirname(os.path.realpath(__file__)) + "\\TestSet"
ResultsPath = os.path.dirname(os.path.realpath(__file__)) + "\\Results"
ResultsZipPath = os.path.dirname(os.path.realpath(__file__)) + "\\Results.zip"
FileName = ""

if os.path.exists(Upload_Path):
    shutil.rmtree(Upload_Path)
os.makedirs(Upload_Path)

app.config['UPLOAD_FOLDER'] = Upload_Path


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/uploader", methods=['GET', 'POST'])
def upload():
    if os.path.exists(Upload_Path):
        shutil.rmtree(Upload_Path)
        os.makedirs(Upload_Path)
    if request.method == 'POST':
        f = request.files['file']
        if (f.filename.endswith('.zip')):
            global FileName
            FileName = f.filename
            f.save(os.path.join(
                app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return render_template("uploader.html", content=f.filename)
        else:
            return render_template("uploaderError.html")


@app.route("/analysis")
def analysis():
    if os.path.exists(Test_Path):
        shutil.rmtree(Test_Path)
        os.makedirs(Test_Path)
    with zipfile.ZipFile(Upload_Path + "\\" + FileName, 'r') as zip_ref:
        zip_ref.extractall(Test_Path)
    PassedTestPath = Test_Path + "\\" + FileName
    PassedTestPath = PassedTestPath[:len(PassedTestPath) - 4]
    AILogic.PreformAnalysis(PassedTestPath)
    return render_template("analysis.html")


@app.route("/download")
def download():
    shutil.make_archive("Results", 'zip', ResultsPath)
    return send_file(ResultsZipPath, as_attachment=True)


@app.route("/<anything>")
def reroute(anything):
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()
