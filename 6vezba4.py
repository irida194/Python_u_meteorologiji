import re

text = 'Lazic Sokolov Savic Tosic'

prezimena = re.findall(r'\w+ic', text)

print(prezimena)