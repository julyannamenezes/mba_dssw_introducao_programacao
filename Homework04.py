peso = float(input('Digite o peso em kg:'))
altura = float(input('Digite a altura em m:'))

IMC = (peso / (altura * altura))

print(f'O IMC é: {IMC:.2f}.')
