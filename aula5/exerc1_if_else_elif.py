#1. Faça um programa que pede duas notas de um aluno. Em seguida
#   ele deve calcular a média do aluno e dar o seguinte resultado:
#   A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#   A mensagem "Reprovado", se a média for menor do que sete;
#   A mensagem "Aprovado com Distinção", se a média for igual a dez.

aluno  = input("Nome do aluno: ")
nota_a = float(input("1º nota do aluno: "))
nota_b = float(input("2º nota do aluno: "))

nota_reprovado = 7
nota_aprovado_distincao = 10
media = (nota_a + nota_b) / 2

if (media == nota_aprovado_distincao):
    print("O aluno %s, tirou nota %.2f e foi aprovado com distinção. " % (aluno,media))
elif(media > nota_reprovado and media < nota_aprovado_distincao):
    print("O aluno %s, tirou nota %.2f e foi aprovado. " % (aluno,media))
elif(media <= nota_reprovado):
    print("O aluno %s, tirou nota %.2f e foi reprovado. " % (aluno,media))
else:
    print("\nValor inválido. Digite nota com numeros entre 1 a 10")
