def skibidus(t, sizes, a, b):
    b.sort()
    m = len(b)
    
    def helper(i):
        prev_val = a[i-1]
        target = prev_val + a[i]
        left = 0
        right = m - 1
        res = float('inf')
        
        while left <= right:
            mid = (left + right) // 2
            if b[mid] >= target:
                res = b[mid] - a[i]
                right = mid - 1
            else:
                left = mid + 1
        return res
        
    a[0] = min(a[0], b[0] - a[0])
    
    for i in range(len(a) - 1):
        prev_val = a[i]
        
        opt1 = a[i+1] if a[i+1] >= prev_val else float('inf')
        opt2 = helper(i + 1)
        
        best = min(opt1, opt2)
        
        if best == float('inf'):
            return "NO"
        
        a[i+1] = best
            
    return "YES"

t_input = input()
if t_input:
    t = int(t_input)
    for _ in range(t):
        sizes = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        print(skibidus(t, sizes, a, b))
