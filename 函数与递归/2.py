def get_days(y, m):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if m == 2:
        if (y%4==0 and y%100!=0) or (y%400==0):
            return 29
        else:
            return 28
    return month_days[m-1]

res_list = []
while True:
    try:
        y, m, x = map(int, input().split())
        cnt = 0
        days = get_days(y, m)
        t = str(x)
        for d in range(1, days + 1):
            s = f"{y:04d}-{m:02d}-{d:02d}"
            cnt += s.count(t)
        res_list.append(cnt)
    except EOFError:
        break

for ans in res_list:
    print(ans)
