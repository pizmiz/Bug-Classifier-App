import os
from stat import FILE_ATTRIBUTE_SPARSE_FILE
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import losses

ModelDirectory = os.path.dirname(os.path.realpath(__file__)) + "\\AI\\FuncModel\\FuncModel"

max_features = 10000
sequence_length = 250

vectorize_layer = layers.TextVectorization(
    standardize='lower_and_strip_punctuation',
    max_tokens=max_features,
    output_mode='int',
    output_sequence_length=sequence_length
)


model = tf.keras.models.load_model(ModelDirectory, compile=True)

#export_model = tf.keras.Sequential([
#    vectorize_layer,
#    model,
#    layers.Activation('sigmoid')
#])

#export_model.compile(
#    loss=losses.BinaryCrossentropy(from_logits=True), optimizer="adam", metrics=['accuracy']
#)

TestStr = [
    'Who are we anymore',
    'This is broken send help',
    'Functional',
    'This component is not working correctly',
    'Test',
    'This is a non functional component'
]


print (model.predict(TestStr))