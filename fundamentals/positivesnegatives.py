def count_positives_sum_negatives(arr):
    sum(1 for x in arr if x > 0)
    sum(x for x in arr if x < 0)

arr = [2, 5, 7]
print(count_positives_sum_negatives(arr))