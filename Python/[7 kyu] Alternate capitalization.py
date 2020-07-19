# see https://www.codewars.com/kata/59cfc000aeb2844d16000075/solutions/python

def capitalize(s):
    s1, s2 = '', ''
    for i, letter in enumerate(s):
        if i%2 == 0:
            s1 += letter.upper()
            s2 += letter
        else:
            s1 += letter
            s2 += letter.upper()
    return [s1, s2]


print(capitalize("abcdef") == ['AbCdEf', 'aBcDeF'])
print(capitalize("codewars") == ['CoDeWaRs', 'cOdEwArS'])
print(capitalize("abracadabra") == ['AbRaCaDaBrA', 'aBrAcAdAbRa'])
print(capitalize("codewarriors") == ['CoDeWaRrIoRs', 'cOdEwArRiOrS'])