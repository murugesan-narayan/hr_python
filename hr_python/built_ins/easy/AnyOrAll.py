if __name__ == '__main__':
    input()
    m = input().split()
    print(all(int(a) > 0 for a in m) and any(int(a) < 10 or a[0] == a[1] for a in m))
