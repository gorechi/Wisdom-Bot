from pogovorki_functions import *
import json


pogovorki = readfile('pogovorki.txt', True, '|')

# with open('pogovorki.json', 'a', encoding='utf-8') as file:
#     file.write('[\n')
#     for i in pogovorki:
#         file.write('  {\n')
#         file.write('    "part1":\n      [\n        "' + i[0] + '"\n      ],\n')
#         file.write('    "part2":\n      [\n        "' + i[1] + '"\n      ]\n')
#         file.write('  },\n')
#     file.write(']')

with open('pogovorki.json', encoding='utf-8') as read_data:
    parsed_data = json.load(read_data)
print(parsed_data[0:10])
wisdom = parsed_data[0]['part1'][0] + parsed_data[3]['part2'][0]
print (wisdom)