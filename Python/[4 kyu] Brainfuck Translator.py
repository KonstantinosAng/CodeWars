# More details on this kata
# https://www.codewars.com/kata/58924f2ca8c628f21a0001a1/discuss

def brainfuck_to_c(source_code):
    s, c_code, indentation, j, brackets = list(source_code), '', '', 0, 0
    while len(s) > 0:
        if s[0] not in ['+', '-', '<', '>', ',', '.', '[', ']']:
            del s[0]
            continue
        if ''.join(s[:2]) in ['+-', '-+', '<>', '><', '[]', ',,']:
            del s[0]
            del s[0]
            continue
        if s[0] == '+':
            while s[0] == '+':
                j += 1
                del s[0]
                if len(s) <= 0:
                    break
            c_code += indentation + "*p += {};\n".format(j)
            j = 0
            continue
        if s[0] == '-':
            while s[0] == '-':
                j += 1
                del s[0]
                if len(s) <= 0:
                    break
            c_code += indentation + '*p -= {};\n'.format(j)
            j = 0
            continue
        if s[0] == '<':
            while s[0] == '<':
                j += 1
                del s[0]
                if len(s) <= 0:
                    break
            c_code += indentation + 'p -= {};\n'.format(j)
            j = 0
            continue
        if s[0] == '>':
            while s[0] == '>':
                j += 1
                del s[0]
                if len(s) <= 0:
                    break
            c_code += indentation + 'p += {};\n'.format(j)
            j = 0
            continue
        if s[0] == '.':
            while s[0] == '.':
                c_code += indentation + "putchar(*p);\n"
                del s[0]
                if len(s) <= 0:
                    break
            continue
        if s[0] == ',':
            c_code += indentation + '*p = getchar();\n'
            del s[0]
            continue
        if s[0] == '[':
            c_code += indentation + 'if (*p) do {\n'
            indentation += '  '
            brackets += 1
            del s[0]
            continue
        if s[0] == ']':
            indentation = indentation[:-2]
            c_code += indentation + "} while (*p);\n"
            brackets += 1
            del s[0]
    if brackets % 2 == 1:
        return "Error!"
    return c_code
