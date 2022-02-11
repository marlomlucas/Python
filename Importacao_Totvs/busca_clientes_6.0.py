from lista_clientes import clientes
from tkinter import *
from pandastable import Table
import pandas

window = Tk()
window.geometry('1050x450')  # Largura x Comprimento
window.title("Importação Clientes")

local_arquivo = "D:\import_clientes.txt"

r_import = 0  # Contador registros a importar


def busca_cli():
    arquivo = open(local_arquivo, 'a', encoding="utf-8")  # Abre/Cria Arquivo
    r_find = 0  # Registros encontrados em cada busca

    global r_import, conteudo, conteudo2, cliente_achado  # Indica Variaveis globais

    cli_find = cli_find_campo.get().strip()  # Pega Valor informado

    for c1 in "./-":
        cli_find = cli_find.replace(c1, "")  # Remove pontos e traços (CNPJ/CPF)

    find = False
    for c2 in range(0, len(clientes)):
        if clientes[c2].lower().find(cli_find.lower()) != -1:  # Gambiarra ???
            cliente_achado = clientes[c2]  # ?? fiquei sem ideias para nomes de var.
            arquivo.write(cliente_achado + "\n")  # Grava no arquivo
            add_linha_tab()
            find = True
            r_find += 1
    if find:
        conteudo2.config(text=f"Registros localizados = {r_find}", fg="green")
    else:
        conteudo2.config(text="**Cliente Não localizado**", fg="red")
    r_import += r_find  # Acumula quantidade a importar
    cli_find_campo.delete(0, 'end')  # Limpa campo Entry "input"
    arquivo.close()  # Fecha arquivo
    conteudo.config(text=f"{r_import} Registros a importar")


def limpa_arquivo():
    open(local_arquivo, 'w', encoding="utf-8").close()  # Abre e Fecha para limpar o arquivo. "w"
    global r_import, conteudo, conteudo2, data_frame, frame, data, linhas  # Indica Variaveis globais
    r_import = 0
    conteudo.config(text="Arquivo limpo.")
    conteudo2.config(text="")
    botao_limpa.config(bg="green")

    try:
        data_frame = data_frame.iloc[0:0]
        data.clear()
        linhas = 0
        tabela = Table(frame, dataframe=data_frame)
        tabela.show()
    except:
        pass


colunas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
           "V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AL", "AM", "AN",
           "AO"]  # Valor para as colunas tabela, conf tamanho layout importação.
data = {"A": [""]}  # Cria a estrutura inicial
linhas = 0  # Variavel para verificação.


def add_linha_tab():
    global cliente_achado, linhas

    cliente_achado_split = cliente_achado.split(";")
    if linhas == 0:
        for c3 in range(0, len(cliente_achado_split)):
            data[colunas[c3]] = [cliente_achado_split[c3]]
    else:
        for c4 in range(0, len(cliente_achado_split)):
            data[colunas[c4]].append(cliente_achado_split[c4])
    linhas += 1
    create_freme()


def create_freme():
    global data_frame, frame

    data_frame = pandas.DataFrame(data=data)
    frame = Frame(window)
    tabela = Table(frame, dataframe=data_frame)
    frame.grid(column=5, row=4, padx=0, pady=0)
    tabela.show()


create_freme()

cli_find_campo = Entry(window, width=50)
cli_find_campo.grid(column=0, row=0, padx=1, pady=1)


def valida_input():
    valor_pesquisa = cli_find_campo.get()
    if valor_pesquisa == "" or len(valor_pesquisa) < 6:
        botao_find.config(bg="red")
        conteudo2.config(text="Valor pesquisa invalido.")
    else:
        busca_cli()
        botao_find.config(bg="green")


conteudo = Label(window, text="")
conteudo.grid(column=0, row=3, padx=1, pady=1)

conteudo2 = Label(window, text="")
conteudo2.grid(column=0, row=2, padx=1, pady=1)

botao_find = Button(window, text="Buscar",  bg="green", fg="black", command=valida_input)
botao_find.grid(column=0, row=1, padx=1, pady=1)

botao_limpa = Button(window, text="Limpa lista",  bg="green", fg="black", command=limpa_arquivo)
botao_limpa.grid(column=1, row=1, padx=1, pady=1)

count_linhas = 0

try:
    count_linhas = sum(1 for line in open(local_arquivo))
except:
    arquivo = open(local_arquivo, 'a', encoding="utf-8")

if count_linhas > 0:
    botao_limpa.config(bg="red")
    conteudo = Label(window, text=f"Linhas no arquivo: {count_linhas}")
    conteudo.grid(column=1, row=3, padx=1, pady=1)

window.mainloop()
