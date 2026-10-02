#2 - Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.
print("Digite [1]-Verificar se é ímpar/par , ou [2]-Verificar se é positivo/negativo")
opcao = int(input("Escolha uma das opções: "))

if opcao == 1:
    numero = int(input("Digite para descobrir se é (+)/(-): "))
    if numero > 0:
        print("Esse número é positivo")
    else:
        print("Esse número é negativo")
elif opcao == 2:
    numero = int(input("Digite para ver se é par ou ímpar: "))
    if numero % 2 == 0:
        print("Esse número é par")
    else:
        print("Esse número é impar")
else:
    print("Porfavor escolha uma das opções")