# More details on this kata
# https://www.codewars.com/kata/526156943dfe7ce06200063e

class Brainfuck:

    def __init__(self, code, user_input):
        self._code = code
        self._user_input = user_input
        self._buffer = [0]
        self._pointer = 0
        self._loop_map = []
        self._output = ''
        self._input_pointer = 0

    def loop_mapping(self):
        loops = []
        for i, c in enumerate(self._code):
            if c == '[':
                loops.append(i)
            if c == ']':
                self._loop_map.append([loops[-1], i])
                del loops[-1]

    def evaluate(self):
        self.loop_mapping()
        i = 0
        while i < len(self._code):
            c = self._code[i]
            if c == '+':
                if self._buffer[self._pointer] < 255:
                    self._buffer[self._pointer] += 1
                else:
                    self._buffer[self._pointer] = 0
            if c == '-':
                if self._buffer[self._pointer] > 0:
                    self._buffer[self._pointer] -= 1
                else:
                    self._buffer[self._pointer] = 255
            if c == '>':
                if len(self._buffer) <= 2 ** 16:
                    self._buffer.append(0)
                    self._pointer += 1
                else:
                    self._pointer = 0
            if c == '<':
                if self._pointer == 0:
                    self._pointer = len(self._buffer) - 1
                else:
                    self._pointer -= 1
            if c == '[':
                if self._buffer[self._pointer] == 0:
                    for s, e in self._loop_map:
                        if s == i:
                            i = e
                            break
            if c == ']':
                if self._buffer[self._pointer] != 0:
                    for s, e in self._loop_map:
                        if e == i:
                            i = s
                            break
            if c == '.':
                self._output += chr(self._buffer[self._pointer])
            if c == ',':
                self._buffer[self._pointer] = ord(self._user_input[self._input_pointer])
                self._input_pointer += 1
            i += 1
        return self._output


def brain_luck(code, program_input):
    interpreter = Brainfuck(code, program_input)
    return interpreter.evaluate()
