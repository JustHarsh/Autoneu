# Using Tensorflow 2.x
# Make sure to use the latest version of Tensorflow

# Using Tensorflow 2.x

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(64, (2, 2), input_shape=(64, 64, 3)),
    tf.keras.layers.Conv2D(64, (2, 2)),
    tf.keras.layers.Conv2D(32, (2, 2)),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(16, (2, 2), activation='relu'),
    tf.keras.layers.Conv2D(8, (2, 2), activation='relu'),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(units=1, activation='sigmoid')
])


# Compiling the CNN
model.compile(
    optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# PART 2 - FITTING CNN TO IMAGES
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

training_data = 'Data/train/'
testing_data = 'Data/test/'

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
    training_data,
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')


testing_set = test_datagen.flow_from_directory(
    testing_data,
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')

cnn = model.fit(training_set,
                steps_per_epoch=160,
                epochs=10,
                validation_data=testing_set,
                validation_steps=20)

saved_model = './Code/saved_model/'
model.save(saved_model)
print("Model saved.")
