print('             CONVERSOR DE TEMPERATURA        ')
print('(1) para digitar temperatura em graus Celsius')
print('(2) para inserir a temperatura em graus fahrenheit')
print('(3) para inserir a temperatura em Kelvin')

op = int(input('digite a opção desejada: '))
x = int(input('insira a temperatura que queira converter: '))

if op == 1:
    tf = (x * 9/5)+32
    print('a temperatura em graus fahrenheit é: ', tf)
    tk = x + 273.15
    print('a temperatura em Kelvin será de ', tk)

elif op == 2:
    tc = (x * 9/5) - 32
    print('a temperatura em graus Celsius será: ', tc)
    tk = (x - 32) * 5/9 +273.15
    print('a temperatura em Kelvin será de:', tk)

elif op == 3:
    tc = x - 273.15
    print('a temperatura em graus Celsius será: ', tc)
    tf = (x-273.15) * 1.8 + 32
    print('a temperatura em fahrenheit será de ', tf)

else:
    print('operação inválida')


