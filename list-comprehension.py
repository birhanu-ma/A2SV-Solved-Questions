def listComprehension(x,y,z,n):
    coordinate_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+k+j != n]
    print(coordinate_list)
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    listComprehension(x,y,z,n)
