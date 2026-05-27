import re

ARQUIVO_ENTRADA = "dados.txt"
ARQUIVO_SAIDA = "datas_formatadas.txt"


def criar_arquivo():
    with open(ARQUIVO_ENTRADA, "w", encoding="utf-8") as arquivo:
        arquivo.write("""Compra realizada em 10/03/2024.
Produto enviado em 2024-03-15.
Cliente retornou em 22/03/2024.
""")


def formatar_data(data):
    if "/" in data:
        dia, mes, ano = data.split("/")
        return f"{dia}-{mes}-{ano}"

    ano, mes, dia = data.split("-")
    return f"{dia}-{mes}-{ano}"


def main():
    criar_arquivo()

    with open(ARQUIVO_ENTRADA, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    padrao = r"\b\d{2}/\d{2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b"

    datas = re.findall(padrao, texto)

    with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as arquivo:
        for data in datas:
            arquivo.write(formatar_data(data) + "\n")

    print("Arquivo gerado com as datas formatadas.")


if __name__ == "__main__":
    main()