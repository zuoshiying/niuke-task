import sys

patterns = [
    ("zero", "0"),
    ("four", "4"),
    ("nine", "9"),
    ("two", "2"),
    ("six", "6"),
    ("0", "0"),
    ("2", "2"),
    ("4", "4"),
    ("6", "6"),
    ("9", "9"),
]

T = int(sys.stdin.readline())
for _ in range(T):
    s = sys.stdin.readline().strip()
    result = []
    i = 0
    n = len(s)
    while i < n:
        matched = False
        for word, digit in patterns:
            if s.startswith(word, i):
                result.append(digit)
                i += len(word)
                matched = True
                break
        if not matched:
            i += 1
    print(''.join(result))
