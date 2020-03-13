# More details on this kata
# https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(text):
    import string
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    words = text.split()
    _words, _test, ret = [], '', ''
    for word in words:
        if len(word) == 1:
            if word in upper or word in lower:
                _words.append(word + 'ay')
                continue
            _words.append(word)
            continue
        for i in range(len(word)-1):
            if word[0] in upper or word[0] in lower:
                _test += word[i+1]
                continue
        _test += word[0] + 'ay'
        _words.append(_test)
        _test = ''
    for i, w in enumerate(_words):
        if i == len(_words) - 1:
            ret += w
            break
        ret += f"{w} "
    return ret
