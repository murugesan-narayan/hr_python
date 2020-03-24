if __name__ == '__main__':
    input()
    m = set(map(int, input().split()))
    input()
    n = set(map(int, input().split()))
    r = m.symmetric_difference(n)
    print(len(r))
