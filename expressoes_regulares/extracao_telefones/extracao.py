import re

try:
    texto = """
    João: (21) 98765-4321
    Maria: (11) 91234-5678
    Pedro: (31) 99876-1234
    Número inválido: 2198765-4321
    Outro inválido: (21) 8765-4321
    """

    padrao = r"\(\d{2}\) 9\d{4}-\d{4}"

    telefones = re.findall(padrao, texto)

    if telefones:
        print("Telefones encontrados:")

        for telefone in telefones:
            print(telefone)
    else:
        print("Nenhum telefone encontrado.")

except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")