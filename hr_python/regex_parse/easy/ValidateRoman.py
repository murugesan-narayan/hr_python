import re

if __name__ == '__main__':
    rr = r'(^(?=[MDCLXVI])M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$)'
    m = re.match(rr, input())
    print(True if m else False)
