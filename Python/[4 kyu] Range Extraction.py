# More details on this kata
# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

def solution(args):
    j, k, ret, flag, done = 0, 0, [], True, False
    for i in range(len(args)):
        if i + j >= len(args) - 1:
            ret.append(f"{args[-1]}")
            break
        flag = True
        if abs(args[i + j] - args[i + j + 1]) == 1:
            temp = i + j
            while flag:
                j += 1
                k += 1
                if i + j >= len(args) - 1:
                    if k >= 2:
                        ret.append(f"{args[temp]}-{args[i + j]}")
                    else:
                        ret.append(f"{args[temp]}")
                        ret.append(f"{args[i + j]}")
                    flag = False
                    done = True
                    break
                if abs(args[temp] - args[i + j + 1]) != k + 1:
                    if k >= 2:
                        ret.append(f"{args[temp]}-{args[i + j]}")
                    else:
                        ret.append(f"{args[temp]}")
                        ret.append(f"{args[i+j]}")
                    flag = False
                    k = 0
        else:
            ret.append(f"{args[i + j]}")
        if done: break
    return ','.join(x for x in ret)

