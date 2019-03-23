# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
#F
#- Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite F ou M: ")

if (sexo == 'f' or 'F'):
    print(" {} - Feminino".format(sexo))

elif (sexo == 'm' or 'M'):
    print(" {} - Masculino".format(sexo))

else:
    print("Valor inválido !!!")
