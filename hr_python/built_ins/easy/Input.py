if __name__ == '__main__':
    x, k = map(int, input().split())
    eq = input()
    ev = eval(eq)
    print(ev == k)