def feast(beast, dish):
    beast_last_first = beast[0] + beast[-1]
    dish_last_first = dish[0] + dish[-1]
    
    if beast_last_first == dish_last_first:
        return True
    else:
        return False