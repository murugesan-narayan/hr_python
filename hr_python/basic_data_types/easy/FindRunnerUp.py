if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s = set(arr)
    lst = list(s)
    lst.sort()
    print(lst[-2])
