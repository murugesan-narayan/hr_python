import string
if __name__ == '__main__':
    print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')
