import wandb
import tensorflow as tf
from tensorflow import keras

(train_images, train_labels), (test_images,
                               test_labels) = keras.datasets.mnist.load_data()

# What are the dimensions of train_images?
print(train_images.shape)

# Assign the number of test images to a variable
total_test_images = len(train_images)
