ARQUIVO_ORIGINAL = "dados.txt"
ARQUIVO_NOVO = "dados_reverso.txt"

try:
    
    with open(ARQUIVO_ORIGINAL, "w", encoding="utf-8") as arquivo:
        arquivo.write("""Primeira linha
Segunda linha
Terceira linha
Quarta linha""")
        
    with open(ARQUIVO_ORIGINAL, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    linhas_invertidas = linhas[::-1]

    with open(ARQUIVO_NOVO, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(linhas_invertidas)

    print(f"Arquivo '{ARQUIVO_ORIGINAL}' criado com sucesso!")
    print(f"Arquivo '{ARQUIVO_NOVO}' criado com sucesso!")

except FileNotFoundError:
    print(f"Erro: O arquivo '{ARQUIVO_ORIGINAL}' não foi encontrado.")

except PermissionError:
    print("Erro: Sem permissão para acessar ou criar o arquivo.")

except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")