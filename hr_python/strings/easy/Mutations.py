def mutate_string(string, position, character):
    part1 = string[:position]
    part2 = string[position+1:]
    return part1 + character + part2


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
