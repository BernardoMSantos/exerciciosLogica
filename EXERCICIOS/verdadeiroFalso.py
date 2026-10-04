#7 - Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO.

valorLogico1 = input("Escreva um valor lógico(True/False): ")

if valorLogico1 == "True" or valorLogico1 == "False":
    valorLogico2 = input("Escreva um outro valor lógico(True/False): ")

    if valorLogico2 == "True" or valorLogico2 == "False":

        if valorLogico1 == "True" and valorLogico2 == "True":
            print("Os valores são ambos VERDADEIROS.")
        elif valorLogico1 == "False" and valorLogico2 == "False":
            print("Os valores são ambos FALSOS.")
        else:
            print("Os valores são DIFERENTES.")
    else:
        print("Porfavor escreva um dos valores lógicos -TRUE/FALSE.")

else:
    print("Porfavor escreva um dos valores lógicos -TRUE/FALSE.")
