import random

a = "0123456789"
num_list = []
num_qty = 25


def number_generator(num):
    count = num
    new_number = ''
    while True:
        digit = random.choice(a)
        new_number += digit
        count -= 1

        if count == 0:
            return new_number


def num_list_generator(num_qty):

    while True:
        if num_qty == 0:
            break
        else:
            num = random.randint(1, 4)
            new_number = int(number_generator(num))
            num_list.append(new_number)
            num_qty -= 1


num_list_generator(num_qty)
