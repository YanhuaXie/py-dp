
# In this notebook, we are going to cover some of the most fundamental concepts of tensors using TensorFlow
# More specifically, we are going to cover:
#
# introduction to tensors
# getting information from tensors
# manipulating tensors
# tensors & NumPy
# using @tf.function (a way to speed up your regular Python functions)
# using GPUs with TensorFlow (or TPUs)
# Exercises to try for yourself!


# import tensorflow
import tensorflow as tf

# create a tensor
print(tf.__version__)

tensor = tf.constant([10, 7])
print(tensor)