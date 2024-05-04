def find_needle(haystack):
    for position, name in enumerate(haystack):
        if name == "needle":
            return f"found the needle at position {position}"

haystack = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]
print(find_needle(haystack))