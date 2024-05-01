def find_needle(haystack):
    for i, n in enumerate(haystack):
        if n == "needle" or "NEEDLE" or "Needle":
            return f"found the needle in {n}"

haystack = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]
print(find_needle(haystack))