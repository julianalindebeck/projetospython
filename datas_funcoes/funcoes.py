from datetime import datetime

def data_atual():
    return datetime.now()

def verifica_data(data):
    try:
        return datetime.strptime(data, '%d-%m-%Y')
    except:
        raise Exception('Entrada inválida. Formato necessário: DD-MM-AAAA.')

def verifica_vencimento(data_vencimento):
    data_formatada = verifica_data(data_vencimento)

    if data_atual() > data_formatada:
        return True
    else:
        return False