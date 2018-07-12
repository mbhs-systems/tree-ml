"""
File Name: CNN
Author: Ryan Cho
Implementation of Keras and Tensorflow
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets

learning_rate = 0.0001
epochs = 10
batch_size = 50

x = tf.placeholder(tf.float32, [None, 784])
x_shaped = tf.reshape(x, [-1, 28, 28 1])
y = tf.placeholder(tf.float32, [None, 10])

def create_new_conv_layer(input_data, num_input_channels, num_filters, filter_shape, pool_shape, name):
    conv_filt_shape = [filter_shape[0], filter_shape[1], num_input_channels, num_filters]
    weights = tf.Variable(tf.truncated_normal(conv_filt_shape, stddev=0.03), name=name+'_W')
    bias = tf.Variable(tf.truncated_normal([num_filters]), name=name+'_b')
    out_layer = tf.nn.conv2d(input_data, weights, [1, 1, 1, 1], padding='SAME')
    out_layer += bias
    out_layer = tf.nn.relu(out_layer)
    ksize = [1, pool_shape[0], pool_shape[1], 1]
    strides = [1, 2, 2, 1]
    out_layer = tf.nn.max_pool(out_layer, ksize=ksize, strides=strides, 
                               padding='SAME')
    return out_layer


##from __future__ import print_function
##import keras
##from keras.layers import Dense, Flatten
##from keras.layers import Conv2D, MaxPooling2D
##from keras.models import Sequential
##import matplotlib.pylab as plt
##
##batch_size = 128
##num_classes = 10
##epochs = 10
##
###LeNet-5
##model = Sequential()
##model.add(Conv3D(32, kernel_size=(5, 5), strides=(1, 1),
##                 activation='relu',
##                 input_shape=None))
##model.add(MaxPooling3D())
##model.add(Conv3D()
##model.add(MaxPooling3D())
##model.add(Flatten())
##model.add(Dense())
##model.add(Dense(num_classes, activation='softmax'))
##
###compile
##model.compile(optimizer=keras.optimizers.SGD(lr=0.01),
##              loss='binary_crossentropy',
##              metrics=['accuracy'])
##
##model.fit(

