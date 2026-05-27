import os

ARQUIVO = "../../manipulacao_de_arquivos/poema/poema.txt"

def abrir_arquivo():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
                resposta = arquivo.readlines()

            print("Arquivo aberto com sucesso!")
            print(resposta)

        except FileNotFoundError:
            print("Erro: arquivo não encontrado.")

        except PermissionError:
            print("Erro: você não tem permissão para abrir esse arquivo.")

        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")
    else:
        print("Erro: caminho do arquivo não existe.")

if __name__ == "__main__":
    abrir_arquivo()