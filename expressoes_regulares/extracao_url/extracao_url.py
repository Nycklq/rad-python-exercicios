import re

def validar_url(texto):
    padrao = r"https?://[^\s]+"
    urls = re.findall(padrao,texto)
    return urls

if __name__ == "__main__":
    try:
        texto = """
        Acesse nosso site em https://www.exemplo.com
        Veja também http://teste.com.br/pagina
        Link inválido: www.google.com
        Outro link válido: https://github.com/usuario/projeto
        """
        urls_encontrada = validar_url(texto)
        
        if urls_encontrada:
            print("-="*10 + " URLS ENCONTRADAS " + "-="*10)
            
            for url in urls_encontrada:
                print(url)
            
        else:
            print("Nenhuma URL encontrada")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")