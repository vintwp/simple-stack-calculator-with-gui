import time
from math import pow, sqrt
start_time = time.time()
z = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '×': 2}

def parse_str(input_string):
    i = 0
    s1, s2 = [], []
    while i < len(input_string):
        if input_string[i] in z or input_string[i] in {'(', ')'}:
            input_string[i] = input_string[i]
            i_elem = input_string[i]
        else:
            try:
                input_string[i] = float(input_string[i])
                i_elem = input_string[i]
            except ValueError:
                print('Something wrong')
                exit()
        solution(input_string, i, i_elem, s1, s2)
        i += 1
    s1[0] = convert_to_int(s1[0])
    return s1[0]

def solution(input_string, i,  i_elem, s1, s2):
    if isinstance(i_elem, float):
        s1.append(i_elem)
        if i == len(input_string) - 1:
            mathematics(s1, s2)
            while len(s2) != 0:
                mathematics(s1, s2)
    elif i_elem in z:
        if len(s2) == 0:
            s2.append(i_elem)
        elif s2[len(s2) - 1] != '(':
            if z.get(s2[len(s2) - 1]) >= z.get(i_elem):
                mathematics(s1, s2)
                while len(s2) > 0 and s2[len(s2) - 1] != '(' and z.get(s2[len(s2) - 1]) >= z.get(i_elem):
                    mathematics(s1, s2)
                s2.append(i_elem)
            else:
                s2.append(i_elem)
        else:
            s2.append(i_elem)
    elif i_elem in {'(', ')'}:
        if i_elem == '(':
           s2.append(i_elem)
        else:
            while s2[len(s2) - 1] != '(':
                mathematics(s1, s2)
            s2.pop()
            if i == len(input_string) - 1:
                mathematics(s1, s2)
                while len(s2) != 0:
                    mathematics(s1, s2)

    return input_string

def mathematics(s1, s2):
    sym = s2[len(s2) - 1]
    if sym == '+':
        tmp = s1.pop(len(s1) - 2) + s1.pop(len(s1) - 1)
        s2.pop()
        s1.append(tmp)
    elif sym == '-':
        tmp = s1.pop(len(s1) - 2) - s1.pop(len(s1) - 1)
        s2.pop()
        s1.append(tmp)
    elif sym == '*' or sym == '×':
        tmp = s1.pop(len(s1) - 2) * s1.pop(len(s1) - 1)
        s2.pop()
        s1.append(tmp)
    elif sym == '/':
        try:
            tmp = s1.pop(len(s1) - 2) / s1.pop(len(s1) - 1)
        except ZeroDivisionError:
            tmp = 0
        s2.pop()
        s1.append(tmp)
    elif sym == '^':
        tmp = s1.pop(len(s1) - 2) ** s1.pop(len(s1) - 1)
        s2.pop()
        s1.append(tmp)
    return s1, s2

def convert_to_int(x):
    if x % 1 == 0:
        try:
            x = int(x)
        except ValueError:
            x = float(x)
            x = x * 0
    return x

#input_string = list(map(str, input().split()))
# sin1 = list(map(str, '1 / -1'.split())) # -1
# sin2 = list(map(str, '1 + 1 - 2 * 3'.split())) # -4
# sin3 = list(map(str, '1 + -1 - 3  * 3 + 10'.split())) #1
# sin4 = list(map(str, '1 + 2 * 3 + 4 / 2 - 0 * 3 - 4'.split())) #5
# sin5 = list(map(str, '3 * 1 + 1 + 1 * 3 - 4 - 1 * 1'.split())) #2
# sin6 = list(map(str, '18 / 2 - 2 * 3 + 12 / 3'.split())) #7
# sin7 = list(map(str, '2 * 9 - 18 / 3'.split())) #12
# sin8 = list(map(str, '1 + 2 * ( 3 + 4 / 2 - ( 1 + 2 ) ) * 2 + 1'.split())) # 10
# sin9 = list(map(str, '1 + ( 2 * 3 - 1 ) * 2'.split())) #11
# sin10 = list(map(str, '1 + ( 2 * 3 - 1 )'.split())) #6 !!!
# sin11 = list(map(str, '1 + ( 2 * 3 ) / 6'.split())) #2
# sin12 = list(map(str, '( 2 * 3 ) / 6 + 1'.split())) #2
# sin13 = list(map(str, '32 + 9 * ( 19 - 16 )'.split())) #59 !!!
# sin14 = list(map(str, '43 - ( 20 - 7 ) + 15'.split())) #45
# sin15 = list(map(str, '18 / ( 11 - 5 ) + 47'.split())) #50
# sin16 = list(map(str, '37 + 9 - 6 / 2 * 3'.split())) #37
# sin17 = list(map(str, '-10 - ( 2 - 4 ) * 3'.split())) #-4
# sin18 = list(map(str, '( ( 2 + 2 ) + ( 2 * 3 ) ) / 10'.split())) #1
# sin19 = list(map(str, '( 2 ^ 2 + 1 ) / 0'.split())) #10
sin20 = list(map(str, '2 * 0.5'.split())) #10

# print(parse_str(sin1))
# print(parse_str(sin2))
# print(parse_str(sin3))
# print(parse_str(sin4))
# print(parse_str(sin5))
# print(parse_str(sin6))
# print(parse_str(sin7))
# print(parse_str(sin8))
# print(parse_str(sin9))
# print(parse_str(sin10))
# print(parse_str(sin11))
# print(parse_str(sin12))
# print(parse_str(sin13))
# print(parse_str(sin14))
# print(parse_str(sin15))
# print(parse_str(sin16))
# print(parse_str(sin17))
# print(parse_str(sin18))
#print(parse_str(sin19))
print(parse_str(sin20))
print("--- %s seconds ---" % (time.time() - start_time))