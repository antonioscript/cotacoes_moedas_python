import requests
from tkinter import * 


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto


#pegar_cotacoes()




#Código

janela = Tk()
janela.title("Cotação Atual das Moedas")


texto_orientacao = Label(janela, text="Clique no Botão para ver as cotações das Moedas")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

#Botão
botao = Button(janela, text="Buscar Cotações", command = pegar_cotacoes) #Sem Parêntese 
botao.grid(column=0, row=1,padx=10, pady=10)

#Texto das Cotações
texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()






