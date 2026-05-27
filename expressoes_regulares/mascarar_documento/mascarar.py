import re

def mascarar_cpfs(texto):
    padrao = r"\d{3}\.\d{3}\.\d{3}-\d{2}"
    texto_mascarado = re.sub(padrao, "***.***.***-**", texto)
    return texto_mascarado

if __name__ == "__main__":
    
    try:
        texto = """
        João tem o CPF 123.456.789-10.
        Maria tem o CPF 987.654.321-00.
        Pedro informou o documento 111.222.333-44.
        """

        resultado = mascarar_cpfs(texto)

        print(resultado)

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")