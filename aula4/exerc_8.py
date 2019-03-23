# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve
#    comprar, sabendo que a decisão é sempre pelo mais barato.
preco_a = float(input("Digite o preço do produto A: R$ "))
preco_b = float(input("Digite o preço do produto B: R$ "))
preco_c = float(input("Digite o preço do produto C: R$ "))

if(preco_a < preco_b and preco_a < preco_c):
    print("\nO produro A com o valor de R$ %.2f dever ser comprado." % (preco_a))


elif(preco_b < preco_c and preco_b < preco_a):
    print("\nO produro B com o valor de R$ %.2f dever ser comprado." % (preco_b))


elif(preco_c < preco_a and preco_c < preco_b):
    print("\nO produro C com o valor de R$ %.2f dever ser comprado." % (preco_c))
