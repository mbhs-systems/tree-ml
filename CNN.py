"""
File Name: CNN
Author: Ryan Cho
Implementation of Keras and Tensorflow

LeNet-5 Architecture
"""
from __future__ import print_function
import keras
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential
import matplotlib.pylab as plt

batch_size = 128
num_classes = 10
epochs = 10

#LeNet-5
model = Sequential()
model.add(Conv3D(32, kernel_size=(5, 5), strides=(1, 1),
                 activation='relu',
                 input_shape=None))
model.add(MaxPooling3D())
model.add(Conv3D()
model.add(MaxPooling3D())
model.add(Flatten())
model.add(Dense())
model.add(Dense(num_classes, activation='softmax'))

#compile
model.compile(optimizer=keras.optimizers.SGD(lr=0.01),
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(

