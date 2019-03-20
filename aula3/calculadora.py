valor1 = float(input("Primeiro Valor: "))
valor2 = float(input("Segundo Valor: "))
tipocalc = input(" +  para SOMA"
                     + "\n -  para SUBTRAÇÃO"
                     + "\n *  para MULTIPLICAÇÃO"
                     + "\n /  para DIVISÃO"
                     + "\n ** para EXPONENCIAÇÃO"
                     + "\n %  para RESTO DA DIVISÃO"
                     + "\nSeleciona uma das opções: ")

if (tipocalc == '+'):
    calculadora = valor1 + valor2
    print("\nResultado da soma: ", calculadora)

elif(tipocalc == '-'):
    calculadora = valor1 - valor2
    print("vResultado da soma: ", calculadora)

elif(tipocalc == '*'):
    calculadora = valor1 * valor2
    print("\nResultado da soma: ", calculadora)

elif(tipocalc == '/'):
    calculadora = valor1 / valor2
    print("\nResultado da soma: ", calculadora)

elif(tipocalc == '**'):
    calculadora = valor1 ** valor2
    print("\nResultado da soma: ", calculadora)

elif(tipocalc == '%'):
    calculadora = valor1 % valor2
    print("\nResultado da soma: ", calculadora)

else:
    print("\nValor inválido!")
