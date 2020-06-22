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
    return x


