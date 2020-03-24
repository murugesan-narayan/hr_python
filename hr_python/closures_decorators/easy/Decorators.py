def wrapper(f):
    def fun(l):
        # complete the function
        for i in range(len(l)):
            l[i] = '+91 '+l[i][-10:-5]+' '+l[i][-5:]
        f(l)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


