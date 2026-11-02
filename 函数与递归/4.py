x, y = map(int, input().split())
cnt = 0
for n in range(x, y + 1):
    s = 0
    t = n
    while t > 0:
        s += t % 10
        t //= 10
    if s % 5 == 0:
        cnt += 1
print(cnt)
