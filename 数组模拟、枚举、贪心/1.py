n, t = map(int, input().split())
s = input().strip()

# 分割整数、小数
if '.' in s:
    int_part, dec_part = s.split('.')
    ints = list(int_part)
    decs = list(dec_part)
else:
    ints = list(s)
    decs = []

while t > 0:
    # 找小数里第一个 >='5' 的位置
    p = -1
    for i in range(len(decs)):
        if decs[i] >= '5':
            p = i
            break
    if p == -1:
        break  # 没有可以四舍五入的地方了
    
    t -= 1
    # 删掉p以及后面所有小数位，准备给p-1进位
    del decs[p:]
    carry = 1
    # 进位：先处理小数这边
    cur_pos = p - 1
    while carry and cur_pos >= 0:
        new_d = int(decs[cur_pos]) + carry
        if new_d == 10:
            decs[cur_pos] = '0'
            carry = 1
        else:
            decs[cur_pos] = str(new_d)
            carry = 0
        cur_pos -= 1
    # 小数这边进位还没消，进到整数部分
    idx = len(ints) - 1
    while carry and idx >= 0:
        new_d = int(ints[idx]) + carry
        if new_d == 10:
            ints[idx] = '0'
            carry = 1
        else:
            ints[idx] = str(new_d)
            carry = 0
        idx -= 1
    if carry:
        ints.insert(0, '1')

# 清理尾部0
while decs and decs[-1] == '0':
    decs.pop()

# 输出
if decs:
    print(''.join(ints) + '.' + ''.join(decs))
else:
    print(''.join(ints))
