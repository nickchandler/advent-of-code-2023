import os
"""
Problem: sum all of the numbers adjacent to a symbol

Approach: iterate through rows, find a symbol

    go up, down, left, right, diag and look for numbers

    add the whole number to the running sum, and then blank the number so as not to add it twice

I need to represent the file as a 2d matrix, then traverse it with x and y coords

"""

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')

f = open(file_path, 'r')

matrix = f.readlines()

cur_x = 0
cur_y = 0


def isPart(char):
    if char == '.':
        return False
    try:
        int(char)
        return False
    except:
        return True

# go thru the file and find the symbols that aren't period or a number
print(isPart('+'))

## Make a bunch of helper functions that will hand the tedious shit you have to do






