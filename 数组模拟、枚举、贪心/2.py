middle = {
    (1, 3): 2,
    (1, 7): 4,
    (1, 9): 5,
    (2, 8): 5,
    (3, 7): 5,
    (3, 9): 6,
    (4, 6): 5,
    (7, 9): 8,
}

while True:
    try:
        s = input().strip()
    except EOFError:
        break

    used = set()
    valid = True
    prev = None

    for ch in s:
        n = int(ch)

        if n in used:
            valid = False
            break

        if prev is not None:
            a, b = min(prev, n), max(prev, n)
            if (a, b) in middle:
                if middle[(a, b)] not in used:
                    valid = False
                    break

        used.add(n)
        prev = n

    print("YES" if valid else "NO")
