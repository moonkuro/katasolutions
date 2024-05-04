def rental_car_cost(d):
    daysUsed = d * 40
    cost = 0 
    
    if d < 3:
        cost = daysUsed
    elif d >= 7:
        cost = daysUsed - 50
    elif d >= 3: 
        cost = daysUsed - 20
    return cost
