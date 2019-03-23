#10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou
#    V- Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
#    ou "Valor Inválido!", conforme o caso.
nome_aluno = input("Digite seu nome: ")
turno = input(" {}, digite o turno que você estuda: \n - M para matutino, \n - V para Vespertino  \n - N para Noturno\n".format(nome_aluno))

if (turno.lower() == 'm'):
    print("========",
          "\nBom Dia!",
          "\n========")

if (turno.lower() == 'v'):
    print("==========",
          "\nBom Tarde!",
          "\n==========")

if (turno.lower() == 'n'):
    print("=========-",
          "\nBoa Noite!",
          "\n==========")
