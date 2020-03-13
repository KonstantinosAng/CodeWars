# More details on this kata
# https://www.codewars.com/kata/550498447451fbbd7600041c

def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    if len(array1) != len(array2):
        return False
    for n in array1:
        if n*n not in array2:
            return False
    dubl = [0 for x in range(len(array1))]
    for i, n in enumerate(array1):
        dubl[i] = array1.count(n)
    print(dubl)
    for i, d in enumerate(dubl):
        if d > 1:
            if array2.count(array1[i]*array1[i]) != d:
                return False
    return True
