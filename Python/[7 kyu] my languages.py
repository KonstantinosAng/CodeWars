# see https://www.codewars.com/kata/5b16490986b6d336c900007d/solutions/python

def my_languages(results):
    results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1])}
    return [key for key, value in results.items() if value >= 60][::-1]


print(my_languages({"Java": 10, "Ruby": 80, "Python": 65}) == ["Ruby", "Python"])
print(my_languages({"Hindi": 60, "Dutch": 93, "Greek": 71}) == ["Dutch", "Greek", "Hindi"])
print(my_languages({"C++": 50, "ASM": 10, "Haskell": 20}) == [])