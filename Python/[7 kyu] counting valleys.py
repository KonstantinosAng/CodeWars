# see https://www.codewars.com/kata/5da9973d06119a000e604cb6/solutions/python

def counting_valleys(s): 
    valleys = 0
    height = 0
    inValley = False
    for letter in s:
        if letter == "U":
            height += 1
        elif letter == "D":
            height -= 1
        else:
            continue
        if height < 0: inValley = True
        if inValley and height >= 0: 
            valleys += 1
            inValley = False
    return valleys
        

print(counting_valleys('UFFFD') == 0)
print(counting_valleys('DFFFD') == 0)
print(counting_valleys('UFFFU') == 0)
print(counting_valleys('DFFFU') == 1)
print(counting_valleys('UFFDDFDUDFUFU') == 1)
print(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFU') == 2)
print(counting_valleys('UFFDDFDUDFUFUUFFDDUFFDDUFFDDUDUDUDUDUDUUUUUUUUU') == 3)
print(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU') == 4)
print(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU') == 6)
