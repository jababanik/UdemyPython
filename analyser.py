from demo import quick_sort, mergesort, bubble_sort
import time
import random

def rand_list(size,max_val):
    random_list = []
    for i in range (size):
        random_list.append(random.randint(1,max_val))
    return random_list

def analyze_func(func_name, arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc-tic
    print(f"{func_name.__name__.capitalize()}\t --> Elapsed time --->:{ seconds:.5f}")


size = int(input("Enter the size of the list"))
max_val = int(input("Enter the range max val"))
run_times = int(input("How many times do you want to run?"))

for num in range(run_times):
    print (f"Run:{num+1}")
    l = rand_list(size,max_val)
    #print(l)
    analyze_func(quick_sort, l)
    analyze_func(mergesort, l)
    analyze_func(bubble_sort, l.copy())
    analyze_func(sorted, l)
    print("-" * 40)
