#3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá somar os dois valores, caso contrário devera multiplicar A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado a uma variável C eimprimir seu valor na tela.

valorA = int(input("Digite um valor: "))
valorB = int(input("Digite outro valor: "))

if valorA == valorB:
    valorC = valorB + valorA
    print(f"Os valores são iguais, então a soma dos dois: {valorC}")
else:
    valorC = valorA * valorB
    print(f"Os valores são diferentes, então a multiplicação de ambos: {valorC}")