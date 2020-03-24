import cmath


if __name__ == '__main__':
    cmx = complex(input())
    r, p = cmath.polar(cmx)
    # r = abs(cmath.sqrt(cmx.real**2+cmx.imag**2))
    print(r)
    # phase = cmath.phase(cmx)
    print(p)
