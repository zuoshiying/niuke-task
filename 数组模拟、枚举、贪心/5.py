import sys

counts = list(map(int, sys.stdin.readline().split()))

odd_digits = [d for d in range(10) if counts[d] % 2 == 1]

if len(odd_digits) > 1:
    print(-1)
else:
    pairs = [counts[d] // 2 for d in range(10)]
    middle = str(odd_digits[0]) if odd_digits else ""
    total_pairs = sum(pairs)

    if total_pairs == 0:
        print(middle if middle else -1)
    else:
        first = -1
        for d in range(1, 10):
            if pairs[d] > 0:
                first = d
                break

        if first == -1:
            print(-1)
        else:
            pairs[first] -= 1
            left = str(first)
            for d in range(10):
                left += str(d) * pairs[d]
            right = left[::-1]
            print(left + middle + right)
