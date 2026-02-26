def brokenKeyWord(t, s):
    s += "$" 
    ptr = 0
    ctr = 0
    res = set() 

    for i in range(len(s)):
        if s[i] == s[ptr]:
            ctr += 1
        else:
            if ctr % 2 != 0:
                res.add(s[ptr])
            ptr = i
            ctr = 1
    return "".join(sorted(list(res)))

t = int(input())
for _ in range(t):
    s = str(input())
    print(brokenKeyWord(t, s))



