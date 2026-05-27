import re

def validar_senha(senha: str) -> bool:
    padrao = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&.#_-]).{8,}$"
    
    if re.match(padrao,senha):
        return True
    else:
        return False
    
if __name__ == "__main__":
    try:
        senha = input("Password: ")

        if validar_senha(senha):
            print("Senha válida")
        else:
            print("Senha invalida")
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")