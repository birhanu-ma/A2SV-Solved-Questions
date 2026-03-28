def flipTheBit(t, n, a, b):
    balance = 0
    good = [0]*n
    
    for i in range(n):
        if a[i] == '1':
            balance += 1
        else:
            balance -= 1
        
        if balance == 0:
            good[i] = 1
    
    flip = 0
    
    for i in range(n-1, -1, -1):
        curr = a[i]
        
        if flip:
            curr = '1' if curr == '0' else '0'
        
        if curr == b[i]:
            continue
        
        if good[i] == 0:
            print("NO")
            return
        
        flip ^= 1  
    
    print("YES")


t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()
    flipTheBit(t, n, a, b)
