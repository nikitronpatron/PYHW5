## Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def Rle(data):
    out = ''
    prevChar = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != prevChar:
            if prevChar:
                out += str(count) + prevChar
            count = 1 
            prevChar = char
        else:
            count += 1
    else:
        out += str(count) + prevChar 
        return out

string = Rle("aaaaabbccccccccccccdddeffaaaaaaacc")
print(string)

def RleDecode(data):
    out = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            out += char * int(count)
            count = ''
    return out

string = RleDecode("4a11b2c4d4a4d1b")
print(string)