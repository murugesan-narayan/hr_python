if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        try:
            a, b = map(int, input().split())
            print(a//b)
        except (ValueError, ZeroDivisionError) as e:
            print("Error Code:", e)
