#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import choice
import telebot
from telebot import types
import json

#Константы
TOKEN = '1686080013:AAEPaxgAdfQ2uQ4SkT5q8qjkDu8bnlZ8TVQ'
bot = telebot.TeleBot(TOKEN)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
itembtn = types.KeyboardButton('Хочу еще мудрость')
markup.add(itembtn)

def trim(wisdom:str) -> str:
    
    """
    Функция получает на вход строку и вычищает из нее весь возможный мусор, 
    который может возникнуть при склейке двух частей пословиц.
    
    """
    
    wisdom = wisdom.replace(', а,', ', а')
    wisdom = wisdom.replace(', да –', ', да ')
    wisdom = wisdom.replace(', -', ' -')
    wisdom = wisdom.replace(',-', ' -')
    wisdom = wisdom.replace(',,', ',')
    wisdom = wisdom.replace('?,', ',')
    wisdom = wisdom.replace(', —', ' —')
    wisdom = wisdom.replace(', –', ' -')
    wisdom = wisdom.replace(': —', ':')
    wisdom = wisdom.replace(': -', ':')
    wisdom = wisdom.replace(':,', ':')
    wisdom = wisdom.replace(',:', ',')
    wisdom = wisdom.replace('- —', '—')
    return wisdom

# Читаем файл
with open('pogovorki.json', encoding='utf-8') as read_data:
    parsed_data = json.load(read_data)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет!\nЯ генерирую бред из русских пословиц.\n"
                          "Иногда это смешно, но часто - вовсе нет.\n"
                          "Напиши что угодно или нажми на кнопку внизу, "
                          "и я отвечу очередной мудростью.\nЕсли у тебя дергается глаз от легкого издевательства "
                          "над русским языком, то лучше сходи сюда: @grammarrulez", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    part1 = choice(choice(parsed_data)['part1'])
    print(part1)
    part2 = choice(choice(parsed_data)['part2'])
    print(part2)
    wisdom = trim(part1 + part2)
    bot.send_message(message.chat.id,  wisdom, reply_markup=markup)

bot.polling(none_stop=True, interval=0)