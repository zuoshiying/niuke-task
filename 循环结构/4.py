T = int(input())
for _ in range(T):
    n = int(input())
    mid = n // 2 + 1
    # 上半部分（包含中间行） i=1 ~ mid
    for i in range(1, mid + 1):
        # 空格：mid - i
        # 星：2*i -1
        print(" " * (mid - i) + "*" * (2*i - 1))
    # 下半部分 i=mid-1 往下到 1
    for i in range(mid - 1, 0, -1):
        print(" " * (mid - i) + "*" * (2*i - 1))
