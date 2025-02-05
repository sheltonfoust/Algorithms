def kmp(s, p):
    res = []
    j = 0
    lps = [0] * len(p)
    for i in range(1, len(p)):
        while p[i] != p[j] and j > 0:
            j = lps[j - 1]
            if p[i] == p[j]:
                j += 1
                lps[i] = j
    j, i = 0, 0
    while i < len(s):
        if s[i] == p[j]:
            i += 1
            j += 1
            if j == len(p):
                res.append(i - len(p))
                j = lps[j - 1]
        elif j == 0:
            i += 1
        else:
            j = lps[j - 1]
    return res