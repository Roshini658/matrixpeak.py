def find_peak(matrix):# "find peak element in matrix" using "binary search"
    n=len(matrix)#number of rows
    m=len(matrix[0])#number of columns
    low=0#start column
    high=m-1#end column
    while low<=high:#binary search loop
        mid=(low+high)//2#middle column
        max_row=0#row index of max element in mid column
        for i in range(n):#find maximum in this column
            if matrix[i][mid]>matrix[max_row][mid]:
                max_row=i
        left=matrix[max_row][mid-1] if mid>0 else -float('inf')#left neighbor
        right=matrix[max_row][mid+1] if mid<m-1 else -float('inf')#right neighbor
        if matrix[max_row][mid]>left and matrix[max_row][mid]>right:#peak found
            return (max_row,mid)#return index
        elif left>matrix[max_row][mid]:#if left is greater
            high=mid-1#move to left half
        else:#if right is greater
            low=mid+1#move to right half
    return (-1,-1)#safety return
matrix=[
    [10,8,10,10],
    [14,13,12,11],
    [15,9,11,21],
    [16,17,19,20]
]
print(find_peak(matrix))
