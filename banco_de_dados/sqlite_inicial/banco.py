import sqlite3
from sqlite3 import Error
from aluno import Aluno

class Banco:
    def __init__(self, nome_banco="escola.db") -> None:
        self.nome_banco = nome_banco
        self.conn = None
    
    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.nome_banco)
            print("Conexão criada com sucesso.")
        except sqlite3.DatabaseError as e:
            raise sqlite3.DatabaseError(f"Falha ao conectar com o banco: {e}")
    
    def criar_tabela_aluno(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS aluno(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome VARCHAR(100) NOT NULL,
                        nota FLOAT NOT NULL
                        )""")
            
                self.conn.commit()
                cursor.close()
  
            except Error as e:
                raise Error(f"Falha ao criar tabela aluno: {e}")
    
    def criar_aluno(self, aluno: Aluno):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("""INSERT INTO aluno(nome,nota)
                               VALUES
                               (?,?)""",(aluno.nome,aluno.nota))
            
                self.conn.commit()
                cursor.close()
                
            except Error as e:
                raise Error(f"Falha ao criar aluno: {e}")
    
    def listar_alunos(self) -> list:
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("""SELECT * FROM aluno""")
                
                alunos = cursor.fetchall()
                
                cursor.close()
                
                return alunos
            except Error as e:
                raise Error(f"Falha ao lista aluno: {e}")
            
        return []

    def calcular_media_notas(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()

                cursor.execute("SELECT AVG(nota) FROM aluno")

                resultado = cursor.fetchone()

                cursor.close()

                media = resultado[0]

                return media
            except Error as e:
                raise Error(f"Falha ao calcular média das notas: {e}")
    
    def fechar_conexao(self):
        if self.conn:
            try:
                self.conn.close()
                self.conn = None
            except Error as e:
                print(f"Falha ao fechar a conexão: {e}.")
    