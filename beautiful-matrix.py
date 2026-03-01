def BeautifulMatrix(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j]==1:
                step = abs(j-2)+abs(i-2)
                return step
first = list(map(int, input().split()))

second = list(map(int, input().split()))

third = list(map(int, input().split()))

fourth = list(map(int, input().split()))

fifth = list(map(int, input().split()))
matrix = [first, second, third, fourth, fifth]

print(BeautifulMatrix(matrix))


