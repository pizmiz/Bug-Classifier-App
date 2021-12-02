from tensorflow.python.ops.gen_batch_ops import batch
from tensorflow.keras import preprocessing
from tensorflow.keras import losses
from tensorflow.keras import layers
import tensorflow as tf
import string
import re
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def DoEverything():
    batch_size = 32
    seed = 42

    raw_train_ds = preprocessing.text_dataset_from_directory(
        'Data',
        batch_size=batch_size,
        validation_split=0.2,
        subset='training',
        seed=seed
    )

    #print (raw_train_ds.class_names[0])
    #print (raw_train_ds.class_names[1])

    raw_val_ds = preprocessing.text_dataset_from_directory(
        'Data',
        batch_size=batch_size,
        validation_split=0.2,
        subset='validation',
        seed=seed
    )

    # def custom_standardization(input_data):
    #    lowercase = tf.strings.lower(input_data)
    #    returnstring = tf.strings.regex_replace(lowercase, '[%s]' % re.escape(string.punctuation), '')
    #    return returnstring

    max_features = 10000
    sequence_length = 250

    vectorize_layer = layers.TextVectorization(
        standardize='lower_and_strip_punctuation',
        max_tokens=max_features,
        output_mode='int',
        output_sequence_length=sequence_length
    )

    train_text = raw_train_ds.map(lambda x, y: x)
    vectorize_layer.adapt(train_text)

    def vectorize_text(text, label):
        text = tf.expand_dims(text, -1)
        return vectorize_layer(text), label

    #print (vectorize_layer.get_vocabulary()[1000])
    #print (vectorize_layer.get_vocabulary()[144])

    train_ds = raw_train_ds.map(vectorize_text)
    val_ds = raw_val_ds.map(vectorize_text)

    AUTOTUNE = tf.data.AUTOTUNE

    train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    embedding_dim = 16
    max_features = 10000

    model = tf.keras.Sequential([
        layers.Embedding(max_features + 1, embedding_dim),
        layers.Dropout(0.2),
        layers.GlobalAveragePooling1D(),
        layers.Dropout(0.2),
        layers.Dense(1)
    ])

    model.summary()

    model.compile(loss=losses.BinaryCrossentropy(from_logits=True),
                  optimizer='adam',
                  metrics=tf.metrics.BinaryAccuracy(threshold=0.0)
                  )

    epochs = 10
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs
    )

    loss, accuracy = model.evaluate(val_ds)

    export_model = tf.keras.Sequential([
        vectorize_layer,
        model,
        layers.Activation('sigmoid')
    ])

    export_model.compile(
        loss=losses.BinaryCrossentropy(from_logits=True), optimizer="adam", metrics=['accuracy']
    )

    examples = [
        'Who are we anymore',
        'This is broken send help',
        'Functional',
        'This component is not working correctly',
        'Test',
        'This is a non functional component'
    ]

    #print (model.predict(examples))

    print("Saving Model...")

    export_model.save('FuncModel\\FuncModel', save_format='tf')

    #ModelDirectory = os.path.dirname(os.path.realpath(__file__)) + "\\FuncModel"

    #model = tf.keras.models.load_model(ModelDirectory)

    #print (model.predict(examples))

    print("Loss: ", loss)
    print("Accuracy: ", accuracy)

    return


if (__name__) == "__main__":
    DataPath = os.path.dirname(os.path.realpath(__file__)) + '\\Data'
    if (os.path.exists(DataPath)):
        DoEverything()
    else:
        print("Run ManualLabel.py First")
