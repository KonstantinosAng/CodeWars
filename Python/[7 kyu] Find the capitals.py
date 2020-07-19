# see https://www.codewars.com/kata/53573877d5493b4d6e00050c/solutions/python

def capital(capitals):
    arr = []
    for d in capitals:
        if 'country' in d:
            arr.append(f"The capital of {d['country']} is {d['capital']}")
        else:
            arr.append(f"The capital of {d['state']} is {d['capital']}")
    return arr


state_capitals = [{'state': 'Maine', 'capital': 'Augusta'}]
print(capital(state_capitals) == ["The capital of Maine is Augusta"]);
country_capitals = [{'country' : 'Spain', 'capital' : 'Madrid'}]
print(capital(country_capitals) == ["The capital of Spain is Madrid"])
mixed_capitals = [{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}]
print(capital(mixed_capitals) == ["The capital of Maine is Augusta", "The capital of Spain is Madrid"])