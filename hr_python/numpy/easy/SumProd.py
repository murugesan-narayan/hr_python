import numpy
numpy.set_printoptions(sign=' ')
if __name__ == '__main__':
    a = []
    for i in range(int(input().split()[0])):
        a.append(input().split())
    a = numpy.array(a, numpy.int)
    s = numpy.sum(a, axis=0)
    print(numpy.prod(s))
