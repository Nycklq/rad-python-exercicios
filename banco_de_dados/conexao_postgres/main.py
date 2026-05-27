from conexao import ConexaoPostgres


def main():
    db = ConexaoPostgres()

    try:
        db.conectar()
        db.criar_tabela_produtos()

    except Exception as erro:
        print(f"Erro no PostgreSQL: {erro}")

    db.fechar_conexao()


if __name__ == "__main__":
    main()