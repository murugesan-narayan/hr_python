import numpy
numpy.set_printoptions(sign=' ')
if __name__ == '__main__':
    a = numpy.array(input().split(), numpy.float)
    print(numpy.floor(a))
    print(numpy.ceil(a))
    print(numpy.rint(a))
