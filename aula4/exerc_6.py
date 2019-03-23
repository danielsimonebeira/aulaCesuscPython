# 6. Faça um Programa que leia três números e mostre o maior deles.
numero_a = int(input("Digite o 1º numero: "))
numero_b = int(input("Digite o 2º numero: "))
numero_c = int(input("Digite o 2º numero: "))

if (numero_a > numero_b and numero_a > numero_c):
    print("{} é maior que {} e {}.".format(numero_a,numero_b,numero_c))

elif (numero_b > numero_a and numero_b > numero_c):
    print("{} é maior que {} e {}.".format(numero_b,numero_a,numero_c))

elif (numero_c > numero_a and numero_c > numero_b):
    print("{} é maior que {} e {}.".format(numero_c,numero_a,numero_b))
