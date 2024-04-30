def sum_array(arr):
    if arr is None or len(arr) <= 1:
        return 0
    
    else: 
        sorted_arr = sorted(arr)
        sorted_arr.remove(min(arr))
        sorted_arr.remove(max(arr))
        return sum(sorted_arr)