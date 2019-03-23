# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero_a = int(input("Digite o 1º numero: "))
numero_b = int(input("Digite o 2º numero: "))
numero_c = int(input("Digite o 3º numero: "))

valor = [numero_a,numero_b,numero_c]
valor.sort(reverse=True)
print("Valor digitado em ordem decrescente",valor,sep=': ')

