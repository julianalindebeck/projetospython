import json
import random
import os

base = os.path.dirname(__file__)
caminho = os.path.join(base, 'respostas.json')
arq = open(caminho, encoding = 'utf8')

with open(caminho, encoding="utf8") as arq:
    palavras = json.load(arq)

"""
    base = pasta atual
    os.path.dirname() = pega a pasta atual
    __file__ = caminho do arquivo termoo.py

    caminho = caminho completo até "respostas.json"
    os.path.join(1, 2) = junta os caminhos 1 e 2

    with open(caminho) as arq = abre e fecha o arquivo automaticamente
"""

escolha = random.choice(list(palavras.keys()))

print("Seja bem-vindo ao jogo de adivinhação da cultura pop!")

tentativas = 5
vitoria = False

while tentativas > 0 and vitoria is not True:
    print(f'\nDica: {palavras[escolha]} | Tentativas: {tentativas}')
    resposta_usuario = input('\nDigite a data (DDMMAAAA): ')
    
    if len(resposta_usuario) != 8:
        print('\nResposta inválida! A resposta deve ter 8 dígitos.')
        continue

    if resposta_usuario.isdigit():
        verificacao = []
        pontuacao = 0

        for i in range(8):
            if resposta_usuario[i] == escolha[i]:
                verificacao.append('✅')
                pontuacao += 1
            else:
                verificacao.append('❌')

        print(f'\nResposta: {' | '.join(resposta_usuario)}')
        print(f'Verificação: {' | '.join(verificacao)}')

        if pontuacao == 8:
            vitoria = True
    
    else:
        print('\nResposta inválida! A resposta deve ser uma data.')
        continue

    tentativas -= 1

if vitoria:
    print('\nParabéns! Você ganhou o jogo!')
else:
    print(f'\nVocê perdeu! Resposta correta: {escolha}')
