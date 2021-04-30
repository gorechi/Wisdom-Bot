#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint as dice
from pogovorki_functions import *

# Читаем файл
pogovorki = readfile('pogovorki.txt', True, '|')

#Основная программа

print (str(len(pogovorki)))
a = input('Хотите мудрость?')

while a not in ['end', 'конец']:
    wisdom = trim(pogovorki[dice(0, len(pogovorki) - 1)][0] + pogovorki[dice(0, len(pogovorki) - 1)][1])
    print(wisdom)
    a = input('Хотите мудрость?')
    if a in ['s', 'ы', 'c', 'с']:
        writefile('saved-wisdom.txt', wisdom)
        print('Мудрость сохранена в анналах')