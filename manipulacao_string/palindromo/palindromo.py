import re


def verificar_palindromo(frase):
    frase_limpa = re.sub(r"[^a-zA-Z0-9]", "", frase)

    frase_limpa = frase_limpa.lower()

    if frase_limpa == frase_limpa[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        frase = input("Frase: ")

        if verificar_palindromo(frase):
            print("É um palindromo")
        else:
            print("Nao é um palindromo")

    except Exception as erro:
        print(f"Erro inesperado: {erro}")
