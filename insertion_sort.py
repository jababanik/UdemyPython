# insertion sort
def inser_sort(arr):
    l = len(arr)
    for i in range(1,l):
        for j in range (0,i):
            if (arr[j] > arr[i]):
                arr[i], arr[j] = arr[j], arr[i]
        print(arr)


input_list = [6,1,8,4,10]
inser_sort(input_list)