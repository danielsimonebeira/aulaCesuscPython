# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = int(input("Digite um valor positivo ou negativo: "))


if (valor < 0):
    print("O valor {} é negativo.".format(valor))

else:
    print("O valor {} é positivo.".format(valor))
