from collections import defaultdict
def SmallSet(n, segment):
    k = n[1]
    left = 0
    count = defaultdict(int)
    distinct_count = 0
    ans =0
    for right in range(len(segment)):
        if count[segment[right]] == 0:
            distinct_count+=1
        count[segment[right]]+=1
      
        while distinct_count>k:
            count[segment[left]]-=1
            if count[segment[left]]==0:
                distinct_count-=1
            left+=1
        ans+=(right-left+1)
    return ans
n = list(map(int, input().split()))
segment = list(map(int, input().split()))
print(SmallSet(n, segment))



