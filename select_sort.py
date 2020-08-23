# Selection sort
def selection_sort(arr):
    comparison = 0
    for i in range(len(arr)):
        comparison +=1
        for j in range(i,len(arr)):
            comparison +=1
            if (arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)
    print(comparison)

# input_list = [6,8,1,4,10,7,8,9,3,2,5] # avg case
# input_list = [10,9,8,8,7,6,5,4,3,2,1] # worst case
input_list = [1,2,3,4,5,6,7,8,8,9,10] # best case
selection_sort(input_list)
