# 8.)  Faça um programa que pergunte quanto você ganha por hora e o numero de horas trabalhadas no mês. Calcule e mostre o total do seu
# salario no referido mes.

nome = input("Digite seu nome: ")
salario_hora = float(input("Digite quanto você ganha por hora: "))
hora_trabalhada = float(input("Digite quantidade de horas trabalhadas: "))

salario_bruto = salario_hora * hora_trabalhada
inss = 0.08
irrf = 7.5
salario_liquido = salario_bruto - (salario_bruto * inss) - (salario_bruto / 100 * irrf)

print("Funcionário {} recebe ao mês:".format(nome))
print("Salario bruto: R$ %.2f " % salario_bruto)
print("Salario liquido: R$ %.2f " % salario_liquido)
