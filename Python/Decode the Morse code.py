# More details on this Kata
# https://www.codewars.com/kata/54b724efac3d5402db00065e

def decodeMorse(morse_code):
    import re
    words = re.split(" ", morse_code)
    sentence, j = '', 0
    for i, w in enumerate(words):
        if len(w) == 0:
            j += 1
            continue
        if j > 1:
            if len(sentence) > 0:
                if MORSE_CODE[w].isalpha():
                    sentence += " "
                j = 0
        sentence += f'{MORSE_CODE[w]}'
    return sentence
