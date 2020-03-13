# More details on this Kata
# https://www.codewars.com/kata/56747fd5cb988479af000028

def get_middle(s):
    if len(s) == 1:
        return s
    if len(s) == 2:
        return s
    if len(s) % 2 == 0:
        return str(s[int(len(s)/2)-1]) + str(s[int(len(s)/2)])
    return s[int((len(s) - 1)/2)]
