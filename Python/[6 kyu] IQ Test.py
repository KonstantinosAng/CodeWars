# More details on this kata
# https://www.codewars.com/kata/552c028c030765286c00007d

def iq_test(numbers):
    numbers = [int(x) for x in numbers.split()]
    if numbers[0] % 2 == 0:
        flag = 'EVEN'
    if numbers[0] % 2 == 1:
        flag = 'ODD'
    for i, n in enumerate(numbers):
        if n % 2 == 0:
            _flag = 'EVEN'
        if n % 2 == 1:
            _flag = 'ODD'
        if flag != _flag:
            if i == 1:
                if numbers[2] % 2 == 0:
                    __flag = 'EVEN'
                else:
                    __flag = 'ODD'
                if flag == __flag:
                    return 2
                return 1
            return i + 1
