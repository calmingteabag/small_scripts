# Solved this cata in codewars and thought it was nice to have a function of this around

def secs_to_galaxy():

    seconds = ''
    usr_input = ''

    while True:
        """
        The usual check to see if user input is a number and not
        a random gibberish
        """
        if usr_input.isdigit():
            seconds = new_func(usr_input)
            break
        else:
            usr_input = input("Type a time in seconds: ")
            continue

    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    day, hour = divmod(hour, 24)
    year, day = divmod(day, 365)

    return sec, min, hour, day, year

def new_func(usr_input):
    seconds = int(usr_input)
    return seconds


secs_to_galaxy()
