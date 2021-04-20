# see https://www.codewars.com/kata/58e24788e24ddee28e000053/train/python

def simple_assembler(program):
  memory = {}
  pointer = 0
  while pointer < len(program):
    cmd = program[pointer].split(" ")
    if cmd[0] == 'mov':
      if not cmd[2].isalpha():
        if cmd[2].isdigit():
          memory[cmd[1]] = int(cmd[2])
        else: 
          memory[cmd[1]] = float(cmd[2])
      else:
        if cmd[2] in memory:
          memory[cmd[1]] = memory[cmd[2]]
      pointer += 1
    elif cmd[0] == 'inc':
      if cmd[1] in memory:
        memory[cmd[1]] += 1
      pointer += 1
    elif cmd[0] == 'dec':
      if cmd[1] in memory:
        memory[cmd[1]] -= 1
      pointer += 1
    elif cmd[0] == 'jnz':
      if not cmd[1].isalpha():
        if cmd[1].isdigit():
          if int(cmd[1]) == 0:
            pointer += 1
            continue
          else:
            pointer += int(cmd[2])
        else: 
          if float(cmd[1]) == 0.0:
            pointer += 1
            continue
          else:
            pointer += int(cmd[2])
      else:
        if memory[cmd[1]] != 0:
          pointer += int(cmd[2])
        else:
          pointer += 1
          continue        
    else:
      pointer += 1
      continue
  return memory
  

from TestFunction import Test
test = Test(None)
code = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''
test.assert_equals(simple_assembler(code.splitlines()), {'a': 1})

code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
test.assert_equals(simple_assembler(code.splitlines()), {'a': 409600, 'c': 409600, 'b': 409600})
