import tensorflow as tf
import os
import shutil
from stat import FILE_ATTRIBUTE_SPARSE_FILE
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def PreformAnalysis(TestPath):
    ModelDirectory = os.path.dirname(os.path.realpath(
        __file__)) + "\\AI\\FuncModel\\FuncModel"

    model = tf.keras.models.load_model(ModelDirectory, compile=True)

    Files = []
    FilesEnds = os.listdir(TestPath)
    for FileEnd in FilesEnds:
        FileToAppend = TestPath + "\\" + FileEnd
        Files.append(FileToAppend)

    TestSet = []

    for file in Files:
        f = open(file, "r")
        FileText = f.read()
        TestSet.append(FileText)
        f.close()

    results = model.predict(TestSet)
    print(results)

    ResultsPath = os.path.dirname(os.path.realpath(__file__)) + "\\Results"
    ResultsPathFunc = ResultsPath + "\\Functional"
    ResultsPathNonFunc = ResultsPath + "\\Non-Functional"
    ResultsPathUnknown = ResultsPath + "\\Unknown"

    if os.path.exists(ResultsPath):
        shutil.rmtree(ResultsPath)
        os.makedirs(ResultsPath)
    else:
        os.makedirs(ResultsPath)

    os.makedirs(ResultsPathFunc)
    os.makedirs(ResultsPathNonFunc)
    os.makedirs(ResultsPathUnknown)

    MyIndex = 0
    for file in Files:
        if (float(results[MyIndex]) < .05):
            shutil.copy(file, ResultsPathFunc)
        elif (float(results[MyIndex]) > .95):
            shutil.copy(file, ResultsPathNonFunc)
        else:
            shutil.copy(file, ResultsPathUnknown)
        MyIndex = MyIndex + 1
