cube = lambda x: pow(x, 3)


def fibonacci(n):
    a = 0
    b = 1
    f_list = [a, b]
    for i in range(2, n):
        c = a + b
        f_list.append(c)
        a = b
        b = c
    return f_list[0:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
