import os
from collections import defaultdict

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
power_sum = 0

while keep_counting == True:
    running_maxes = {
        "red": 0,
        "blue": 0,
        "green": 0,
    }
    game = file.readline().strip()
    if game.__len__() == 0:
        break;

    grabs = game[game.index(':') + 1:].split(';')

    bad_game = False
    # go thru the grabs in a game
    for grab in grabs:
        color_counts = grab.split(',')


        # for a grab, go through the individual colors
        for color_count in color_counts:
            count = int(color_count[1:3].strip())
            color = color_count[3:].strip()

            running_max = running_maxes.get(color)
            if running_max == None: break;
            # record the running max for this color for the game
            if count > running_max:
                running_maxes.__setitem__(color, count)

            limit = limit_dict.get(color)
            if limit == None: continue

            if int(count) > limit:
                bad_game = True;


    if bad_game == False:
        sum = sum + game_num

    curr_power_set = running_maxes["blue"] * running_maxes["green"] * running_maxes["red"];
    power_sum = power_sum + curr_power_set

    game_num = game_num + 1

print(sum, 'sum')
print(power_sum, 'power_sum')
