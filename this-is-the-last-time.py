import sys
import heapq
 
input = sys.stdin.readline
 
def lastTime(first_line, second_line):
    second_line.sort()
    
    n = first_line[0]
    obt_coin = first_line[1]
    available_rewards = []
    ptr = 0
    
    while True:
        while ptr < n and second_line[ptr][0] <= obt_coin:
            l, r, real = second_line[ptr]
            if obt_coin <= r and real > obt_coin:
                heapq.heappush(available_rewards, -real)
            ptr += 1
        
        found_upgrade = False
        while available_rewards:
            best_reward = -heapq.heappop(available_rewards)
            if best_reward > obt_coin:
                obt_coin = best_reward
                found_upgrade = True
                break
        
        if not found_upgrade:
            break
            
    return obt_coin
line = input().split()
if line:
    t = int(line[0])
    for _ in range(t):
        n, k = map(int, input().split())
        
        second_line = []
        for _ in range(n):
            l, r, real = map(int, input().split())
            second_line.append([l, r, real])
        
        print(lastTime([n, k], second_line))
