n = int(input())
lst = list(map(int, input().split()))
if n == 1:
    print("无法判断")
else:
    a, b = lst[-2], lst[-1]
    if b > a:
        print("UP")
    else:
        print("DOWN")
