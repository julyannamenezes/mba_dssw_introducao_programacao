#variáveis
valor_produto = float(input('Digite o valor do produtp:'))
desconto = float(input('Digite o valor do desconto:'))

# Funções e Métodos

#Processamento
valor_desconto = (valor_produto * desconto) / 100
valor_final = valor_produto - valor_desconto

# Visualização
print(f'o valor do desconto é {valor_final:.2f}')

