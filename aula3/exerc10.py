# 10.)  Faça um programa que a peça a temperatura em graus celsius, transforme e mostre em graus farenheit

# 9.)  Faça um programa que peça a temperatura em graus  farenheit, transforme e mostre a temperatura em graus celsius. c = (5*(F-32)/9)

graus_c = float(input("Digite a temperatura em graus Celsius: "))
graus_f = (graus_c * 9/5) + 32

print("O valor de %.2f Celsius, em graus Farenheit é de %.2f" % (graus_c,graus_f))


