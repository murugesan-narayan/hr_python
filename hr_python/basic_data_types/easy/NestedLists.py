if __name__ == '__main__':
    s_map = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        s = s_map.get(score)
        if s:
            s.append(name)
        else:
            s_map[score] = [name]
    keys = sorted(s_map.keys())
    result = s_map.get(keys[1])
    result.sort()
    for i in range(len(result)):
        print(result[i])
