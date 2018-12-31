"""This script takes a string pasted to the console and outputs all 26 possible
Caesar shifts on it, along with a chi-squared test statitstic, to help more rapidly
identify which might match the letter frequency distribution of the English language.

Example:
    > python rotall.py QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"""

import sys

english_letter_freqs = {
    "a": 8.167,
    "b": 1.492,
    "c": 2.782,
    "d": 4.253,
    "e": 12.702,
    "f": 2.228,
    "g": 2.015,
    "h": 6.094,
    "i": 6.966,
    "j": 0.153,
    "k": 0.772,
    "l": 4.025,
    "m": 2.406,
    "n": 6.749,
    "o": 7.507,
    "p": 1.929,
    "q": 0.095,
    "r": 5.987,
    "s": 6.327,
    "t": 9.056,
    "u": 2.758,
    "v": 0.978,
    "w": 2.360,
    "x": 0.150,
    "y": 1.974,
    "z": 0.074
} # Taken from here: https://gist.github.com/evilpacket/5973230

try:
    input = raw_input # Ensure this script works under Python 2 as well as Python 3.
except NameError:
    pass

def chisquared_stat(observed_values,expected_values):
    # The original version of this function (which just calculates the chi-squared test
    # statistic without relying on SciPy) can be found here:
    # http://specminor.org/2017/01/08/performing-chi-squared-gof-python.html
    test_statistic = 0

    for observed, expected in zip(observed_values, expected_values):
        test_statistic += (float(observed)-float(expected))**2/float(expected)

    df = len(observed_values)-1

    return test_statistic

def encrypt_and_count(string, shift):
    # This is a variant on the Caesar cipher shift published at
    # https://www.thecrazyprogrammer.com/2018/05/caesar-cipher-in-python.html
    # extended to analyze letter frequencies.
    cipher = ''

    counts = [0] * 26
    for char in string:
        if char == ' ':
            cipher += char
        elif char.isupper():
            n = (ord(char) + shift - 65) % 26
            cipher += chr(n + 65)
            counts[n] += 1
        elif char.islower():
            n = (ord(char) + shift - 97) % 26
            cipher += chr(n + 97)
            couns[n] += 1
        else:
            cipher += char

    return cipher, counts

if len(sys.argv) == 1:
    text = input("Enter string to shift: ")
else:
    text = ' '.join([str(x) for x in sys.argv[1:]])

expected_unnormalized = english_letter_freqs.values()
shifted, observed = encrypt_and_count(text,0)
expected = [e*sum(observed)/sum(expected_unnormalized) for e in expected_unnormalized]

print("Shifting {} by all possible shifts.".format(text))
chisquared_min = 9999999999999
shifted_min = None
shift_min = None
for shift in range(0,26):
    shifted, observed = encrypt_and_count(text,shift)
    chisquared = chisquared_stat(observed,expected)
    if chisquared < chisquared_min:
        chisquared_min = chisquared
        shifted_min = shifted
        shift_min = shift

    print("{:>2}  |  {}  | {:>8.1f}".format(shift,shifted,chisquared))

print("\nBest guess based on chi-squared test:")
print("    {:>2}  |  {}  | {:>8.1f}".format(shift_min,shifted_min,chisquared_min))
