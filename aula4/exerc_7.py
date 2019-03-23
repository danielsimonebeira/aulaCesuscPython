# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.
numero_a = int(input("Digite o 1º numero: "))
numero_b = int(input("Digite o 2º numero: "))
numero_c = int(input("Digite o 3º numero: "))

if (numero_a > numero_b and numero_a > numero_c):
    if (numero_c < numero_b):
        print("=============================",
              "\n - {} é maior e {} é menor.".format(numero_a,numero_c),
              "\n=============================")

    else:
        print("=============================",
              "\n - {} é maior e {} é menor.".format(numero_a,numero_b),
              "\n=============================")

elif (numero_b > numero_a and numero_b > numero_c):
    if (numero_a < numero_c):
        print("=================================",
              "\n - {} é maior que e {} é menor.".format(numero_b,numero_a),
              "\n=================================")

    else:
        print("=================================",
              "\n - {} é maior que e {} é menor.".format(numero_b,numero_c),
              "\n=================================")

elif (numero_c > numero_a and numero_c > numero_b):
    if (numero_b < numero_a):
        print("=================================",
              "\n - {} é maior que e {} é menor.".format(numero_c,numero_b),
              "\n=================================")

    else:
        print("=================================",
              "\n - {} é maior que e {} é menor.".format(numero_c,numero_a),
              "\n=================================")
