class Aluno:
    def __init__(self, nome: str, nota: float) -> None:
        self.nome = nome
        self.nota = nota
    
    def __str__(self) -> str:
        return f"Nome:{self.nome}\nNota:{self.nota}"