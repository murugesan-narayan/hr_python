if __name__ == '__main__':
    input()
    s1 = set(map(int, input().split()))
    t = int(input())
    for i in range(t):
        op, c = input().split()
        s2 = set(map(int, input().split()))
        if op == 'intersection_update':
            s1.intersection_update(s2)
        elif op == 'update':
            s1.update(s2)
        elif op == 'symmetric_difference_update':
            s1.symmetric_difference_update(s2)
        elif op == 'difference_update':
            s1.difference_update(s2)
    print(sum(s1))
