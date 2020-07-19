# see https://www.codewars.com/kata/55968ab32cf633c3f8000008/solutions/python

def initials(name):
    names = name.split(" ")
    ret = ''
    for i, name in enumerate(names):
        if i == len(names) - 1:
            ret += name.capitalize()
            break
        ret += name[0].upper() + '.'
    return ret

print(initials('code wars') == 'C.Wars')
print(initials('Barack hussein obama') == 'B.H.Obama')
print(initials('barack hussein Obama') == 'B.H.Obama')