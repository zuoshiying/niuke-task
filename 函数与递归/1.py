L, R = map(int, input().split())
res = 0
for i in range(L, R+1):
    res += str(i).count('2')
print(res)
