ARQUIVO = "poema.txt"

try:
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        arquivo.write("""A vida é feita de escolhas
Python ajuda a pensar
Com arquivos e códigos
Eu começo a praticar""")

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    total_linhas = len(linhas)
    total_palavras = 0

    for linha in linhas:
        palavras = linha.split()
        total_palavras += len(palavras)

    print(f"Total de linhas: {total_linhas}")
    print(f"Total de palavras: {total_palavras}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{ARQUIVO}' não foi encontrado.")

except PermissionError:
    print(f"Erro: Sem permissão para acessar o arquivo '{ARQUIVO}'.")

except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")