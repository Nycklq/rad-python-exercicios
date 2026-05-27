import pymysql
from conexao import Conexao


def main():
    db = Conexao()

    try:
        db.criar_conexao()

        versao = db.verificar_versao()

        if versao:
            print(f"Versão do servidor MySQL: {versao}")
        else:
            print("Não foi possível verificar a versão.")

    except pymysql.MySQLError as erro:
        print(f"Erro no MySQL: {erro}")

    except Exception as erro:
        print(f"Erro inesperado: {erro}")

    finally:
        db.fechar_conexao()


if __name__ == "__main__":
    main()