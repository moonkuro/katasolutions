def bmi(weight, height):
    altura = height * height 
    imc = weight / altura 

    if imc <= 18.5:
        return "Underweight"
    if imc <= 25:
      return "Normal"
    if imc <= 30:
        return "Overweight"
    if imc > 30:
        return "Obese"


height = 1.20
weight = 40
print(bmi(weight, height))