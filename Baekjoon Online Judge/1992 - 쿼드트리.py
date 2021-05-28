n = int(input())

arr = []
for i in range(n):
    arr.append(input())



def mark_split(array, N):

    cnt_0 = 0
    cnt_1 = 0
    for array_ in array:
        if '0' in array_:
            cnt_0 = 1
        if '1' in array_:
            cnt_1 = 1
    if cnt_0 == 0:
        print('1', end = '')
    elif cnt_1 == 0:
        print('0', end = '')

    else:
        print('(',end = '')
        array_1 = []
        array_2 = []
        array_3 = []
        array_4 = []
        for i in range(N//2):
            array_1.append(array[i][0:N//2])
            array_2.append(array[i][N//2:N])
            array_3.append(array[i+N//2][0:N//2])
            array_4.append(array[i+N//2][N//2:N])

        mark_split(array_1, N//2)
        mark_split(array_2, N//2)
        mark_split(array_3, N//2)
        mark_split(array_4, N//2)
        print(')', end = '')

mark_split(arr, n)
