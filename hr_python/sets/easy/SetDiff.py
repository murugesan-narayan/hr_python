if __name__ == '__main__':
    input()
    m = set(map(int, input().split()))
    input()
    n = set(map(int, input().split()))
    r = m.difference(n)
    print(len(r))
