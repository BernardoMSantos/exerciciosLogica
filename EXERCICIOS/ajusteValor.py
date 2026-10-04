#6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.

print("[1]-Para adicionar 5% /ou [2]-Para tirar 5%")
escolha = int(input("Digite: "))
if escolha == 1:
    valor = int(input("Escreva um valor: "))
    valor = valor + (valor * 0.05)
    print(f"O valor com o acréscimo de 5%: {valor}")
if escolha == 2:
    valor = int(input("Escreva um valor: "))
    valor = valor - (valor * 0.05)
    print(f"O valor menos 5%: {valor}")
    