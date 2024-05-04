def positive_sum(arr):
    soma = 0
    for n in arr:
        if n > 0:
            soma += n
    return soma