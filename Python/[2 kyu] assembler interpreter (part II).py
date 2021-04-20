# see https://www.codewars.com/kata/58e61f3d8ff24f774400002c/train/python

from TestFunction import Test

cmp_output = {}
memory = {}
output = ''
code = ''

def assembler_interpreter(program, cmd=None):
  global cmp_output, memory, output, code
  if not cmd:
    code = (program + '.')[:-1]
  pointer = 0
  endNotFound = True
  program = program.splitlines()
  while pointer < len(program):
    if ';' in program[pointer]:
      program[pointer] = program[pointer][:program[pointer].find(';')]
      if program[pointer] == "":
        pointer += 1
        continue
    cmd = program[pointer].strip().split(" ")
    command = cmd[0]
    if command == 'mov':
      tmp_command = program[pointer].strip()[3:].strip()
      x, y = tmp_command.split(",")[0].strip(), tmp_command.split(",")[1].strip()
      if not y.isalpha():
        if y.isdigit():
          memory[x] = int(y)
        else:
          memory[x] = float(y)
      else:
        if y in memory:
          memory[x] = memory[y]
      pointer += 1
    elif command == 'cmp':
      tmp_command = program[pointer].strip()[3:].strip()
      x, y = tmp_command.split(",")[0].strip(), tmp_command.split(",")[1].strip()
      val_x, val_y = None, None
      if not x.isalpha():
        if x.isdigit():
          val_x = int(x)
        else:
          val_x = float(x)
      else:
        if x in memory:
          val_x = memory[x]
      if not y.isalpha():
        if y.isdigit():
          val_y = int(y)
        else:
          val_y = float(y)
      else:
        if y in memory:
          val_y = memory[y]
      cmp_output = {'x': val_x, 'y': val_y}
      pointer += 1
    elif command == 'msg':
      tmp_command = str(program[pointer].strip()[3:].strip())
      i = 0
      while i < len(tmp_command):
        if tmp_command[i] == "'" and i+1 != len(tmp_command):
          j = i + 1
          while tmp_command[j] != "'":
            j += 1
          output += tmp_command[i+1:j]
          i = j + 1
        elif tmp_command[i].isalpha():
          if tmp_command[i] in memory:
            output += str(memory[tmp_command[i]])
          i += 1
        else:
          i += 1
      pointer += 1
    elif command == 'inc':
      if cmd[-1] in memory:
        memory[cmd[-1]] += 1
      pointer += 1
    elif command == 'dec':
      if cmd[-1] in memory:
        memory[cmd[-1]] -= 1
      pointer += 1
    elif command == 'add' or command == 'sub' or command == 'mul' or command == 'div':
      tmp_command = program[pointer].strip()[3:].strip()
      x, y = tmp_command.split(",")[0].strip(), tmp_command.split(",")[1].strip()
      if not y.isalpha():
        if y.isdigit():
          val = int(y)
        else:
          val = float(y)
        if x in memory:
          if cmd[0] == 'add':
            memory[x] += val
          elif cmd[0] == 'sub':
            memory[x] -= val
          elif cmd[0] == 'mul':
            if type(memory[x]) == int and type(val) == int:
              memory[x] *= val
              memory[x] = int(memory[x])
            else:
              memory[x] *= val
          elif cmd[0] == 'div':
            if val != 0 and val != 0.0:
              if type(memory[x]) == int and type(val) == int:
                memory[x] /= val
                memory[x] = int(memory[x])
              else:
                memory[x] /= val
          else:
            pass
      else:
        if y in memory and x in memory:
          if cmd[0] == 'add':
            memory[x] += memory[y]
          elif cmd[0] == 'sub':
            memory[x] -= memory[y]
          elif cmd[0] == 'mul':
            memory[x] *= memory[y]
          elif cmd[0] == 'div':
            if val != 0 and val != 0.0:
              memory[x] /= memory[y]
          else:
            pass
      pointer += 1
    elif command == 'jnz':
      tmp_command = program[pointer].strip()[3:].strip()
      x, y = tmp_command.split(",")[0].strip(), tmp_command.split(",")[1].strip()
      if not x.isalpha():
        if x.isdigit():
          if int(x) == 0:
            pointer += 1
            continue
          else:
            pointer += int(y)
        else:
          if float(x) == 0.0:
            pointer += 1
            continue
          else:
            pointer += int(y)
      else:
        if memory[x] != 0:
          pointer += int(y)
        else:
          pointer += 1
          continue
    elif command == 'jne':
      function_name = program[pointer].strip()[3:].strip()
      if cmp_output['x'] != cmp_output['y']:
        assembler_interpreter('call ' + function_name, cmd=True)
      else:
        pass
      pointer += 1
    elif command == 'end':
      return output
    elif command == 'call':
      i = 0
      while i < len(program):
        if program[pointer].split()[1] in code.splitlines()[i] and code.splitlines()[i].split()[0] != 'call':
          while program[i+1][:4] == "    ":
            if program[i+1].strip() == 'ret':
              i = len(program)
              break
            assembler_interpreter(program[i+1], cmd=True)
            i += 1
        i += 1
      pointer += 1
    else:
      pointer += 1
      continue
    if pointer == len(program) and endNotFound:
      return -1
  return memory


test = Test(None)

# program = '''
# ; My first program
# mov  a, 5
# inc  a
# call function
# msg  '(5+1)/2 = ', a    ; output message
# end

# function:
#     div  a, 2
#     ret
# '''

# test.assert_equals(assembler_interpreter(program), '(5+1)/2 = 3')

program_factorial = '''
mov   a, 5
mov   b, a
mov   c, a
call  proc_fact
call  print
end

proc_fact:
    dec   b
    mul   c, b
    cmp   b, 1
    jne   proc_fact
    ret

print:
    msg   a, '! = ', c ; output text
    ret
'''

test.assert_equals(assembler_interpreter(program_factorial), '5! = 120')
