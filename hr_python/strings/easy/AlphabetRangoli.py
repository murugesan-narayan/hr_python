import string


def print_rangoli(size):
    # your code goes here
    az = string.ascii_lowercase
    c = '-'
    s = az[:size]
    rs = s[::-1]
    p = size-1
    ts = 2*p + 1
    ui = 0
    for i in range(p):
        for i1 in range(2 * p - ui//2):
            print(c, end='')
        u1s = ''
        for u1 in range(ui//2):
            u1s += rs[u1//2] if u1 % 2 == 0 else c
        print(u1s, rs[i], u1s[::-1], end='', sep='')
        for i1 in range(2 * p - ui//2):
            print(c, end='')
        print()
        ui = ui + 4
    for i in range(2*p):
        print(rs[i//2] if i%2 == 0 else c, end='')
    print(s[0], end='')
    for i in range(1, 2*p +1):
        print(s[i//2] if i%2 == 0 else c, end='')
    print()
    ui = ui - 4
    for i in range(1, p+1):
        for i1 in range(2 * p - ui//2):
            print(c, end='')
        u1s = ''
        for u1 in range(ui//2):
            u1s += rs[u1//2] if u1 % 2 == 0 else c
        print(u1s, s[i], u1s[::-1], end='', sep='')
        for i1 in range(2 * p - ui//2):
            print(c, end='')
        print()
        ui = ui - 4


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
