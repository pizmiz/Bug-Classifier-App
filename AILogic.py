import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow.keras import layers


model = tf.keras.models.load_model('AI/FuncModel')

model.summary()