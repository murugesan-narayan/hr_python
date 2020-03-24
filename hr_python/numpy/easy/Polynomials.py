import numpy

if __name__ == '__main__':
    a, c = list(map(float, input().split())), int(input())
    print(numpy.polyval(a, c))
