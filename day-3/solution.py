import os

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
def find_num(line, x):
    if x < 0 or x > line.__len__() - 1: return False
    if not safe_int(line[x]): return False
    num_string = [line[x]]
    print(num_string, 'this is num_string')
    #line[x] = '.'
    # go left
    x_left = 1
    while True:
        if line[x - x_left] == None: 
            break

        if safe_int(line[x - x_left]):
            num_string.insert(0, line[x - x_left])
            #        line[x - x_left] = '.'

        else: break

        x_left += 1

    print(num_string, 'this is num_string after going left')
    # go right
    x_right = 1
    while True:
        if line[x + x_right] == None: 
            break

        if safe_int(line[x + x_right]):
            num_string = num_string + [line[x + x_right]]
            #       line[x + x_right] = '.'

        else: break

        x_right += 1

    print(num_string, 'this is num_string after going right')
    return safe_int("".join(num_string))
        
def solution(input):
    sum = 0

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
                if line_num - 1 > 0:
                    line = input[line_num - 1]
                    print(line, 'LOOKING IN THIS LINE')
                    if not line == None:
                        maybe_num = find_num(line, x)
                        if maybe_num:
                            sum += maybe_num
                        
                    # up left
                if line_num - 1 > 0:
                    line = input[line_num - 1]
                    print(line, 'LOOKING IN THIS LINE')
                    if not line == None:
                        if x > 0:
                            maybe_num = find_num(line, x - 1)
                            if maybe_num:
                                sum += maybe_num
                        
                    # up right
                if line_num - 1 > 0:
                    line = input[line_num - 1]
                    print(line, 'LOOKING IN THIS LINE')
                    if not line == None:
                        maybe_num = find_num(line, x + 1)
                        if maybe_num:
                            sum += maybe_num
                        
                    # right 
                if line_num - 1 > 0:
                    line = input[line_num]
                    print(line, 'LOOKING IN THIS LINE')
                    if not line == None:
                        maybe_num = find_num(line, x + 1)
                        if maybe_num:
                            sum += maybe_num
                        
                    # down right
                if line_num + 1 < matrix_len - 1:
                    line = input[line_num + 1]
                    print(line, 'LOOKING IN THIS LINE')
                    if not line == None:
                        maybe_num = find_num(line, x + 1)
                        if maybe_num:
                            sum += maybe_num

                    # down 
                if line_num + 1 < matrix_len - 1:
                    line = input[line_num + 1]
                    print(line, 'LOOKING IN THIS LINE')
                    if not line == None:
                        maybe_num = find_num(line, x)
                        if maybe_num:
                            sum += maybe_num

                    # down left
                if line_num + 1 < matrix_len - 1:
                    line = input[line_num + 1]
                    print(line, 'LOOKING IN THIS LINE')
                    if not line == None:
                        if x > 0:
                            maybe_num = find_num(line, x - 1)
                            if maybe_num:
                                sum += maybe_num

                    # left
                    line = input[line_num]
                    print(line, 'LOOKING IN THIS LINE')
                    if not line == None:
                        if x > 0:
                            maybe_num = find_num(line, x - 1)
                            if maybe_num:
                                sum += maybe_num
            

    return sum


test_matrix = [matrix[0], matrix[1]]
print(test_matrix, 'this is the test matrix')
print(solution(test_matrix))
print(solution(matrix))


