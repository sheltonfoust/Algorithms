def manacher(t):
    l, r = 0, 0
    z = [0] * len(t)
    for i in range(len(t)):
        z[i] = min(z[l + r - i], r - i) if r > i else 0
        while (i - z[i] - 1 >= 0 and i + z[i] + 1 < len(t)
            and t[i - z[i] - 1] == t[i + z[i] + 1]):
            z[i] += 1
        if i + z[i] > r:
            l, r = i - z[i], i + z[i]
