T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    # 极差 = 最大值 - 最小值
    max_a = max(arr)
    min_a = min(arr)
    r = max_a - min_a

    # 求平均值
    avg = sum(arr) / n
    # 方差：1/n * Σ (xi - avg)^2
    s2 = 0.0
    for x in arr:
        s2 += (x - avg) ** 2
    s2 = s2 / n

    # 输出：极差整数，方差保留3位小数
    print(f"{r} {s2:.3f}")
