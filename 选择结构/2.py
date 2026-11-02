n = int(input("在一行中输入一个正整数(1≦n≦10^5):"))

if n % 2 == 1:
    res = 3 * n + 1
else:
    res = n // 2
print(res)
