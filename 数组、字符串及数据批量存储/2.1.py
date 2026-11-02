n, x = map(int, input().split())
cnt = 0
for i in range(1, n + 1):
    t = i
    while t > 0:
        digit = t % 10   # 取出最后一位
        if digit == x:
            cnt += 1
        t = t // 10      # 去掉最后一位
print(cnt)


