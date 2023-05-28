salario_bruto = float(input('+salario bruto: '))

ir = salario_bruto * 11 / 100
print(f'- IR (11%): {ir}')

inss = salario_bruto * 8 / 100
print(f'- INSS( 8%): {inss}')

sindicato = salario_bruto * 5 / 100
print(f'- Sindicato (5%): {sindicato}')

impostos = ir + inss + sindicato

salario_liquido = salario_bruto - impostos

print(f'= Salário Líquido: {salario_liquido:.2f}')
