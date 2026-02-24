import sys
input = sys.stdin.readline
def polycap(n, contest):
    contest.sort()
    day = 1
    for num_problem in contest:
        if num_problem>=day:
             day += 1
        else:
            continue
    return day-1    
n = int(input())
contest = list(map(int, input().split()))
print(polycap(n, contest))
