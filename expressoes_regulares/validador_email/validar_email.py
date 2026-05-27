import re

def validar_email(email) -> bool:
    padrao = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$"
    
    if re.match(padrao,email):
        return True
    else:
        return False

if __name__ == "__main__":
    
    try:
        email = input("E-mail: ")
    
        if validar_email(email):
            print("E-mail válido")
        else:
            print("E-mail inválido")
            
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")