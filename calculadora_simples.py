print('1- adição')
print('2- subtração')
print('3- multiplicação')
print('4- divisão')

x = int(input('escolha um uma operação: '))

num1 = float(input('digite o primeiro número: '))
num2 = float(input('digite o segundo número: '))

if x == 1:
    resultado = num1 + num2
elif x == 2:
    resultado = num1 - num2
elif x == 3:
    resultado = num1 * num2
elif x == 4:
    resultado = num1 / num2
else:
    print('operação inválida')


print(f' o resultado da operação é:{resultado:.2} ' )

