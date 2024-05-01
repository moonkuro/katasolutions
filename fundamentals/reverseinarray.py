def digitize(n):
    n_reverse = str(n)
    n_reverse = n_reverse[::-1]
    list = []
    for r in n_reverse:
        list.append(int(r))
    return list
