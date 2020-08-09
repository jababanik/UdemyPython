# Bubble sort
def bubble_sort(arr):
    swap_happened = True
    comparisons = 0
    while (swap_happened):
        swap_happened = False
        comparisons +=1
    #for j in range(len(arr)-1):
        for i in range(len(arr)-1):
            comparisons +=1
            if (arr[i] > arr[i+1]):
                swap_happened = True
                arr[i], arr[i+1] = arr[i+1], arr[i]
        
    print(comparisons)
    return arr

input_list = [6,8,1,4,10,7,8,9,3,2,5] # avg case
# input_list = [10,9,8,8,7,6,5,4,3,2,1] # worst case
# input_list = [1,2,3,4,5,6,7,8,8,9,10] # best case
sorted_list = bubble_sort(input_list)
print(sorted_list)