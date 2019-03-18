# 1.) Converta as seguintes expressões matemáticas para que
# possam ser calculadas usando p interpretador Python
print("Soma + multiplicação",10+20*30,"\n"
      + "valor ao quadrado e divisão",4 ** 2 / 30,"\n"
      + "valor ao quadrado, soma, multplica e subtrai", (9 ** 4 + 2)  * 6 - 1, sep=' : ')

# 2.) digite a seguinte expressão no interpretador
print("\nResultado atividade 2", 10 % 3 * 10 ** 2 + 1 -10 * 4 / 2, sep=" : ")

#complete a tabela a seguir, marcando inteiro ou ponto flutuante dependendo do número apresentado
print("===============")
print("\nAtividade 3\n")

valor = [5,5.0,4.3,100,1.333]
contador = 4

for tabela in range (0,contador + 1):
      qualtipo = type(valor[tabela])
      if (qualtipo == int):
            print("Valor da linha {}".format(tabela), valor[tabela], " = Valor é INTEIRO", sep=" | ")
      elif (qualtipo == float):
            print("Valor da linha {}".format(tabela), valor[tabela], " = Valor é PONTO FLUTUANTE", sep=" | ")
      elif (tabela == contador):
            break

# Complete a tabela abaixo, respondendo True ou False.
print("===============")
print("\nAtividade 4\n")
a = 4
b = 10
c = 5.0
d = 1
f = 5
#        0,1,2,3,4
teste = [a,b,c,d,f]
print("O Resultado de {} igual a {}".format(teste[0],teste[2]),teste[0] == teste[2], sep=' : ')
print("O Resultado de {} maior a {}".format(teste[0],teste[1]),teste[0] > teste[1], sep=' : ')
print("O Resultado de {} maior a {}".format(teste[4],teste[1]),teste[4] > teste[1], sep=' : ')
#print("O Resultado de a({}) igual a c({})".format(teste[3],teste[4]),teste[3] = teste[4], sep=' : ')
print("O Resultado de {} igual a {}".format(teste[0],teste[1]),teste[0] == teste[1], sep=' : ')
print("O Resultado de {} menor a {}".format(teste[2],teste[3]),teste[2] < teste[3], sep=' : ')
print("O Resultado de {} maior a {}".format(teste[1],teste[0]),teste[1] > teste[0], sep=' : ')
print("O Resultado de {} maior e igual a {}".format(teste[4],teste[3]),teste[4] >= teste[3], sep=' : ')
print("O Resultado de {} menor e igual a {}".format(teste[2],teste[2]),teste[2] <= teste[2], sep=' : ')
print("O Resultado de {} menos e igual a {}".format(teste[2],teste[4]),teste[2] <= teste[4], sep=' : ')

# Escreva uma expressão pra determinar se uma pessoa deve ou não pagar imposto.
# Consedere que pagam imposto possoas cujo salário é maior que R$ 1.200,00

print("\n===========")
print("Atividade 5")

nome = input("Nome do funcionario(a): ")
salario_str = input("Digite seu salario: ")
salario = float(salario_str)
imposto = 1200

if (salario > imposto):
      print("Funcionário(a) {} \nSalário {} \nO salário informado é maior que {} e terá que pagar o imposto de renda.".format(nome,salario,imposto),sep=" : ")
else:
      print("Funcionário(a) {} \nSalário {} \nO salário informado é menor que {} e não terá que pagar o imposto de renda.".format(nome,salario,imposto),sep=" : ")

#Escreva uma expressão que será utilizada para decidir se um aluno foi ou não
#aprovado. Para ser aprovado todas as médias do aluno devem ser maiores que 7.
#Considere que o aluno cursa apenas 3 matérias e que a nota de cada uma está
#armazenada nas seguintes variáveis: matéria1, matéria2, matéria3.



aluno = input("\nDigite o nome do aluno: ")
nota_materia1 = int


nota_materia1 = int(input("Digite a nota de 1 a 10 da matéria 1: "))
materia1 = float(nota_materia1)

nota_materia2 = input("Digite a nota de 1 a 10 da matéria 2: ")
materia2 = float(nota_materia2)

nota_materia3 = input("Digite a nota de 1 a 10 da matéria 3: ")
materia3 = float(nota_materia3)

if (materia1 > 10 or materia2 > 10 or materia3 > 10):
      print("=============================")
      print("Uma das notas estão inválida!")
      print("=============================")
      exit()

media = (materia1 + materia2 + materia3) / 3

if (media > 7):
      print("Aluno {} foi aprovado devido a nota {}.".format(aluno,media))
else:
      print("Aluno {} não foi aprovado devido a nota {}.".format(aluno,media))

