#3.Faça um Programa que leia três números inteiros, em seguida
#  mostre o maior e o menor deles.
numero_a = int(input("1º numero: "))
numero_b = int(input("2º numero: "))
numero_c = int(input("3º numero: "))

if (numero_a > numero_b and numero_c < numero_b ):
    print("O maior numero é %d e o menor é %d" % (numero_a,numero_c))
elif(numero_a > numero_c and numero_b < numero_c):
    print("O maior numero é %d e o menor é %d" % (numero_a,numero_b))

elif(numero_b > numero_a and numero_c < numero_a):
    print("O maior numero é %d e o menor é %d" % (numero_b,numero_c))
elif(numero_b > numero_c and numero_a < numero_c):
    print("O maior numero é %d e o menor é %d" % (numero_b,numero_a))

elif(numero_c > numero_a and numero_b < numero_a):
    print("O maior numero é %d e o menor é %d" % (numero_c,numero_b))
elif(numero_c > numero_b and numero_a < numero_b):
    print("O maior numero é %d e o menor é %d" % (numero_c,numero_a))

elif(numero_a == numero_b and numero_c < numero_b):
    print("Os numeros %d , %d são iguais e %d é menor." % (numero_a,numero_b,numero_c))
elif(numero_a == numero_c and numero_b < numero_c):
    print("Os numeros %d, %d são iguais e %d é menor." % (numero_a,numero_c,numero_b))
elif(numero_b == numero_c and numero_a < numero_c):
    print("Os numeros %d, %d são iguais e %d é menor." % (numero_b,numero_c,numero_b))

elif(numero_a == numero_b and numero_c > numero_b):
    print("Os numeros %d, %d são iguais e %d é maior." % (numero_a,numero_b,numero_c))
elif(numero_a == numero_c and numero_b > numero_c):
    print("Os numeros %d, %d são iguais e %d é maior." % (numero_a,numero_c,numero_b))
elif(numero_b == numero_c and numero_a > numero_c):
    print("Os numeros %d, %d são iguais e %d é maior." % (numero_b,numero_c,numero_a))

elif(numero_b == numero_a):
    print("%d, %d e %d são numeros iguais"%(numero_a,numero_b,numero_c))
