#1 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.

valorA = int(input("Digite uma quantia: "))
valorB = int(input("Digite outra quantia: "))
valorC = int(input("Digite mais uma quantia (juro que será o último): "))

soma = valorA + valorB
if soma > valorC:
    print(f"A soma dos dois primeiros valores {soma}, é maior que o último, {valorC}")
else:
    print(f"A soma dos 2 primeiros valores {soma}, não é maior que o último, {valorC}")