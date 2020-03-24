import re


def and_or_rep(match):
    s = match.group(0)
    if s == '&&':
        return 'and'
    elif s == '||':
        return 'or'
    else:
        return s


if __name__ == '__main__':
    for i in range(int(input())):
        print(re.sub(r"(?<= )(&&|\|{2})(?= )", and_or_rep, input()))
