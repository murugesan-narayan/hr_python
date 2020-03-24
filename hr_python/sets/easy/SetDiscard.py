if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    q = int(input())
    for i in range(q):
        qi = input().split()
        qs = qi[0]
        if qs == 'pop':
            s.pop()
        if qs == 'discard':
            s.discard(int(qi[1]))
        if qs == 'remove':
            s.remove(int(qi[1]))
    for v in s:
        print(v, end=" ")
