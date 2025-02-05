def partition(s):
    res, part = [], []
    def dfs(i):
        if i >= len(s):
            res.append(part.copy())
            return
        for j in range(i, len(s)):
            part.append(s[i : j + 1])
            dfs(j + 1)
            part.pop()
    dfs(0)
    return res