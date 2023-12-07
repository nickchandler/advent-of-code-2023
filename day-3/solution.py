import os
from collections import defaultdict

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')

f = open(file_path, 'r')

matrix = f.readlines()

def safe_int(str):
    try:
        return int(str)
    except:
        return False

def isPart(char):
    if char == '.':
        return False
    try:
        int(char)
        return False
    except:
        return True

# find a number if it exists, and blank it out
def find_num(y, x, input, seen_dict):
    if y < 0 or y > input.__len__() - 1: return False
    line = input[y]
    if x < 0 or x > line.__len__() - 1: return False
    if not safe_int(line[x]): return False
    num_string = [line[x]]
    seen_dict[y][x] = True

    # go left
    x_left = 1
    while True:
        if line[x - x_left] == None: 
            break

        if safe_int(line[x - x_left]):
            num_string.insert(0, line[x - x_left])
            seen_dict[y][x - x_left] = True

        else: break

        x_left += 1

    # go right
    x_right = 1
    while True:
        if line[x + x_right] == None: 
            break

        if safe_int(line[x + x_right]):
            num_string = num_string + [line[x + x_right]]
            seen_dict[y][x + x_right] = True

        else: break

        x_right += 1

    return safe_int("".join(num_string))
        
def solution(input):
    sum = 0
    ## Pass the seen dict into find_num so that we can "blank the number out by recording where we've seen numbers.
    ## You'll need to now pass line number into find_num to accurately report the coordinates of where we've seen numbers before.
    seen_dict = defaultdict(lambda: defaultdict(lambda: None))


    matrix_len = input.__len__()
    
    for line_num in range(matrix_len):
        if input[line_num] == None: break
        line_len = input[line_num].__len__()

        print(input[line_num], 'curr line')
        for x in range(line_len):
            print(input[line_num][x], 'curr char')

            if isPart(input[line_num][x]):
                print('LOOKING FOR STUFF')
                # look for numbers and blank them out
                # up
                if line_num - 1 > 0 and not seen_dict[line_num -1][x]: 
                        maybe_num = find_num(line_num - 1, x, input, seen_dict)
                        if maybe_num:
                            sum += maybe_num
                        
                    # up left
                if line_num - 1 > 0 and not seen_dict[line_num - 1][x - 1]:
                        if x > 0:
                            maybe_num = find_num(line_num - 1, x - 1, input, seen_dict)
                            if maybe_num:
                                sum += maybe_num
                        
                    # up right
                if line_num - 1 > 0 and not seen_dict[line_num - 1][x + 1]:
                        maybe_num = find_num(line_num - 1, x + 1, input, seen_dict)
                        if maybe_num:
                            sum += maybe_num
                        
                    # right 
                if  not seen_dict[line_num][x + 1]:
                        maybe_num = find_num(line_num, x + 1, input, seen_dict)
                        if maybe_num:
                            sum += maybe_num
                        
                    # down right
                if line_num + 1 < matrix_len - 1 and not seen_dict[line_num + 1][x + 1]:
                        maybe_num = find_num(line_num + 1, x + 1, input, seen_dict)
                        if maybe_num:
                            sum += maybe_num

                    # down 
                if line_num + 1 < matrix_len - 1 and not seen_dict[line_num + 1][x]:
                        maybe_num = find_num(line_num + 1, x, input, seen_dict)
                        if maybe_num:
                            sum += maybe_num

                    # down left
                if line_num + 1 < matrix_len - 1 and not seen_dict[line_num + 1][x -1]:
                        if x > 0:
                            maybe_num = find_num(line_num + 1, x - 1, input, seen_dict)
                            if maybe_num:
                                sum += maybe_num

                    # left
                        if x > 0 and not seen_dict[line_num][x - 1]:
                            maybe_num = find_num(line_num, x - 1, input, seen_dict)
                            if maybe_num:
                                print(maybe_num, 'this is maybe_num')
                                print(sum, 'this is sum')
                                sum += maybe_num
    print(input)

    return sum


test_matrix = [matrix[0], matrix[1]]
print(test_matrix, 'this is the test matrix')
print(solution(test_matrix))
print(solution(matrix))


