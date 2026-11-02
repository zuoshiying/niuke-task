import math

# 定义一个函数：判断一个数是不是素数
def is_prime(n):
    if n < 2:        # 小于2一定不是素数
        return False
    if n == 2:       # 2是唯一的偶素数
        return True
    if n % 2 == 0:   # 大于2的偶数直接不是素数
        return False
    # 只检查奇数，从3到根号n，步长2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# 读取输入，当成字符串，方便反转
t = input().strip()

# 构造题目要求的回文数
pal = t + t[::-1][1:]
num = int(pal)

# 判断并输出
if is_prime(num):
    print("prime")
else:
    print("noprime")
