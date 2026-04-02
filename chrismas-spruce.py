from collections import defaultdict

ctr = defaultdict(int)
def chrismas(t, node):
    ctr[node] += 1
    return ctr



t = int(input())
result = defaultdict(int)
parent_map = {}

for i in range(2, t + 1):
    node = int(input())
    parent_map[i] = node  
    res = chrismas(t, node)
    result = res


for i in range(2, t + 1):
    if i in result:
        prior_key = parent_map[i]
        result[prior_key] -= 1
        

ans = "Yes"
for key, val in result.items():
    if val < 3:
        ans = "No"
        break

print(ans)
