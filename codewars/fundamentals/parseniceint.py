def get_age(age):
    age = age.split()
    age_enumerated = enumerate(age)
    print(age_enumerated)

    #https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1/train/python

age = "4 years old"
print(get_age(age))