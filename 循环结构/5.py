n = int(input())
mid = n + 1
# 上半部分
for i in range(1, mid + 1):
 print(" " * (2 * mid - 2 * i) + "*" * i)
# 下半部分
for i in range(mid - 1, 0, -1):
 print(" " * (2 * mid - 2 * i ) + "*" * i)
 
