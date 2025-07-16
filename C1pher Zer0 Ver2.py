from tabulate import tabulate
from time import sleep
from tqdm import tqdm
import sys
import time

class colorMe:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
    ITALIC = '\33[3m'
    CSELECTED = '\33[7m'



def encrypt(text,key):
    global stage1

    for char in text:
        if char == ' ':
            stage1 += char
        elif char.isupper():
            stage1 += chr((ord(char) + key - 65) % 26 + 65)
        else:
            stage1 += chr((ord(char) + key - 97) % 26 + 97)

    return stage1


def decrypt(stage1,key):
    global stage2

    for char2 in stage1:
        if char2 == ' ':
            stage2 += char2
        elif char2.isupper():
            stage2 += chr((ord(char2) - key - 65) % 26 + 65)
        else:
            stage2 += chr((ord(char2) - key - 97) % 26 + 97)

    return stage2

text = input("Enter Plain Text --->")
key = int(input("Enter Algorithm Key --->"))

charArray =[]
charDOTnext = []
stage1 = ""
stage2 = ""

print(encrypt(text,key))
print(decrypt(stage1,key))

for i in text :
    charArray.append(i)

for i in stage1 :
    charDOTnext.append(i)

table = [charArray, charDOTnext]
print(colorMe.CYAN+tabulate(table, tablefmt='fancy_grid')+colorMe.ENDC)



