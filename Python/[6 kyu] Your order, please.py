# More on this kata
# https://www.codewars.com/kata/55c45be3b2079eccff00010f

def order(sentence):
    if sentence is None:
        return []
    letters, ret = {}, ''
    for word in sentence.split():
        for letter in word:
            if letter.isdigit():
                letters.update({word:int(letter)})
    for i, el in enumerate(sorted(letters.items(), key=lambda x: x[1])):
        if i == len(letters) - 1:
            ret += el[0]
            continue
        ret += f"{el[0]} "
    return ret

