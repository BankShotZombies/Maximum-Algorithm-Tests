import numpy as np
import time

def max1(arr):
    curHighest = arr[0]
    for i in arr:
        if i > curHighest:
            curHighest = i
    return curHighest, str(time.perf_counter()) + " seconds"

def max2(arr):
    curHighest = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                i = j
                curHighest = arr[i]
    return curHighest, str(time.perf_counter()) + " seconds"

def max3(arr):
    return max(arr), str(time.perf_counter()) + " seconds"

def max4(arr):
    arr.sort()
    return arr[-1], str(time.perf_counter()) + " seconds"

def max5(arr):
    quick_sort(arr, 0, len(arr)-1)
    return arr[-1], str(time.perf_counter()) + " seconds"

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

a = np.random.randint(1, 10000, 10000)
print(max2(a))

'''
CONLUSION:

BASED ON THESE 5 MAXIMUM NUMBER ALGORITHMS, I HAVE CONCLUDED THAT USING 
PYTHON'S BUILT IN SORT() FUNCTION, WHICH USES TIMSORT, AND THEN GETTING THE
LAST ELEMENT IS THE FASTEST WITH 0.99 SECONDS

THE SECOND FASTEST IS THE STANDARD PROCEDURE, WHICH IS GOING THROUGH THE LIST AND
REPEATEDLY CHECKING WHICH NUMBER IS MORE, AND SETTING THE HIGHER AMOUNT TO A VARIABLE (MAX1 AND MAX3)

THE ABOVE WAS WITH 10,000 ELEMENTS

THE TIMSORT METHOD (MAX4) TOOK 67 SECONDS WITH 1,000,000,000 ELEMENTS
MAX1 TOOK 176 SECONDS WITH 1,000,000,000 ELEMENTS
MAX3 TOOK 97 SECONDS WITH 1,000,000,000 ELEMENTS
QUICKSORT (MAX5) TOOK TOO LONG, SO I STOPPED IT

THE MAX2 METHOD WAS EASILY THE LONGEST, BEING O(n^2). I DON'T THINK IT WILL EVER FINISH WITH 1,000,000,000 ELEMENTS
THE EQUATION FOR MAX2 WAS Y=3.578*10^-7 * X^2 - 1.58*10^-5 * X + 1.048 (A QUADRATIC EQUATION, BECAUSE IT'S O(n^2))
FOR FUN, I DID THE MATH AND IT WOULD TAKE 357800000000 SECONDS, OR 11345.763571791 YEARS

QUICKSORT ALOGIRTHM STRIPPED FROM: https://stackabuse.com/quicksort-in-python/
'''
