import numpy

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(str(numpy.eye(a, b, k=0)).replace('1', ' 1').replace('0', ' 0'))
