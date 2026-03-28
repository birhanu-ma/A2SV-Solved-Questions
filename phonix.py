from collections import Counter

def Phoenix(t, num, socks):
    n = num[0]
    l = num[1]
    r = num[2]
    
    left_socks = Counter(socks[:l])
    right_socks = Counter(socks[l:])
    
    for color in left_socks:
        if color in right_socks:
            match = min(left_socks[color], right_socks[color])
            left_socks[color] -= match
            right_socks[color] -= match
            l -= match
            r -= match
 
    if l < r:
        left_socks, right_socks = right_socks, left_socks
        l, r = r, l
    
    cost = 0
    to_flip = (l - r) // 2
    
    for color in left_socks:
        can_take = left_socks[color] // 2
        take = min(to_flip, can_take)
        cost += take
        to_flip -= take
        l -= 2 * take
        
    cost += (to_flip * 2) + r
    return cost

t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    socks = list(map(int, input().split()))
    print(Phoenix(t, nums, socks))
