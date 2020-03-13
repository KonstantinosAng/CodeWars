# More details on this kata
# https://www.codewars.com/kata/537e18b6147aa838f600001b

def justify(text, width):
    if not text: return ''
    if width == 0: return ''
    if not isinstance(text, str): return ''
    if len(text.split()) == 1: return text.strip() + '\n'
    t, l, ret = text.split(), [], ''
    for i, w in enumerate(t):
        l.append(w + ' ')
        if i + 1 <= len(t) - 1:
            if len(''.join(x for x in l) + t[i + 1]) > width:
                j, l[-1] = 0, l[-1].strip()
                if len(l) > 2:
                    while len(''.join(x for x in l)) < width:
                        l[j] += ' '
                        if j == len(l) - 2:
                            j = 0
                            continue
                        j += 1
                else:
                    if len(l) == 2:
                        l[1] = ''.join(c for c in l[1] if c != ' ')
                        while len(''.join(x for x in l)) < width:
                            l[0] += ' '
                    if len(l) == 1:
                        l[0] = l[0].strip()
                ret += ''.join(x for x in l) + '\n'
                l = []
        else:
            ret += (''.join(x for x in l)).strip() + '\n'
            l = []
    return ret[:-1]

