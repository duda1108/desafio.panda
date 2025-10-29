def funcao(n, ws, wb):

    # Adiconar gastos:
    while True:
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
            break

        # Vizualizar os gastos:
        elif n == 2:
            print("-----------------------GASTOS TOTAIS--------------------------")
            for linha in ws.iter_rows(min_row=2, values_only=True):
                data, categoria, valor = linha
                print(f"-No dia {data}, foram gastos {valor} reais em {categoria}\n")
            break

        # Encerrar codigo:
        elif n == 0:
            print(f"Encerrando...")
            return "quebra"
            break

        else:
            print("Você deve digitar um dos numeros da lista\n")

