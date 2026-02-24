import time

while True:
    tempo = input('Digite o tempo em segundos: ')

    if tempo.isdigit():
        tempo = int(tempo)
        break
    else:
        print('\nValor inválido.\n')
        continue

print()

while tempo >= 0:
    minutos, segundos = divmod(tempo, 60)
    timer = '{:02d}:{:02d}'.format(minutos, segundos) # d = número inteiro, 2 = dois dígitos, 0 = considera 0 a esquerda
    print(timer, end = '\r')
    time.sleep(1)
    tempo -= 1

print('\n\nTempo encerrado!')