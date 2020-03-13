# More details on this kata
# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string):
    _string = ''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for s in string:
        if s in vowels:
            continue
        _string += s
    string = _string
    return string
