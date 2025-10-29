import pandas as pd
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Controle de gastos"

ws.append(["Data", "Categoria", "Valor"])

wb.save("desafioGIT.xlsx")

while True:
    print("\n================= MENU PRINCIPAL =================")
    print(f"Bem vindo a lista de chamados, selecione o que deseja:")
    try:
        n = int(input(f" 1- Adicionar gastos\n 2- Vizualizar gastos\n 0- Encerrar\n"))

        #Adiconar gastos:
        if n == 1:
            print("-----------------------------------------------------------------------")
            data = input("Informe a data do consumo (ex: 12/10): ")
            while True:
                categoria = input("Informe a categoria do produto (Alimentação, Lazer, ...): ")
                if categoria == "":
                    print("Você deve digitar uma categoria! Tente novamente.")
                    continue
                break
            while True:
                try:
                    valor = float(input("Informe o valor do produto: "))
                    if valor <= 0:
                        print("O valor deve ser positivo! Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Valor inválido! Digite apenas números.")
            print("--------------------------GASTO ADICIONADO!---------------------------\n")
            ws.append([data, categoria, valor])
            wb.save("desafioGIT.xlsx")
            continue

        #Vizualizar os gastos:
        if n == 2:
            print("-----------------------GASTOS TOTAIS--------------------------")
            for linha in ws.iter_rows(min_row=2, values_only=True):
                data, categoria, valor = linha
                print(f"-No dia {data}, foram gastos {valor} reais em {categoria}\n")
            continue

        #Encerrar codigo:
        if n == 0:
            print(f"encerrando...")
            break

        else:
            print("Você deve digitar um dos numeros da lista\n")
            continue
    except ValueError:
        print("voce deve digitar um número..")
