import pandas as pd
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Entrada"

ws.append(["Data", "Categoria", "Valor"])

wb.save("desafioGIT.xlsx")

while True:
    print(f"Bem vindo a lista de chamados, selecione o que deseja:")
    n = int(input(f" 1- Adicionar gastos\n 2- Vizualizar gastos\n 0- Encerrar\n"))
