peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)
imc = round(imc, 2)
print('Seu IMC é: ' + str(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso normal')
elif imc < 30:
    print('Sobre peso')
elif imc < 35:
    print('Obesidade 1')
elif imc < 40:
    print('Obesidade 2')
else:
    print('Obesidade mórbida')
    
