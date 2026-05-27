import pymysql
from conexao import Conexao
from cliente import Cliente


def main():
    db = Conexao()

    try:
        db.criar_conexao()
        db.criar_tabela_cliente()

        cliente = Cliente("Nicollas", "nicollas@email.com")

        db.criar_cliente(cliente)

        print("Cliente inserido com sucesso.")

        db.atualizar_cliente(
            email="nicollas@email.com",
            nome="Nicollas Nascimento"
        )

    except pymysql.Error as erro:
        print(f"Erro no MySQL: {erro}")

    except Exception as erro:
        print(f"Erro inesperado: {erro}")

    finally:
        db.fechar_conexao()


if __name__ == "__main__":
    main()