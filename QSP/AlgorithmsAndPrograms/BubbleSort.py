def BubbleSort(A):
    for i in range( len( A ) - 1):
        # print('i is', i)
        for k in range( i + 1 , len( A ) , 1 ):
            # print('i is {} k is {}'.format(i, k))
            if(A[i] > A[ k ]):
                swap( A, i, k )


def swap( A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp


A = [909,876,201,173,546,789,321]
BubbleSort(A)
print(A)
