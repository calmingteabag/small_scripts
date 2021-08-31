# Generates a random gibberish string consisting of upper and lower case characters
# numbers and special characters.

import random


def gibberish():
    gibberish_letters = ''
    gibberish_numbers = ''

    letters = "abcdefghijklmnopqrstuvwxyz"
    numeros = "1234567890-=!@#$%¨&*"

    gibberish_size = random.randint(50, 100)

    # For each iteration, picks random character from string and add to another string
    for iterador in range(gibberish_size):
        letter_random = random.choice(letters)
        gibberish_letters = gibberish_letters + letter_random
        number_random = random.choice(numeros)
        gibberish_numbers = gibberish_numbers + number_random

    # Generate a tuple for upper and lower characters (zip), (map) to use the random function the two tuple values and
    # (join) then together.
    # Do it again with numbers and special characters
    result_gibberish_letters = ''.join(map(random.choice, zip(gibberish_letters.lower(), gibberish_letters.upper())))
    result_gibberish = ''.join(map(random.choice, zip(result_gibberish_letters, gibberish_numbers)))

    return result_gibberish
    # print('')
    # print(result_gibberish)


print(gibberish())
