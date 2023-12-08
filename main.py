#funcao main
from funcoes import *

if __name__ == "__main__":
    cotacao_atual = cotacao_moeda()
    layout(cotacao_atual)
    valor_converter = input('Valor a ser convertido: ')
    moeda_ser_convertida(cotacao_atual, valor_converter)