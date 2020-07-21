# see https://www.codewars.com/kata/52dbae61ca039685460001ae/solutions/python

def change(st):
    counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
              'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
              's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for letter in st:
        if letter.lower() in counts:
            counts[letter.lower()] = 1
    return "".join(str(value) for key, value in counts.items())
            

print(change("a **&  bZ") == "11000000000000000000000001")
print(change('Abc e  $$  z') == "11101000000000000000000001")
print(change("!!a$%&RgTT") == "10000010000000000101000000")
print(change("") == "00000000000000000000000000")
print(change("abcdefghijklmnopqrstuvwxyz") == "11111111111111111111111111")
print(change("aaaaaaaaaaa") == "10000000000000000000000000")
print(change("&%&%/$%$%$%$%GYtf67fg34678hgfdyd") == "00010111000000000001000010")
    