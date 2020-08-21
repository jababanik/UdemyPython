# quick sort algo selecting last element as pivot
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        smaller, equal, larger = [], [], []
        pivot = arr[-1]
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else: 
                larger.append(num)

        return quick_sort(smaller) + equal + quick_sort(larger)

l = [10,6,7,2,4,9,11,5,7,8,3]
print(quick_sort(l))