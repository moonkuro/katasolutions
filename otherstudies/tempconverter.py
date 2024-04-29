def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) / 1.8
    return celsius


def celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 1.8) + 32
    return fahrenheit

temp = 100
print(fahrenheit_to_celsius(temp))
print(celsius_to_fahrenheit(temp))