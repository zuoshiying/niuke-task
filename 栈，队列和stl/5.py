s = input().strip()
cnt_a = 0
cnt_b = 0
flag = True

for ch in s:
    if ch == 'a':
        cnt_a += 1
    else:
        cnt_b += 1
    # 任何时刻b不能比a多
    if cnt_b > cnt_a:
        flag = False
        break

# 最后a和b数量必须相等
if flag and cnt_a == cnt_b:
    print("Good")
else:
    print("Bad")
