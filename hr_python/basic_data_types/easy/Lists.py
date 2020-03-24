if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        ops = input().split()
        op = ops[0]
        if op == "insert":
            lst.insert(int(ops[1]), int(ops[2]))
        if op == "pop":
            lst.pop()
        if op == "remove":
            lst.remove(int(ops[1]))
        if op == "append":
            lst.append(int(ops[1]))
        if op == "sort":
            lst.sort()
        if op == "reverse":
            lst.reverse()
        if op == "print":
            print(lst)
