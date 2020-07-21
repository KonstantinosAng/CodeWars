# see https://www.codewars.com/kata/5650ab06d11d675371000003/solutions/python

def split_in_parts(s, part_length): 
    ret = ''
    for i, letter in enumerate(s):
        if i%part_length == 0 and i != 0:
            ret += " " + letter
        else:
            ret += letter
    return ret


print(split_in_parts("supercalifragilisticexpialidocious", 3) == "sup erc ali fra gil ist ice xpi ali doc iou s")
print(split_in_parts("HelloKata", 1) == "H e l l o K a t a")
print(split_in_parts("HelloKata", 9) == "HelloKata")