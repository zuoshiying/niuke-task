n, k, m = map(int, input().split())
people = list(range(n))   # [0,1,2,...,n-1]
idx = k                   # 从k号开始

while len(people) > 1:
   # 起点是idx，往后走 m-1 步
 step = m - 1
 idx = idx + step
  # 绕圈
 idx = idx % len(people)
 people.pop(idx)   # 删掉这个人！

print(people[0])
