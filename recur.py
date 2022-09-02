def sumOfNatureNumber(num):
    if num == 1:
        return 1
    
    return num + sumOfNatureNumber(num - 1)

print(sumOfNatureNumber(10))


def binarySearch(myList , left, right, x):
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if mid == x:
        return mid
    
    if x < mid:
        return binarySearch(myList , left, mid -1, x)

    return binarySearch(myList , mid+1 , right, x)

def fib(n):
    if n == 0 or n == 1:
        return n

    return fib(n-1) + fib(n -2)

print(fib(3))


def mergeSort(myList):

    mid = len(myList) // 2

    
