###################################################################
## ALGORITHM STARTER CODE                                        ##
## Includes: Python versions of Sort and Search functions        ##
## plus Knuth and Pratt Sequence generator functions             ##
## plus a Wrapper function to all you to use the timeit module   ##
###################################################################

import timeit
import random


## WRAPPER FUNCTION - so that you can use our sort functions as a parameter when using the timeit module
## ----------------
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped


## SEQUENCE FUNCTIONS FOR PRATT AND KNUTH
## --------------------------------------

def getKnuthSeq(n):
    k = 1
    gaps = []
    while k < n:
        gaps.append(k)
        k = 3 * k + 1
    gaps.reverse()
    return gaps


def getPrattSeq(max_size):
    gaps = []
    pow3 = 1
    while pow3 <= max_size:
        pow2 = pow3
        while pow2 <= max_size:
            gaps.append(pow2)
            pow2 = pow2 * 2
        pow3 = pow3 * 3
    gaps = sorted(gaps)
    gaps.reverse()
    return gaps


## SORT FUNCTIONS
## --------------

def bubbleSort(myList):
    for a in range(0, len(myList) - 1):
        for b in range(0, len(myList) - 1 - a):
            if myList[b] > myList[b + 1]:
                myList[b], myList[b + 1] = myList[b + 1], myList[
                    b]  # Note: Python's cool way to swap values without using a temp variable
    return (myList)


def shellSort(arr):
    length = len(arr)
    gap = (length // 2)
    while (gap > 0):
        for a in range(gap, (length)):
            temp = arr[a]
            j = a
            while (j >= gap) and (arr[j - gap] > temp):
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = (gap // 2)
    return (arr)


def insertionSort(alist):
    for i in range(1, len(alist)):
        tmp = alist[i]
        k = i
        while k > 0 and tmp < alist[k - 1]:
            alist[k] = alist[k - 1]
            k -= 1
            alist[k] = tmp
    return alist


def insertion_sort_optimized(A):
    for i in range(1, len(A)):
        curNum = A[i]
        k = 0
        for j in range(i - 1, -2, -1):
            k = j
            if A[j] > curNum:
                A[j + 1] = A[j]
            else:
                break
        A[k + 1] = curNum


def merge_sort(A):
    merge_sort2(A, 0, len(A) - 1)


def merge_sort2(A, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle + 1, last)
        merge(A, first, middle, last)


def merge(A, first, middle, last):
    L = A[first:middle + 1]
    R = A[middle + 1:last + 1]
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i = j = 0
    for k in range(first, last + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


## SEARCH FUNCTIONS
## ----------------

def linearSearch(myItem, myList):
    found = False
    position = 0
    while position < len(myList) and not found:
        if myList[position] == myItem:
            found = True
        position = position + 1
    return found


def binarySearch(myItem, myList):
    # myList.sort() - list must be sorted
    found = False
    bottom = 0
    top = len(myList) - 1
    while bottom <= top and not found:
        middle = (bottom + top) // 2
        if myList[middle] == myItem:
            found = True
        elif myList[middle] < myItem:
            bottom = middle + 1
        else:
            top = middle - 1
    return found


## TESTING PROCESS
## ---------------

# add a function to build a list of n random numbers
myList = [3, 10, 2, 9, 5]
wrapped = wrapper(bubbleSort, myList)
print(timeit.timeit(wrapped, number=1))

print(myList)