import os
import psycopg2
from dotenv import load_dotenv


CAMINHO_ENV = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(CAMINHO_ENV, encoding="utf-8")


class ConexaoPostgres:
    def __init__(self) -> None:
        self.host = os.getenv("POSTGRES_HOST", "localhost")
        self.port = os.getenv("POSTGRES_PORT", "5432")
        self.user = os.getenv("POSTGRES_USER", "postgres")
        self.password = os.getenv("POSTGRES_PASSWORD", "")
        self.dbname = os.getenv("POSTGRES_DATABASE", "estudosdb")
        self.conn = None

    def conectar(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                dbname=self.dbname
            )

            print("Conexão com PostgreSQL criada com sucesso.")

        except psycopg2.Error as erro:
            raise psycopg2.Error(f"Falha ao conectar com PostgreSQL: {erro}")

    def criar_tabela_produtos(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()

                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS produtos (
                        id SERIAL PRIMARY KEY,
                        nome VARCHAR(100),
                        preco NUMERIC
                    )
                """)

                self.conn.commit()
                cursor.close()

                print("Tabela produtos criada com sucesso.")

            except psycopg2.Error as erro:
                raise psycopg2.Error(f"Falha ao criar tabela produtos: {erro}")

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            print("Conexão fechada com sucesso.")