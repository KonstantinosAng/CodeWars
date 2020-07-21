# see https://www.codewars.com/kata/5d50e3914861a500121e1958/solutions/python

def add_letters(*letters):
    sum = 0
    for letter in letters:
        sum += ord(letter) - 96
    while sum > 26 :
        sum -= 26
    return chr(sum + 96) if letters != () else 'z'
        

tests = [
        (['a', 'b', 'c'], 'f'),
        (['z'], 'z'),
        (['a', 'b'], 'c'),
        (['c'], 'c'),
        (['z', 'a'], 'a'),
        (['y', 'c', 'b'], 'd'),
        ([], 'z')
        ]

for i, o in tests:
    str = ', '.join(['"' + s + '"' for s in i])
    print(add_letters(*i) == o)