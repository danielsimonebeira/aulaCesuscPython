# 9.)  Faça um programa que peça a temperatura em graus  farenheit, transforme e mostre a temperatura em graus celsius. c = (5*(F-32)/9)

graus_f = float(input("Digite a temperatura em graus farenheit: "))
graus_c = (5 * (graus_f - 32) / 9)

print("O valor de %.2f farenheit, em graus Celsius é de %.2f" % (graus_f,graus_c))
