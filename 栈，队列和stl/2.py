# 读取第一行 n 总巧克力数量，K 早上要吃的个数
n, K = map(int, input().split())
# A：早上甜蜜值
A = list(map(int, input().split()))
# B：晚上甜蜜值
B = list(map(int, input().split()))

sum_b = 0
diff = []
for a, b in zip(A, B):
    sum_b += b
    diff.append(a - b)

# 差值从大到小排序
diff.sort(reverse=True)
# 选前K个最大差值加上
for i in range(K):
    sum_b += diff[i]

print(sum_b)
