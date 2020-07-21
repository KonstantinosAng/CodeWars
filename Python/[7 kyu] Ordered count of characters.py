# see https://www.codewars.com/kata/57a6633153ba33189e000074/solutions/python

def ordered_count(inp):
    counts = {}
    for letter in inp:
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1
    return [(key, value) for key, value in counts.items()]


tests = (
    ('abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
    ('Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)])
)

for t in tests:
    inp, exp = t
    print(ordered_count(inp) == exp)