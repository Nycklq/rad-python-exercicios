import os
import pymysql
from dotenv import load_dotenv
from cliente import Cliente


CAMINHO_ENV = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(CAMINHO_ENV)


class Conexao:
    def __init__(self) -> None:
        self.host = os.getenv("MYSQL_HOST", "localhost")
        self.user = os.getenv("MYSQL_USER", "root")
        self.password = os.getenv("MYSQL_PASSWORD", "")
        self.database = os.getenv("MYSQL_DATABASE", "")
        self.conn = None

    def criar_conexao(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            print("Conexão com MySQL criada com sucesso.")

        except pymysql.MySQLError as erro:
            raise pymysql.MySQLError(f"Falha na conexão com o banco MySQL: {erro}")
    
    def criar_tabela_cliente(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS cliente(
                        id INTEGER PRIMARY KEY AUTO_INCREMENT,
                        nome VARCHAR(100) NOT NULL,
                        email VARCHAR(255) UNIQUE NOT NULL
                        )""")
            
                self.conn.commit()
                cursor.close()
  
            except pymysql.Error as e:
                raise pymysql.Error(f"Falha ao criar tabela cliente: {e}")
    
    def criar_cliente(self, cliente: Cliente):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("""INSERT INTO cliente(nome,email)
                               VALUES
                               (%s,%s)""",(cliente.nome,cliente.email))
            
                self.conn.commit()
                cursor.close()
                
            except pymysql.Error as e:
                raise pymysql.Error(f"Falha ao criar cliente: {e}")
    
    def atualizar_cliente(self, email: str, nome: str):
        if self.conn:
            try:
                cursor = self.conn.cursor()

                cursor.execute("""
                    UPDATE cliente
                    SET nome = %s
                    WHERE email = %s
                """, (nome, email))

                self.conn.commit()

                if cursor.rowcount == 0:
                    print("Nenhum cliente encontrado com esse e-mail.")
                else:
                    print("Cliente atualizado com sucesso.")
                    
                self.conn.commit()
                cursor.close()
            except pymysql.Error as e:
                raise pymysql.Error(f"Erro ao atualizar cliente: {e}")
                

    def verificar_versao(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT VERSION()")

                versao = cursor.fetchone()

                cursor.close()

                if versao:
                    return versao[0]

                return None

            except pymysql.MySQLError as erro:
                raise pymysql.MySQLError(f"Falha ao verificar versão: {erro}")

        return None

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            print("Conexão fechada com sucesso.")