T = int(input())
ans_list = []
for _ in range(T):
    parts = input().split()
    a = parts[0]
    b = parts[1]
    res = int(a) * int(b)
    ans_list.append(res)

for x in ans_list:
    print(x)
