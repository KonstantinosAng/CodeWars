# see https://www.codewars.com/kata/51675d17e0c1bed195000001/solutions/python

def solution(digits):
    i = 0
    max = 0
    while i+5 <= len(digits):
        if int(digits[i:i+5]) > max:
            max = int(digits[i:i+5])
        else:
            i += 1
    return max