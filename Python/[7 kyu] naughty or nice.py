# see https://www.codewars.com/kata/52a6b34e43c2484ac10000cd/solutions/python

def get_nice_names(people):
    return [person["name"] for person in people if person["was_nice"]]

def get_naughty_names(people):
    return [person["name"] for person in people if not person["was_nice"]]



naughty = [{'name': 'xDranik', 'was_nice': False}]
nice = [{'name': 'Santa', 'was_nice': True}, {'name': 'Warrior reading this kata', 'was_nice': True}]

print(get_nice_names(naughty) == [])
print(get_nice_names(nice) == ['Santa', 'Warrior reading this kata'])
print(get_naughty_names(naughty) == ['xDranik'])
print(get_naughty_names(nice) == [])