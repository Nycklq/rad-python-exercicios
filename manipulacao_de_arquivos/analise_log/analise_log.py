ARQUIVO_LOG = "sistema.log"

try:

    with open(ARQUIVO_LOG, "w", encoding="utf-8") as arquivo:
        arquivo.write("""INFO Sistema iniciado
WARNING Memória alta
INFO Usuário logado
ERROR Falha ao conectar no banco
WARNING Disco quase cheio
ERROR Timeout na requisição
INFO Sistema finalizado""")

    with open(ARQUIVO_LOG, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    quantidade_error = conteudo.count("ERROR")
    quantidade_warning = conteudo.count("WARNING")

    print(f"Quantidade de ERROR: {quantidade_error}")
    print(f"Quantidade de WARNING: {quantidade_warning}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{ARQUIVO_LOG}' não foi encontrado.")

except PermissionError:
    print("Erro: Sem permissão para acessar ou criar o arquivo.")

except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")