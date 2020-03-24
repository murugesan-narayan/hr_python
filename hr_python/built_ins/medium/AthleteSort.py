if __name__ == '__main__':
    n, m = map(int, input().split())
    ma = []
    for i in range(n):
        ma.append(list(map(int, input().split())))
    k = int(input())
    ma = sorted(ma, key=lambda a: a[k])
    [print(*mi) for mi in ma]