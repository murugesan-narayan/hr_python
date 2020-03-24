if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        input()
        s1 = set(map(int, input().split()))
        input()
        s2 = set(map(int, input().split()))
        print(s1.issubset(s2))
