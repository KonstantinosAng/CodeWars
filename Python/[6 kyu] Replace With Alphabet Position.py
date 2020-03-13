# More details on this Kata
# https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    import string
    ascii = string.ascii_lowercase
    _text = ''
    for i, c in enumerate(text.lower()):
        if ascii.find(c) != -1:
            if i != len(text) - 1:
                _text += f"{str(ascii.find(c) + 1)} "
                continue
            _text += str(ascii.find(c) + 1)
    return _text
