from collections import Counter

def blackandwhite(t, num, letter):
    n = num[0]
    k = num[1]
    current_whites = letter[:k].count('W')
    min_changes = current_whites

    for i in range(k, n):
        if letter[i] == 'W':
            current_whites += 1
        if letter[i - k] == 'W':
            current_whites -= 1
        if current_whites < min_changes:
            min_changes = current_whites          
    return min_changes

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    letter= str(input())
    num = [n, k]
    print(blackandwhite(t, num, letter))
    

        
        


