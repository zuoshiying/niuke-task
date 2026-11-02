n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ok = False
ans = []

for i in range(n - 2):
    x = arr[i]
    y = arr[i+1]
    z = arr[i+2]
    if x + y > z:
        ans = [x, y, z]
        ok = True
        break

if ok:
    print(ans[0], ans[1], ans[2])
else:
    print("No solution")
