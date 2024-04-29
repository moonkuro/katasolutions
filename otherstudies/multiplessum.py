sumNumber = 0
for n in range(1,1000):
    if n % 5 == 0:
        sumNumber += n
    elif n % 3 == 0:
        sumNumber += n

print(sumNumber)