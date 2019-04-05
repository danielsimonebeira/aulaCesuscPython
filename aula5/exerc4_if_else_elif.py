#4. Faça um programa que pede dois inteiros e armazene em duas
#   variáveis. Em seguida, troque o valor das variáveis e exiba na tela

numero_a = int(input("1º numero: "))
numero_b = int(input("2º numero: "))
print("1ª variavel digitada: ",numero_a)
print("2ª variavel digitada: ",numero_b)

aux  = numero_b
numero_b = numero_a
numero_a = aux

print("\n1ª variavel: ",numero_a)
print("2ª variavel: ",numero_b)


