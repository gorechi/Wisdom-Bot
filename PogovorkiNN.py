#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy
import scipy.special
import matplotlib.pyplot as plt
import pickle
from pogovorki_functions import *
import random

class NeuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learningrate
        self.wih = numpy.random.normal(0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        self.counter = 0
        pass

    def activation_function (self, x):
        return scipy.special.expit(x)

    def train(self, inputs_list, targets_list):
        # Преобразуем список входных значений в двухмерный массив
        inputs = numpy.array(inputs_list, ndmin=2).T
        # Преобразуем список целевых значений в двухмерный массив
        targets = numpy.array(targets_list, ndmin=2).T
        # Рассчитываем исходящие сигналы для скрытого слоя
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        # Рассчитываем исходящие сигналы для выходного слоя
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        # Рассчитываем значение ошибки на выходе
        output_errors = targets - final_outputs
        # Рассчитываем распространение ошибки по узлам скрытого слоя
        hidden_errors = numpy.dot(self.who.T, output_errors)
        # Делаем поправку весовых коэффициентов скрытого слоя
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                        numpy.transpose(hidden_outputs))
        # Делаем поправку весовых коэффициентов входного слоя
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))
        self.counter += 1
        return True

    def query(self, inputs_list):
        # Преобразуем список входных значений в двухмерный массив
        inputs = numpy.array(inputs_list, ndmin=2).T
        # Рассчитываем исходящие сигналы для скрытого слоя
        hidden_inputs = self.activation_function(numpy.dot(self.wih, inputs))
        # Рассчитываем исходящие сигналы для выходного слоя
        final_inputs = self.activation_function(numpy.dot(self.who, hidden_inputs))
        return final_inputs

    def test(self, test_file):
        scorecard = []
        data_set = readfile(test_file, True, '|')
        for record in data_set:
            test_data = str_to_data(record[1], int(record[0]))
            result = self.query(test_data[1:])
            if result[0][0] > result[1][0]:
                result_number = 0
            else:
                result_number = 1
            if int(record[0]) == result_number:
                scorecard.append(1)
            else:
                scorecard.append(0)
        print('scorecard: ', scorecard)
        final_score = sum(scorecard)/len(scorecard)
        return final_score

    def save(self, filename):
        if self.counter % 10 == 0:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            return True
        else:
            return False