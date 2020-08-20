# merge sort
def merge_sort(arr1, arr2):
    sorted_array = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_array.append(arr1[i])
            i +=1
        else:
            sorted_array.append(arr2[j])
            j +=1
    while i < len(arr1):
        sorted_array.append(arr1[i])
        i +=1
    while j < len(arr2):
        sorted_array.append(arr2[j])    
        j +=1
    return sorted_array

    
def divide_arr(arr):
    if len(arr) < 2 :
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])
        return merge_sort(l1,l2)

l = [10,6,7,2,4,9,11,5,7,8,3]
r = divide_arr(l)
print(r)