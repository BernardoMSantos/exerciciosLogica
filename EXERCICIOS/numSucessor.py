#4 - Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor.

numero = int(input("Escreva um número para descobrir seu antecessor e sucessor: "))

antecessor = numero - 1
sucessor = numero + 1

print(f"O antecessor de {numero}: {antecessor}, e o sucessor: {sucessor}")