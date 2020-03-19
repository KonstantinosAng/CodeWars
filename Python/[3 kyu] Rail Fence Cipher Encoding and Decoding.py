# More details on this kata
# https://www.codewars.com/kata/58c5577d61aefcf3ff000081

def encode_rail_fence_cipher(string, n):
    if string == '': return ''
    _map = [[None for x in range(len(string))] for y in range(n)]
    i, j, down, ret = 0, 0, True, []
    while j <= len(string) - 1:
        _map[i][j] = string[j]
        if i == n - 1:
            down = False
        if i == 0:
            down = True
        if down: 
            i += 1
        else:
            i -= 1
        j += 1
    for i in range(n):
        for j in range(len(string)):
            if _map[i][j] is not None:
                ret.append(_map[i][j]) 
    return ''.join(ret)

def decode_rail_fence_cipher(string, n):
    if string == '': return ''
    _map = [[None for x in range(len(string))] for y in range(n)]
    i, j, down, ret, index = 0, 0, True, '', 0
    while j <= len(string) - 1:
        _map[i][j] = 'x'
        if i == n - 1:
            down = False
        if i == 0:
            down = True
        if down: 
            i += 1
        else:
            i -= 1
        j += 1
    for i in range(n):
        for j in range(len(string)):
            if index >= len(string): break
            if _map[i][j] == 'x':
                _map[i][j] = string[index]
                index += 1
    i, j, down = 0, 0, True
    while j <= len(string) - 1:
        ret += _map[i][j]
        if i == n - 1:
            down = False
        if i == 0:
            down = True
        if down: 
            i += 1
        else:
            i -= 1
        j += 1
    return ret
