n, m = map(int, input().split())

# 输出第一个金字塔 n
for i in range(1, n+1):
    print(" " * (n - i) + "*" * (2*i - 1))
for i in range(n-1, 0, -1):
    print(" " * (n - i) + "*" * (2*i - 1))

# 输出第二个金字塔 m
for i in range(1, m+1):
    print(" " * (m - i) + "*" * (2*i - 1))
for i in range(m-1, 0, -1):
    print(" " * (m - i) + "*" * (2*i - 1))
