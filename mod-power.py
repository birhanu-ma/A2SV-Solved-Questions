# Enter your code here. Read input from STDIN. Print output to STDOUT
def MathPower(a,b,c):
    print(pow(a,b))
    print(pow(a,b,c))
    
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    MathPower(a,b,c)
