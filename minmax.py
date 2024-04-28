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

print(minimum([5, 3, 2, 113, 21, -23, 1]))
print(maximum([5, 3, 2, 113, 21, -23, 1]))