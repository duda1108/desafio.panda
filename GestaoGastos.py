import pandas as pd
from openpyxl import Workbook
from Funcoes import funcao

wb = Workbook()
ws = wb.active
ws.title = "Controle de gastos"

ws.append(["Data", "Categoria", "Valor"])

wb.save("desafioGIT.xlsx")

while True:
    print("\n================= MENU PRINCIPAL =================")
    print(f"Bem vindo a lista de chamados, selecione o que deseja: \n 1- Adicionar gastos\n 2- Vizualizar gastos\n 0- Encerrar")
    n = int(input(f"Escolha o que deseja:"))
    resultado = funcao(n, ws, wb)
    if resultado == "quebra":
        break
