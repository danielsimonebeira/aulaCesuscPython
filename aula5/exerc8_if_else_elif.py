#8. Faça um programa para o cálculo de uma folha de pagamento,sabendo que os descontos são do Imposto de Renda, que depende do
#   salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS
#   corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa
#   que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
#  descontos. O programa deverá pedir ao usuário o valor da sua hora e a
#  quantidade de horas trabalhadas no mês.
#   Desconto do IR:
#   Salário Bruto até 900 (inclusive) - isento
#   Salário Bruto até 1500 (inclusive) - desconto de 5% Salário Bruto até 2500
#   (inclusive) - desconto de 10%
#   Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as
#   informações, dispostas conforme o exemplo abaixo. No exemplo o valor
#  da hora é 5 e a quantidade de hora é 220.

#  Salário Bruto: (5 * 220) : R$ 1100,00
#  (-) IR (5%) : R$ 55,00
#  (-) INSS ( 10%) : R$ 110,00
#  FGTS (11%) : R$ 121,00
#  Total de descontos : R$ 165,00
#  Salário Liquido : R$ 935,00
funcionario = input("Nome do Funcionario: ")
salario_hora = float(input("Salário hora: R$ "))
hora_trabalhada = float(input("Total de horas trabalhadas no mês: "))

valor_inss = 0.10
valor_fgts = 0.11

salario_bruto =  salario_hora * hora_trabalhada
desconto_inss = salario_bruto * valor_inss
acrescimo_fgts = salario_bruto * valor_fgts

isento = 900
valor_medio = 1500
valor_alto = 2500

if (salario_bruto <= isento):
    total_desconto = desconto_inss
    sal_liquido = (salario_bruto - desconto_inss)
    print("\nFuncionario:",funcionario,
          "\nIR: Isento" +
          "\nINSS: R${:.2f} \nFGTS: R${:.2f} \nTotal de descontos: R${:.2f} \nSalario Liquido: R${:.2f}".format(desconto_inss,acrescimo_fgts,total_desconto,sal_liquido))

elif (salario_bruto > isento and salario_bruto <= valor_medio):
    valor_ir = 0.05
    desconto_ir = (salario_bruto * valor_ir)
    total_desconto = desconto_inss + desconto_ir
    sal_liquido = salario_bruto - total_desconto
    print("\nFuncionario:",funcionario,
          "\nIR (5% de desconto): R$ {:.2f} \nINSS: R${:.2f} \nFGTS: R${:.2f} \nTotal de descontos: R${:.2f} \nSalario Liquido: R${:.2f}".format(desconto_ir,desconto_inss,acrescimo_fgts,total_desconto,sal_liquido))

elif (salario_bruto > valor_medio and salario_bruto <= valor_alto):
    valor_ir = 0.10
    desconto_ir = (salario_bruto * valor_ir)
    total_desconto = desconto_ir + desconto_ir
    sal_liquido = salario_bruto - total_desconto
    print("\nFuncionario:",funcionario,
          "\nIR (10% de desconto): R$ {:.2f} \nINSS: R${:.2f} \nFGTS: R${:.2f} \nTotal de descontos: R${:.2f} \nSalario Liquido: R${:.2f}".format(desconto_ir,desconto_inss,acrescimo_fgts,total_desconto,sal_liquido))

elif (salario_bruto > valor_alto):
    valor_ir = 0.20
    desconto_ir = (salario_bruto * valor_ir)
    total_desconto = desconto_ir + desconto_ir
    sal_liquido = salario_bruto - total_desconto
    print("\nFuncionario:",funcionario,
          "\nIR (20% de desconto): R$ {:.2f} \nINSS: R${:.2f} \nFGTS: R${:.2f} \nTotal de descontos: R${:.2f} \nSalario Liquido: R${:.2f}".format(desconto_ir,desconto_inss,acrescimo_fgts,total_desconto,sal_liquido))
