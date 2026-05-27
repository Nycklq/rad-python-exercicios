def converter_para_float(lista: list):
    for item in lista:
        try:
            numero = float(item)
            print(f"{item} convertido com sucesso para {numero}")
        except ValueError as e:
            print(f"Erro: não foi possível converter '{item}' para float.")
        
        except TypeError:
            print(f"Erro: o item {item} não pode ser convertido para float.")

if __name__ == "__main__":
    
    lista = ["10",25,3.14,"45.7","abc",[1, 2, 3],"","100"]
    
    converter_para_float(lista)