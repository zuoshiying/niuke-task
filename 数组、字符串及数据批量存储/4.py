L, M = map(int, input().split())
remove = set()
for _ in range(M):
    l, r = map(int, input().split())
    for i in range(l, r+1):
        remove.add(i)
ans = (L + 1) - len(remove)
print(ans)
