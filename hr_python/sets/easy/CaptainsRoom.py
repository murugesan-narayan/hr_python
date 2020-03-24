if __name__ == '__main__':
    n = int(input())
    rooms_list = list(map(int, input().split()))
    x = {}
    for i in rooms_list:
        if i in x:
            x[i] += 1
        else:
            x[i] = 1
    for j in x:
        if x[j] == 1:
            print(j)
            break
