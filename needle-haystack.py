from collections import Counter  
def needleHaystack(n, s, t):
    t_counter = Counter(t)
    s_counter = Counter(s)
    temp = ""
    for char in s_counter:
        if s_counter[char]>t_counter[char]:
            return "Impossible"

    for k, v in t_counter.items():
        diff = v-s_counter[k]
        temp+=k*diff
   
    sorted_temp = "".join(sorted(temp))
    lexicographic = []
    temp_ptr = 0
    s_ptr = 0
    while  temp_ptr < len(sorted_temp) and s_ptr < len(s):
        if sorted_temp[temp_ptr]<s[s_ptr]:
            lexicographic.append(sorted_temp[temp_ptr])
            temp_ptr+=1
        elif sorted_temp[temp_ptr]>s[s_ptr]:
            lexicographic.append(s[s_ptr])
            s_ptr+=1
        else:
            lexicographic.append(s[s_ptr])
            s_ptr += 1
    if temp_ptr < len(sorted_temp):
        lexicographic.append(sorted_temp[temp_ptr:])
    if s_ptr < len(s):
        lexicographic.append(s[s_ptr:])
    return "".join(lexicographic)

n = int(input())
for _ in range(n):
    s = str(input())
    t = str(input())
    print(needleHaystack(n, s, t))

