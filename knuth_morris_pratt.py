from test import *

def kmp(haystack, needle):
    if needle == "": return 0
    lps = [0] * len(needle)
    prevLPS, i = 0, 1
    while i < len(needle):
        if needle[i] == needle[prevLPS]:
            lps[i] = prevLPS + 1
            prevLPS += 1
            i += 1
        elif prevLPS == 0:

            lps[i] = 0
            i += 1
        else:
            prevLPS = lps[prevLPS - 1]
    
    i = 0  # ptr for haystack
    j = 0  # ptr for needle
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i, j = i + 1, j + 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
        
        if j == len(needle):
            return i - len(needle)
        
    return -1
kmp("1111001101", "1101")

print(test_pattern_matching(kmp, True))

