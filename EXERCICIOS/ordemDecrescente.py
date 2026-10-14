#8 - Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite mais um número: "))

if num1 > num2 and num1 > num3:
    # num1 é o primeiro
    if num2 > num3:
        # num2 é o segundo
        ordem = f"{num1}, {num2}, {num3}"
    else:
        # num3 é o segundo
        ordem = f"{num1}, {num3}, {num2}"

elif num2 > num1 and num2 > num3:
    # num2 é o primeiro
    if num1 > num3:
        # num1 é o segundo
        ordem = f"{num2}, {num1}, {num3}"
    else:
        # num3 é o segundo
        ordem = f"{num2}, {num3}, {num1}"

elif num3 > num1 and num3 > num2:
    # num3 é o primeiro
    if num1 > num2:
        # num1 é o segundo
        ordem = f"{num3}, {num1}, {num2}"
    else:
        # num3 é o segundo
        ordem = f"{num3}, {num2}, {num1}"

else:
    if num1 == num2 or num1 == num3:
    elif num2 == num1 or num2 == num3:
    elif num3 == num1 or num3 == num2:


print(f"Essa é a ordem decrescente: {ordem}")