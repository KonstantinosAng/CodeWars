# see https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1/solutions/python

def capitalize(s,ind):
    ret = ''
    for i, letter in enumerate(s):
        if i in ind:
            ret += letter.upper()
        else:
            ret += letter
    return ret

print(capitalize("abcdef",[1,2,5]) == 'aBCdeF')
print(capitalize("abcdef",[1,2,5,100]) == 'aBCdeF',)
print(capitalize("codewars",[1,3,5,50]) == 'cOdEwArs')
print(capitalize("abracadabra",[2,6,9,10]) == 'abRacaDabRA')
print(capitalize("codewarriors",[5]) == 'codewArriors')