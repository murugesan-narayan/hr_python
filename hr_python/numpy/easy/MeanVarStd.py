import numpy

if __name__ == '__main__':
    a = []
    for i in range(int(input().split()[0])):
        a.append(input().split())
    a = numpy.array(a, numpy.int)
    print(numpy.mean(a, axis=1))
    print(numpy.var(a, axis=0))
    print(numpy.around(numpy.std(a), 12))
