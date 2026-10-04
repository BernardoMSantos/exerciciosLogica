#5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos salários mínimos esse usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).

salarioMinimo = 1293.20
salarioUsuario = float(input("Quando você ganha (em reais)?: "))

quantidadeSalario = salarioUsuario / salarioMinimo

if quantidadeSalario < 1:
    print(f"Você recebe menos que um salário mínimo({salarioMinimo}), algo de errado não está certo.") 
else:
    print(f"Você recebe {quantidadeSalario:.2f} salário(s) mínimos.")