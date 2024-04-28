def minimum(arr):
    minNumber = arr[0]
    for n in arr:
        if n < minNumber:
            minNumber = n
    return minNumber

def maximum(arr):
    maxNumber = arr[0]
    for n in arr:
        if n > maxNumber:
            maxNumber = n
    return maxNumber