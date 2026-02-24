from funcoes import *

data_vencimento = input('Digite da data de vencimento do produto (DD-MM-AAAA): ')

while len(data_vencimento) != 10:
    data_vencimento = input('\nEntrada inválida! Digite da data de vencimento do produto (DD-MM-AAAA): ')

if verifica_vencimento(data_vencimento):
    print('\nO produto está vencido.')
else:
    print('\nO produto não está vencido.')
