m = float(input('digite o seu peso em kg: '))
h = float(input('digite a sua altura em metros: '))

imc = m / h**2
print(f'imc: {imc:.2f}')

if imc <= 18.5:
    print('você está abaixo do peso')

else:
    print ('voce esta no peso correto')