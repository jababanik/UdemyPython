# nth element in fibonnacci series - new element is sum of 2 previous integer in the series
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

r = fib(10)
print (r)