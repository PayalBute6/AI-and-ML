"""
Question: Write a program to build a Convolutional Neural Network (CNN) for image recognition.(Orange vs Apple)
"""

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import warnings
warnings.filterwarnings("ignore")

# Using random simulated data as a placeholder for actual image datasets
import numpy as np
X_train = np.random.rand(10, 128, 128, 3)
Y_train = np.random.randint(2, size=10)
X_test = np.random.rand(5, 128, 128, 3)
Y_test = np.random.randint(2, size=5)

model = Sequential([
    Conv2D(32, (3, 3), activation="relu", input_shape=(128, 128, 3)),
    MaxPooling2D(),
    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D(),
    Flatten(),
    Dense(128, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

print("Training CNN Model...")
model.fit(X_train, Y_train, epochs=2, verbose=1)

print("\nEvaluating Model...")
loss, accuracy = model.evaluate(X_test, Y_test, verbose=0)
print("Test Accuracy:", round(accuracy, 2))
