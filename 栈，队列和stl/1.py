def dfs(path, used, f):
    if len(path) == 8:
        f.write(' '.join(map(str, path)) + "\n")
        return
    for i in range(1,9):
        if not used[i]:
            used[i] = True
            path.append(i)
            dfs(path, used, f)
            path.pop()
            used[i] = False

used = [False] * 9
with open("perm.txt", "w", encoding="utf-8") as f:
    dfs([], used, f)

