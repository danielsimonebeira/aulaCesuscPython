#1. Faça um Programa que peça dois números e imprima o maior deles.

numero_a = int(input("Digite o primeiro numero: "))
numero_b = int(input("Digite o segundo numero: "))

if (numero_a > numero_b):
    print("O maior numero é",numero_a,sep=": ")

else:
    print("O maior numero é",numero_b,sep=": ")
