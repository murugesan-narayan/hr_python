if __name__ == '__main__':
    s1 = set(map(int, input().split()))
    t = int(input())
    result = True
    for i in range(t):
        s2 = set(map(int, input().split()))
        result = s1.issuperset(s2)
        if not result:
            break;
    print(result)
