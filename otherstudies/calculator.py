user_choice = "s"
while user_choice == "s":
    print("Esta é uma calculadora simples de quatro operações.")
    valor_1 = input("Para começarmos, digite um valor: \n")
    valor_2 = input("Você inseriu o valor " + valor_1 + ". Insira outro valor: \n")
    operation = input("Você inseriou o valor " + valor_2 + ". Insira o tipo de operação: \n")

    print("Você inseriu a seguinte operação: " + valor_1 + " " + operation + " " + valor_2)
    if operation == "+":
        print("Este é o resultado da sua operação:")
        print(int(valor_1) + int(valor_2))

    elif operation == "-":
        print("Este é o resultado da sua operação:")
        print(int(valor_1) - int(valor_2))

    elif operation == "/":
        print("Este é o resultado da sua operação:")
        print(int(valor_1) / int(valor_2))

    elif operation == "*":
        print("Este é o resultado da sua operação:")
        print(int(valor_1) * int(valor_2))
    
    user_choice = input("Deseja recomeçar o programa? (S ou N) \n")
    user_choice = user_choice.lower()
    
    if user_choice == "n":
        break