

# Verificador de Número Par oi Ímpar:
#Crie um programa que verifique se um número (informado pelo usuário) é par ou ímpar

#retornar uma string (texto)
#o retorno dentro de uma variável

numero = int(input('Digite um número: '))
if (numero %2) == 0:
    print(f' O {numero} é par!')
else:
    print(f' O {numero} é ímpar!')
