def minion_game(string):
    # your code goes here
    kevin_sub_str_count = 0
    stuart_sub_str_count = 0
    n = len(string)
    vowels = 'AEIOU'
    for i in range(n):
        if string[i] in vowels:
            kevin_sub_str_count += n - i
        else:
            stuart_sub_str_count += n - i
    if kevin_sub_str_count > stuart_sub_str_count:
        print(f"Kevin {kevin_sub_str_count}")
    elif stuart_sub_str_count > kevin_sub_str_count:
        print(f"Stuart {stuart_sub_str_count}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
