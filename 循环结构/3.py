# ord(字符)拿到字母的 ASCII 数字，A=65，B=66，C=67
# chr(数字)把数字变回字符

ch = input().strip()
n = ord(ch) - ord('A') + 1

for i in range(1, n + 1):
    # 空格
    line = " " * (n - i)
    # 上升 A~目标字母
    for c in range(ord('A'), ord('A') + i):
        line += chr(c)
    # 下降 目标字母前一个 到 A
    for c in range(ord('A') + i - 2, ord('A') - 1, -1):
        line += chr(c)
    print(line)