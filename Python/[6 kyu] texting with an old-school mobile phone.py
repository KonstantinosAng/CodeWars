# see https://www.codewars.com/kata/5ca24526b534ce0018a137b5/solutions/python

from TestFunction import Test

def send_message(message):
  key_map = {'.': 1, ',': 11, '?': 111, '!': 1111, 'a': 2, 'b': 22, 'c': 222,
             'd': 3, 'e': 33, 'f': 333, 'g': 4, 'h': 44, 'i': 444, 'j': 5, 'k': 55, 'l': 555,
             'm': 6, 'n': 66, 'o': 666, 'p': 7, 'q': 77, 'r': 777, 's': 7777, 't': 8, 'u': 88,
             'v': 888, 'w': 9, 'x': 99, 'y': 999, 'z': 9999, "'": '*', '-': '**', '+': '***',
             '=': '****', '*': '*-', "#": "#-", '0': 0, ' ': 0}
  rv = ''
  upper = False
  for letter in message:
    if letter == ' ':
      if len(rv) >= 1:
        if rv[-1] == str(key_map[letter.lower()])[0]:
          rv += ' '
      rv += '0'
    elif not letter.isalpha():
      if not letter.isdigit():
        if len(rv) >= 1:
          if rv[-1] == str(key_map[letter.lower()])[0]:
            rv += ' '
        rv += str(key_map[letter])
      else:
        if len(rv) >= 1:
          if rv[-1] == str(letter):
            rv += ' '
        rv += f'{letter}-'
    else:
      if letter.isupper():
        if not upper:
          rv += '#'
          upper = True
      else:
        if upper: 
          rv += '#'
          upper = False
      if len(rv) >= 1:
        if rv[-1] == str(key_map[letter.lower()])[0]:
          rv += ' '
      rv += str(key_map[letter.lower()])
  return rv

test = Test(None)

messages = [
  ["hey", "4433999"],
  ["one two three", "666 6633089666084477733 33"],
  ["Hello World!", "#44#33555 5556660#9#66677755531111"],
  ["Def Con 1!", "#3#33 3330#222#666 6601-1111"],
  ["A-z", "#2**#9999"],
  ["LOL xD", "#5556665550#99#3"],
  ["1984", "1-9-8-4-"],
  ["     ", "0 0 0 0 0"],
  ["A--b==C", "#2** **#22**** ****#222"],
  ["Big thanks for checking out my kata", "#22#444 4084426655777703336667770222443322255444664066688 806999055282"],
  ["a2D3", "2 2-#3 3-"]
]
  
for message, answer in messages:
  test.assert_equals(send_message(message), answer, 'Message: ' + message)
