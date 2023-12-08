#funcoes

import requests
from datetime import datetime

tam = 55

def layout(cotacao):
    print('-' * tam)
    print('COTAÇÃO MOEDA'.center(50))
    print('-' * tam)
    print(f'Cotação hoje - {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'.center(50))
    print()
    print(f'{"EURO":<40}{"R$"}{cotacao["EURBRL"]["bid"]:<10}'.replace('.', ','))
    print(f'{"DOLAR":<40}{"R$"}{cotacao["USDBRL"]["bid"]:<10}'.replace('.', ','))
    print(f'{"BITCOIN":<40}{"R$"}{"{:,.2f}".format(float(cotacao["BTCBRL"]["bid"])):<10}'.replace(',', '.').replace('.',','))
    print('-' * tam)


def cotacao_moeda():
    cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    return cotacao.json()


def converter_para_euro(cotacao, valor_converter):

    try:
        valor_euro = float(cotacao["EURBRL"]["bid"])
        valor_convertido = valor_euro * float(valor_converter)
        print(f'Valor convertido de Euro para Real: R${valor_convertido:.2f}'.replace('.', ','))
    except ValueError:
        print("Por favor, insira um valor numérico positivo válido.")


def converter_para_dolar(cotacao, valor_converter):

    try:
        valor_euro = float(cotacao["USDBRL"]["bid"])
        valor_convertido = float(valor_converter) * valor_euro
        print(f'Valor convertido de Dólar para Real: R${valor_convertido:.2f}'.replace('.', ','))
    except ValueError:
        print("Por favor, insira um valor numérico positivo válido.")


def converter_para_bitcoin(cotacao, valor_converter):

    try:
        valor_euro = float(cotacao["BTCBRL"]["bid"])
        valor_convertido = valor_euro * float(valor_converter)
        valor_convertido = float(valor_convertido)
        print(f'Valor convertido de Bitcoin para Real: R${valor_convertido:.2f}'.replace('.', ','))
    except ValueError:
        print("Por favor, insira um valor numérico positivo válido.")


def moeda_ser_convertida(cotacao_atual, valor_converter):

    if valor_converter.isnumeric():
        moeda_converter = str(input('Digite a moeda desejada (D para Dólar, E para Euro, B para Bitcoin): ')).lower()

        if moeda_converter == 'e':
                converter_para_euro(cotacao_atual, valor_converter)
                
        elif moeda_converter == 'd':
                converter_para_dolar(cotacao_atual, valor_converter)
                
        elif moeda_converter == 'b':
                converter_para_bitcoin(cotacao_atual, valor_converter)
                
        else:
            print('Moeda não reconhecida. Por favor, escolha entre Euro (E), Dólar (D) e Bitcoin (B).')
        
    else:
        print('Valor inválido.')
        
        