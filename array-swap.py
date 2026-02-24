def parallelSorting(n, arr):
    arr_a = arr[0]
    arr_b = arr[1]
    op_type_idx = []
    for i in range(n):
        if arr_a[i]>arr_b[i]:
            arr_b[i],arr_a[i] = arr_a[i], arr_b[i]
            op_type_idx.append([3, i+1])

    for i in range(len(arr_a)-1):
        for j in range(len(arr_a)-i-1):
            if arr_a[j]>arr_a[j+1]:
                arr_a[j],arr_a[j+1] = arr_a[j+1], arr_a[j]
                op_type_idx.append([1, j+1])

            if arr_b[j]>arr_b[j+1]:
                arr_b[j],arr_b[j+1] = arr_b[j+1], arr_b[j]
                op_type_idx.append([2, j+1])  
    print(len(op_type_idx))
    for i in range(len(op_type_idx)):
         print (*op_type_idx[i])

t= int(input())

for _ in range(t):
    n = int(input())
    

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    arr_with_size = []
    arr_with_size.append(a)
    arr_with_size.append(b) 
    parallelSorting(n, arr_with_size)




