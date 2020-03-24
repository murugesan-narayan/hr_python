import numpy

if __name__ == '__main__':
    a = []
    [a.append(list(map(float, input().split()))) for i in range(int(input()))]
    print(numpy.around(numpy.linalg.det(a), 2))
