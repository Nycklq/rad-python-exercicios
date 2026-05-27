def contar_vogais_consoantes(texto):
    vogais = "aeiou"
    qtd_vogais = 0
    qtd_consoantes = 0

    text = texto.lower()

    for letra in text:
        if letra.isalpha():
            if letra in vogais:
                qtd_vogais += 1
            else:
                qtd_consoantes += 1

    return qtd_vogais, qtd_consoantes

if __name__ == "__main__":
    try:
        frase = input("Digite uma frase: ")

        vogais, consoantes = contar_vogais_consoantes(frase)

        print("Vogais:", vogais)
        print("Consoantes:", consoantes)
    except Exception as e:
        print(f"Erro inesperado: {e}")
