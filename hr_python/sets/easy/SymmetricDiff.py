if __name__ == '__main__':
    input()
    m = set(map(int, input().split()))
    input()
    n = set(map(int, input().split()))
    sd = m.symmetric_difference(n)
    for v in sorted(sd):
        print(v)
