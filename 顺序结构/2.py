def is_valid(a, b): #定义a和b
    product = a * b
    total_str = str(a) + str(b) + str(product) #str函数转化成字符串
    if len(total_str) != 9:  #一共出现9个字符，则停止
        return False
     #集合里面出现不重复的数字，即1到9全部出现
    return set(total_str) == {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

ans = [] #枚举a <= b，防止a*b、b*a当成两个式子
for a in range(1, 10000):
    for b in range(a, 10000):
        if is_valid(a, b):
            ans.append((a * b, a, b))

# 排序规则：结果从小到大；结果相同，小乘数a从小到大
ans.sort(key=lambda x: (x[0], x[1]))

for c, a, b in ans:
    print(f"{c} = {a} x {b}")
