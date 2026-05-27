class Cliente:
    def __init__(self, nome: str, email: str) -> None:
        self.nome = nome
        self.email = email
    
    def __str__(self) -> str:
        return f"Nome:{self.nome}\nEmail:{self.email}"