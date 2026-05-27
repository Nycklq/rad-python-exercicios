def inverter_case(text):    
    if text == text.upper():
        return text.lower()
    else:
        return text.upper()

if __name__ == "__main__":
    try:
        text = input("Texto: ")
        texto_invertido = inverter_case(text)
        print(texto_invertido)
    
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        