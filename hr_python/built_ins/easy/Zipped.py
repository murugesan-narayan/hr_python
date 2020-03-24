if __name__ == '__main__':
    l, n = map(int, input().split())
    lst = list()
    for i in range(n):
        ml = list(map(float, input().split()))
        lst.append(ml)
    lst = list(zip(*lst))
    for il in lst:
        print(sum(il)/n)
