import random

print('Sejam bem-vindo ao jogo de Pedra, Papel ou Tesoura!')

pontuacao_usuario = 0
pontuacao_computador = 0
opcoes = ['r', 'p', 't']

while True:
    escolha_usuario = input('Faça sua escolha: (R) Pedra, (P) Papel, (T) Tesoura ou (S) Sair ').lower()

    if escolha_usuario == 's':
        break
    elif escolha_usuario != 'r' and escolha_usuario != 'p' and escolha_usuario != 't':
        print('\nOpção inválida!\n')
        continue

    escolha_computador = random.randint(0, 2)

    if opcoes[escolha_computador] == 'r':
        print('\nO computador escolheu Pedra.')
    elif opcoes[escolha_computador] == 'p':
        print('\nO computador escolheu Papel.')
    else:
        print('\nO computador escolheu Tesoura.')

    if escolha_usuario == opcoes[escolha_computador]:
        print('\nEmpate!')
    elif (escolha_usuario == 'r' and opcoes[escolha_computador] == 't') or \
         (escolha_usuario == 'p' and opcoes[escolha_computador] == 'r') or \
         (escolha_usuario == 't' and opcoes[escolha_computador] == 'p'):
        print('\nParabéns! Você ganhou!')
        pontuacao_usuario += 1
    else:
        print('\nVocê perdeu!')
        pontuacao_computador += 1

    usuario_rejogar = input('\nDeseja jogar novamente? (S/N) ').lower()

    while usuario_rejogar != 's' and usuario_rejogar != 'n':
        usuario_rejogar = input('\nOpção inválida! Digite (S) para Sim ou (N) para Não. ').lower()

    if usuario_rejogar == 's':
        print('')
        continue
    else:
        break

print(f'\nSua pontuação: {pontuacao_usuario} | Pontuação do computador: {pontuacao_computador} \n\nObrigada por jogar!')
