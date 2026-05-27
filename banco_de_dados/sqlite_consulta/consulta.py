import sys
import os

sys.path.append(os.path.abspath("../sqlite_inicial"))

from banco import Banco


def mostrar_media():
    db = Banco("../sqlite_inicial/escola.db")

    db.conectar()
    db.criar_tabela_aluno()

    media = db.calcular_media_notas()

    if media is None:
        print("Nenhuma média cadastrada.")
    else:
        print(f"Média das notas: {media:.2f}")

    db.fechar_conexao()


if __name__ == "__main__":
    mostrar_media()