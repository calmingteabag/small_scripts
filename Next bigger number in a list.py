# for a given number
# find all permutations without repetitions
# return biggest number

import itertools


def next_big(n):
    number = n

    # needs to be a string for itertools to work
    str_num = str(number)

    iter_object = itertools.permutations(str_num, len(str_num))
    numbers_list = [int(''.join(i)) for i in iter_object]  # contains duplicates
    num_list = []  # without duplicates

    for i in numbers_list:
        if i not in num_list:
            num_list.append(i)

    num_list = sorted(num_list)

    if max(num_list) == number:
        return number

    else:
        return num_list[num_list.index(number)+1]
        # list.index() returns index position of a given element of a list
        # so, we can find where (index wise) a certain element is in a list and return the next element using
        # this index. Since our list is sorted, the next will be the next bigger element
