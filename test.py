#!/usr/bin/python
# -*- coding: utf-8 -*-


# Первый самый дурацкий подход. Текст преобразуется посимвольно, сеть ничего не делает, только гадает на кофейной гуще


from pogovorki_functions import *
import numpy as np
from keras import models
from keras import layers
from random import shuffle
from keras import optimizers, regularizers


yesData, yesResult = nn_readfile('yes.txt', 1)
noData, noResult = nn_readfile('no.txt', 0)
experimentData, exterimentSource = nn_readfile('test.txt', 0)
allTrainData = []
allTrainData.extend(yesData)
allTrainData.extend(noData)
random.shuffle(allTrainData)
testData = allTrainData[0:1000]
allTrainData = allTrainData[1000:]
allLabels = []
testLabels = []
for i in allTrainData:
    allLabels.append(i[0])
    i[0] = 0
for i in testData:
    testLabels.append(i[0])
    i[0] = 0
for i in experimentData:
    i[0] = 0
all_data = np.array(allTrainData)
all_labels = np.array(allLabels)
test_data = np.array(testData)
test_labels = np.array(testLabels)
print(all_data.shape, all_labels.shape, test_data.shape, test_labels.shape)

#

model = models.Sequential()
model.add(layers.Dense(32, activation='relu', input_shape=(150,)))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(2, activation='sigmoid'))

model.compile(optimizer=optimizers.RMSprop(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(all_data, all_labels, epochs=3000, batch_size=512, validation_data=(test_data, test_labels))

for i in range(len(experimentData)):
    nugget = np.array(experimentData[i:i+1])
    text = exterimentSource[i]
    result = model.predict(nugget)
    print (text, result)