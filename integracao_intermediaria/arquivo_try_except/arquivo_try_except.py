import csv

ARQUIVO_VENDAS = "vendas.csv"
ARQUIVO_ERROS = "erros.log"


def criar_arquivo():
    with open(ARQUIVO_VENDAS, "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["produto", "quantidade", "preco"])
        escritor.writerow(["Mouse", "2", "50.00"])
        escritor.writerow(["Teclado", "1", "120.00"])
        escritor.writerow(["Monitor", "", "900.00"])
        escritor.writerow(["Headset", "3", "abc"])
        escritor.writerow(["Cadeira", "1", "750.00"])


def importar_vendas():
    total = 0

    with open(ARQUIVO_VENDAS, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha_numero, venda in enumerate(leitor, start=2):
            try:
                produto = venda["produto"]
                quantidade = int(venda["quantidade"])
                preco = float(venda["preco"])

                valor_venda = quantidade * preco
                total += valor_venda

                print(f"{produto}: R$ {valor_venda:.2f}")

            except ValueError:
                with open(ARQUIVO_ERROS, "a", encoding="utf-8") as log:
                    log.write(f"Erro na linha {linha_numero}: valor numérico inválido\n")

            except KeyError:
                with open(ARQUIVO_ERROS, "a", encoding="utf-8") as log:
                    log.write(f"Erro na linha {linha_numero}: coluna ausente\n")

    print(f"\nTotal das vendas válidas: R$ {total:.2f}")


def main():
    criar_arquivo()
    importar_vendas()


if __name__ == "__main__":
    main()