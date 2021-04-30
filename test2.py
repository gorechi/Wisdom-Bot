#!/usr/bin/python
# -*- coding: utf-8 -*-


# Второй подход. Попытка использовать слой Embedding с формированием словаря всех слов


from pogovorki_functions import *
import numpy as np
from keras import models
from keras import layers
from random import shuffle
from keras import optimizers, regularizers
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical


with open('pogovorki.txt', 'r', encoding='utf-8') as f:
    texts = f.read()
    tests = texts.replace('\ufeff', '')

maxWordsCount = 20000
tokenizer = Tokenizer(num_words=maxWordsCount,
                      filters='!-"—#$%^&*(),._+~`<>=?/[]{}|_\n\t\r',
                      lower=True,
                      split=' ',
                      char_level=False)
tokenizer.fit_on_texts([texts])

dist = list(tokenizer.word_counts.items())
print(dist[:100])

data = tokenizer.texts_to_sequences([texts])
res = to_categorical(data[0], num_classes = maxWordsCount)
print(res.shape)