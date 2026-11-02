a, b = map(int, input().split()) 
# map表示把后面函数内容（一组东西)，全部用前面函数处理一遍
# input获取字符串
# split遇到中间那个空格，直接切开，作为两个数

if a < b:
    print('<')
elif a > b:
    print('>')
else:
    print('=')

# 预计输入内容：1 2
# 输出结果：<