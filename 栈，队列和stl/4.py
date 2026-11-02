from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

n = int(input())
nums = input().split()
nums.sort(key=cmp_to_key(compare))
res = ''.join(nums)
print(res)
