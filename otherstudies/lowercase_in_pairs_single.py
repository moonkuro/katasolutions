import string
alphabet = string.ascii_lowercase

for first_letter in alphabet:
    for second_letter in alphabet:
        if first_letter != second_letter:
            print(first_letter + second_letter)
