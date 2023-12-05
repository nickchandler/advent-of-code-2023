import os
from collections import defaultdict


"""
Game: elf will reach into bag and grab handful of random cubes multiple times per game

elf wants to know which games are possible if bag contains only 12 red cubes, 13 green cubes, 14 blue cubes

approach: 

    you need to iterate through each game in the list
    you need to check each example from each game against the limit

    for games that are possible, add to the running sum
"""

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')

file = open(file_path, 'r')

limit_vals = {
    "blue" : 14,

    "green" : 13,
    "red" : 12,
}

limit_dict = defaultdict(lambda: 0, limit_vals)
game_num = 1
keep_counting = True
sum = 0

while keep_counting == True:
    
    game = file.readline().strip()
    if game.__len__() == 0:
        break;

    grabs = game[game.index(':') + 1:].split(';')

    bad_game = False
    # go thru the grabs in a game
    for grab in grabs:
        if bad_game == True: break
        color_counts = grab.split(',')


        # for a grab, go through the individual colors
        for color_count in color_counts:
            count = color_count[1:3].strip()
            color = color_count[3:].strip()

            limit = limit_dict.get(color)
            if limit == None: continue

            if int(count) > limit:
                bad_game = True;
                break;


    if bad_game == False:
        sum = sum + game_num

    game_num = game_num + 1

print(sum)
