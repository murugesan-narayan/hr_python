import numpy

if __name__ == '__main__':
    a, b = input().split(), input().split()
    a = numpy.array(a, numpy.int)
    b = numpy.array(b, numpy.int)
    print(numpy.inner(a, b))
    print(numpy.outer(a, b))
