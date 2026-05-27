import json
import os

ARQUIVO_JSON = "../dump_json/produtos.json"

try:
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        
        valor_total = 0
        
        for produto in dados["produtos"]:
            preco = produto["preco"]
            estoque = produto["estoque"]
            
            valor_produto = preco * estoque
            valor_total += valor_produto
            
            print(f"{produto['nome']}: R$ {valor_produto:.2f}")
        
        print(f"\nValor total do estoque: R$ {valor_total:.2f}")
    
    else:
        print(f"Erro: O arquivo '{ARQUIVO_JSON}' não foi encontrado.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{ARQUIVO_JSON}' não foi encontrado.")

except PermissionError:
    print("Erro: Sem permissão para ler o arquivo.")

except json.JSONDecodeError:
    print("Erro: O arquivo JSON está com formato inválido.")

except KeyError:
    print("Erro: Alguma chave esperada não existe no JSON.")

except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")