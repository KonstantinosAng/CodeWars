# see https://www.codewars.com/kata/56541980fa08ab47a0000040/solutions/python

def printer_error(s):
    colors = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    errors = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    error = 0
    for letter in s:
        if letter in errors:
            error += 1
    return f"{error}/{len(s)}"



s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(printer_error(s) == "3/56")