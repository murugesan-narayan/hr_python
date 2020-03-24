def print_formatted(number):
    # your code goes here
    b = bin(number)[2:]
    fl = len(b)
    for i in range(1, number+1):
        print(str(i).rjust(fl), str(oct(i)[2:]).rjust(fl),
              str(hex(i)[2:]).upper().rjust(fl),
              str(bin(i)[2:]).rjust(fl), sep='')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
