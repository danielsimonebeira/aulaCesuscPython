#10. Faça um programa que lê as duas notas parciais obtidas por um
#    aluno numa disciplina ao longo de um semestre, e calcule a sua média. A
#    atribuição de conceitos obedece à tabela abaixo:
#    Média de Aproveitamento Conceito
#    Entre 9.0 e 10.0   A
#    Entre 7.5 e 9.0    B
#    Entre 6.0 e 7.5    C
#    Entre 4.0 e 6.0    D
#    Entre 4.0 e zero   E
#    O algoritmo deve mostrar na tela as notas, a média, o conceito
#    correspondente e a mensagem
#    “APROVADO” se o conceito for A, B ou C ou
#    “REPROVADO” se o conceito for D ou E.

nome_aluno = input("Nome do Aluno: ")

nota_aluno_a = float(input("Nota (1 a 10) Avaliação 1: "))
nota_aluno_b = float(input("Nota (1 a 10) Avaliação 2: "))
nota_aluno_c = float(input("Nota (1 a 10) Avaliação 3: "))

qtde_avaliacao = 3
nota_final_a = 10.0
nota_final_b = 9.0
nota_final_c = 7.5
nota_final_d = 6.0
nota_final_e = 4.0

media_aluno = (nota_aluno_a + nota_aluno_b + nota_aluno_c) / qtde_avaliacao


if (media_aluno > nota_final_b or qtde_avaliacao == nota_final_a):
    print("Aluno {}, média {:.2f} Aprovado com a nota final A.".format(nome_aluno,media_aluno))
elif(media_aluno > nota_final_c or qtde_avaliacao <= nota_final_b):
    print("Aluno {}, média {:.2f}  Aprovado com a nota final B.".format(nome_aluno,media_aluno))
elif(media_aluno > nota_final_d or qtde_avaliacao <= nota_final_c):
    print("Aluno {}, média {:.2f}  Aprovado com a nota final C.".format(nome_aluno,media_aluno))
elif(media_aluno > nota_final_e or qtde_avaliacao <= nota_final_d):
    print("Aluno {}, média {:.2f}  Reprovado com a nota final D.".format(nome_aluno,media_aluno))
elif(media_aluno >= 0 or qtde_avaliacao <= nota_final_e):
    print("Aluno {}, média {:.2f}  Reprovado com a nota final E.".format(nome_aluno,media_aluno))
else:
    print("Resultadp Inválido!!")
