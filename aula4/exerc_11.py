#11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
#    lhe contrataram para desenvolver o programa que calculará os reajustes.
#     o Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
#       seguinte critério, baseado no salário atual:
#     o salários até R$ 280,00 (incluindo) : aumento de 20%
#     o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#     o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#     o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
#       informe na tela:
#     o o salário antes do reajuste;
#     o percentual de aumento aplicado;
#     o o valor do aumento;
#     o o novo salário, após o aumento.
print("=== Organizações Tabajara ===")
nome_colaborador = input("Nome do colaborado: ")
salario_atual = float(input("Salario do colaborador {}: R$ ".format(nome_colaborador)))

valor_limitado_a = float(280)
valor_limitado_b = float(700)
valor_limitado_c = float(1500)

if (salario_atual <= valor_limitado_a):
    porcentagem = 20
    bonus = (salario_atual * porcentagem) / 100
    salario_atualizado = salario_atual + bonus
    print("============================================",
          "\nFuncionario        : {}".format(nome_colaborador),
          "\nSalario            : R$ %.2f" % (salario_atual),
          "\nAumento            : R$ %.2f (%d%%)" % (bonus,porcentagem),
          "\nTotal que receberá : R$ %.2f" % (salario_atualizado),
          "\n============================================")

elif (salario_atual > valor_limitado_a and salario_atual < valor_limitado_b):
    porcentagem = 15
    bonus = (salario_atual * porcentagem) / 100
    salario_atualizado = salario_atual + bonus
    print("============================================",
          "\nFuncionario        : {}".format(nome_colaborador),
          "\nSalario            : R$ %.2f" % (salario_atual),
          "\nAumento            : R$ %.2f (%d%%)" % (bonus,porcentagem),
          "\nTotal que receberá : R$ %.2f" % (salario_atualizado),
          "\n============================================")

elif (salario_atual > valor_limitado_b and salario_atual < valor_limitado_c):
    porcentagem = 10
    bonus = (salario_atual * porcentagem) / 100
    salario_atualizado = salario_atual + bonus
    print("============================================",
          "\nFuncionario        : {}".format(nome_colaborador),
          "\nSalario            : R$ %.2f" % (salario_atual),
          "\nAumento            : R$  %.2f (%d%%)" % (bonus,porcentagem),
          "\nTotal que receberá : R$ %.2f" % (salario_atualizado),
          "\n============================================")

else:
    porcentagem = 5
    bonus = (salario_atual * porcentagem) / 100
    salario_atualizado = salario_atual + bonus
    print("============================================",
          "\nFuncionario        : ",nome_colaborador,
          "\nSalario            : R$ %.2f" % (salario_atual),
          "\nAumento            : R$  %.2f (%d%%)" % (bonus,porcentagem),
          "\nTotal que receberá : R$ %.2f" % (salario_atualizado),
          "\n============================================")
