X, Y = map(int, input().split())

if Y % X == 0:
 Z = X + Y
else:
 Z = X - Y

print(Z)