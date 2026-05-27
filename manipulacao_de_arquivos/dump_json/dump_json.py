import json 
import os

ARQUIVO_JSON = "produtos.json"

try:
    if not os.path.exists(ARQUIVO_JSON):
        produtos = {
            "produtos": [
                {
                    "id": 1,
                    "nome": "Mouse",
                    "preco": 50.00,
                    "estoque": 10
                },
                {
                    "id": 2,
                    "nome": "Teclado",
                    "preco": 120.00,
                    "estoque": 5
                },
                {
                    "id": 3,
                    "nome": "Monitor",
                    "preco": 900.00,
                    "estoque": 3
                },
                {
                    "id": 4,
                    "nome": "Headset",
                    "preco": 200.00,
                    "estoque": 8
                },
                {
                    "id": 5,
                    "nome": "Notebook",
                    "preco": 3500.00,
                    "estoque": 2
                }
            ]
        }
        
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
            json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
        
        print(f"Arquivo '{ARQUIVO_JSON}' criado com sucesso")
    else:
        print(f"O arquivo '{ARQUIVO_JSON} já existe'")
    
except PermissionError:
    print("Erro: Sem permissão para criar ou escrever no arquivo.")

except TypeError:
    print("Erro: Algum dado não pode ser convertido para JSON.")

except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")