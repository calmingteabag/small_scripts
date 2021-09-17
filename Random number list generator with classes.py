import random


class Numgen:
    """
        This is a class to create randomly generated numbers list.

        For a given list size defined by 'num_qty', it will first generate a random integer
        using 'num_init' and 'num_end' as its limit values. This will define the size of a number.

        Next a function is called to choose a random number from 0 to 9 and concatenate it in
        a new digit using variable 'num_size' (which is defined by 'num_init' and 'num_end') as its
        parameter.

        The result number is added to the list and process is repeated.


    """

    def __init__(self, num_qty, num_init, num_end):
        """

        :param num_qty: list size
        :param num_init: lowest number size
        :param num_end: biggest number size
        """

        self.num_qty = num_qty
        self.num_init = num_init
        self.num_end = num_end
        self.num_list = []

    def num_list_generator(self):

        numbers = '0123456789'

        def number_generator(num):

            count = num
            new_number = ''
            while True:
                digit = random.choice(numbers)
                new_number += digit
                count -= 1

                if count == 0:
                    return new_number

        remaining_numbers = self.num_qty

        while True:
            if remaining_numbers == 0:
                break
            else:
                num_size = random.randint(self.num_init, self.num_end)
                concatenated_number = int(number_generator(num_size))
                self.num_list.append(concatenated_number)
                remaining_numbers -= 1


