from aluno import Aluno
from banco import Banco

if __name__ == "__main__":
    
    def menu():
        db = Banco()
        db.conectar()
        db.criar_tabela_aluno()
        
        try:  
            aluno1 = Aluno("Arrascaeta", 10.00)
            aluno2 = Aluno("Gabriel B.", 9.00)
            aluno3 = Aluno("Bruno Henrique", 8.00)
            db.criar_aluno(aluno1)
            db.criar_aluno(aluno2)
            db.criar_aluno(aluno3)
            print("Dados inseridos com sucesso")
            
            db.fechar_conexao()
            print("Conexao fechada com sucesso")
            
        except Exception as e:
            print(f"Falha ao criar alunos: {e}")
           
if __name__ == "__main__":
    menu()