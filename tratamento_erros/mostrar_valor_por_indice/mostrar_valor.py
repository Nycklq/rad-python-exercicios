def mostrar_valor_por_indice(lista: list):
    list = lista
    
    try:
        indice = int(input("Digite um indice: "))
        
        valor = list[indice]
        
        print(f"O valor no indice {indice} é: {valor}")
        
    except IndexError:
        print("Erro: índice fora do tamanho da lista.")

    except ValueError:
        print("Erro: você precisa digitar um número inteiro.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
        
def menu():
    lista = []
    
    while True:
        print("[1] - Inserir dados")
        print("[2] - Mostrar valor")
        print("[3] - Sair")
        
        try:
            opcao = int(input("Opçao: "))
            
            if opcao == 1:
                dados = input("Insira dados na lista: ")
                lista.append(dados)
                print("Dado inserido com sucesso")
                
            elif opcao == 2:
                if len(lista) == 0:
                    print("A lista está vazia, Insira dados primeiro")
                else:
                    mostrar_valor_por_indice(lista)
            
            elif opcao == 3:
                print("Voce saiu do programa")
                break
            
            else:
                print("Opção inválida")
                
        except ValueError:
            print("Erro: digite apenas números no menu.")

        
        
if __name__ == "__main__":
    menu()