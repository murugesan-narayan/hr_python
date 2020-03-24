import numpy

if __name__ == '__main__':
    n = int(input())
    a, b = [], []
    [a.append(input().split()) for i in range(n)]
    [b.append(input().split()) for i in range(n)]
    a = numpy.array(a, numpy.int)
    b = numpy.array(b, numpy.int)
    print(numpy.dot(a, b))
