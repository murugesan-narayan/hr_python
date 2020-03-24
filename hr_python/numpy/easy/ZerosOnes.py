import numpy

if __name__ == '__main__':
    v = tuple(map(int, input().split()))
    print(numpy.zeros(v, dtype=numpy.int))
    print(numpy.ones(v, dtype=numpy.int))
