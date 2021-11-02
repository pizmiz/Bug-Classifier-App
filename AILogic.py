import os
from stat import FILE_ATTRIBUTE_SPARSE_FILE
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow.keras import layers

ModelDirectory = os.path.dirname(os.path.realpath(__file__)) + "\\AI\\FuncModel"

model = tf.keras.models.load_model(ModelDirectory)

model.summary()

TestStr = [
    'Who are we anymore',
    'This is broken send help',
    'Functional',
    'This component is not working correctly',
    'Test',
    'This is a non functional component'
]



print (model.predict(TestStr))