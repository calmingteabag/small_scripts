# Solved this on codewars, decided to save it

# Assuming a city with a grid street layout and that a person takes one
# minute to traverse a block, return how many minutes it will take, given the
# sequence of blocks, to finish walking it and if the trajectory will end in
# its origin

minutes = 0
walk = ['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']
n_count = s_count = e_count = w_count = 0

for i in walk:
    minutes += 1
    if i == 'n':
        n_count += 1
    elif i == 's':
        s_count += 1
    elif i == 'w':
        w_count += 1
    else:
        e_count += 1

if n_count != s_count or w_count != e_count:
    """
    Explanation:

    Imagine a X,Y graph, if a dot walks the same distance on x-positive and x-negative it
    will return to the origin. Same for y-positive and y-negative.
    """
    print(f"Walked for {minutes} minutes and it will not end up in origin")
else:
    print(f"Walked for {minutes} minutes and it will end up in origin")