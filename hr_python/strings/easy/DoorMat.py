if __name__ == '__main__':
    n, m = map(int, input().split())
    c, w = '-', 'WELCOME'
    d, di = 3, 1
    for i in range(n//2):
        print(c * ((m-d)//2), '.|.' * di, c * ((m-d)//2), sep='')
        d += 6
        di += 2
    print(c * ((m - len(w)) // 2), w, c * ((m - len(w)) // 2), sep='')
    d -= 6
    di -= 2
    for i in range(n//2):
        print(c * ((m-d)//2), '.|.' * di, c * ((m-d)//2), sep='')
        d -= 6
        di -= 2
