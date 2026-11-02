n, x = map(int, input().split())
s = str(x)
lst = []
for i in range(1, n + 1):
    lst.append(str(i))  # 把每个数字转字符串加入列表
# 统计
cnt = 0
for u in lst:
    cnt += u.count(s)
print(cnt)
