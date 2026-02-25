import random
import string

def gerador_senhas(tam_senha):
    opcoes_ascii = string.ascii_letters
    opcoes_numeros = string.digits
    opcoes_pontuacoes = string.punctuation

    opcoes = opcoes_ascii + opcoes_numeros + opcoes_pontuacoes

    senha = ""

    for i in range(0, tam_senha):
        digito = random.choice(opcoes)
        senha += digito

    return senha

escolha_usuario = input('Bem-vindo ao gerador de senhas! Digite o tamanho da senha para iniciar: ')

while escolha_usuario.isdigit() == False:
    escolha_usuario = input('\nValor inválido! Digite um número para o tamanho da senha: ')

escolha_usuario = int(escolha_usuario)
senha_usuario = gerador_senhas(escolha_usuario)

print(f'\nSenha gerada: {senha_usuario}')