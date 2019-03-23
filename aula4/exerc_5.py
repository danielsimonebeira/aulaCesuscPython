# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve
#    calcular a média alcançada por aluno e apresentar:
#      o A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#      o A mensagem "Reprovado", se a média for menor do que sete;
#      o A mensagem "Aprovado com Distinção", se a média for igual a dez.
nome_aluno = input("Digite o nome do aluno: ")
nota_a = float(input("Digite a primeira nota do aluno {}: ".format(nome_aluno)))
nota_b = float(input("Digite a segunda nota do aluno {}: ".format(nome_aluno)))

media = (nota_a + nota_b) / 2

if (media >= 7 and media < 10):
    print("O aluno {} foi aprovado com a nota %.2f.".format(nome_aluno) % (media))

elif (media == 10.00):
    print("O aluno {} foi aprovado com distinção Mother Fucker!!!".format(nome_aluno))

else:
    print("O aluno {} foi reprovado com a nota %.2f.".format(nome_aluno) % (media))
