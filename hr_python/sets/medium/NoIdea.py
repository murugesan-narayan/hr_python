
if __name__ == '__main__':
    n, m = map(int, input().split())
    a = input().split()
    A = set(input().split())
    B = set(input().split())
    h = 0
    Ad = dict.fromkeys(A)
    Bd = dict.fromkeys(B)
    for k in a:
        if Ad.get(k, 0) != 0:
            h += 1
        elif Bd.get(k, 0) != 0:
            h -= 1
    print(h)
