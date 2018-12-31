import sys
from pprint import pprint

try:
    input = raw_input # Ensure this script works under Python 2 as well as Python 3.
except NameError:
    pass

def encrypt(string, shift):
    # This is a variant on the Caesar cipher shift published at
    # https://www.thecrazyprogrammer.com/2018/05/caesar-cipher-in-python.html
    cipher = ''
    for char in string:
        if char == ' ':
            cipher += char
        elif char.isupper():
            cipher += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher += char

    return cipher

if len(sys.argv) == 1:
    text = input("Enter string to shift: ")
else: 
    text = ' '.join([str(x) for x in sys.argv[1:]])

print("Shifting {} by all possible shifts.".format(text))
for shift in range(0,26):
    print(encrypt(text,shift))
