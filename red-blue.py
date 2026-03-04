def RedBlue(t,n,r,m,b):
    r_prefix = []
    r_sum = 0
    for i in range(len(r)):
        r_sum+=r[i]
        r_prefix.append(r_sum)
    b_prefix = []
    b_sum = 0
    for i in range(len(b)):
        b_sum+=b[i]
        b_prefix.append(b_sum)
    r_maximum = max(r_prefix)
    b_maximum = max(b_prefix)
    r_max = max(r_prefix) if r_maximum>=1 else 0
    b_max = max(b_prefix) if b_maximum>=1 else 0
    return r_max+b_max

t = int(input())


for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    print(RedBlue(t,n,r,m,b))
