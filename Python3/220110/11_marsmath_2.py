T = int(input())
j = 0
b = 0


def calc(a):
    if a == '@':
        return b*3
    elif a == '%':
        return b+5
    elif a == '#':
        return b-7
    else:
        return float(a)


while j < T:
    j += 1
    i = 0
    input_num = list(input().split())

    while i < len(input_num):
        b = calc(input_num[i])
        i += 1
    print(round(b, 2))