def Longest(word):
    stack = [-1]
    max_len = 0
    num_longest = 0 
    for i, char in enumerate(word):
        if char == "(":
            stack.append(i)
        else:
            stack.pop()
            
            if not stack:
                stack.append(i)
            else:
                current_len = i - stack[-1]
                
                if current_len > max_len:
                    max_len = current_len
                    num_longest = 1
                elif current_len == max_len and max_len != 0:
                    num_longest += 1
    if max_len > 0: num_longest=num_longest 
    else: 
        num_longest = 1

    print(*[max_len, num_longest])

word = str(input())
Longest(word)
