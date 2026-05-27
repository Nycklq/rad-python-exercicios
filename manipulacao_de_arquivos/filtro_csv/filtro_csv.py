import csv

ARQUIVO_ORIGINAL = "funcionarios.csv"
ARQUIVO_NOVO = "funcionarios_acima_5000.csv"

try:
    with open(ARQUIVO_ORIGINAL, "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        
        escritor.writerow(["Nome", "Cargo", "Salario"])
        escritor.writerow(["Ana", "Desenvolvedora", 4500])
        escritor.writerow(["Carlos", "Gerente", 7000])
        escritor.writerow(["Maria", "Analista", 5200])
        escritor.writerow(["João", "Estagiário", 1800])
        escritor.writerow(["Fernanda", "Coordenadora", 6500])
        
    funcionarios_filtrados = []

    with open(ARQUIVO_ORIGINAL, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for funcionario in leitor:
            salario = float(funcionario["Salario"])

            if salario > 5000:
                funcionarios_filtrados.append(funcionario)

    with open(ARQUIVO_NOVO, "w", encoding="utf-8", newline="") as arquivo:
        campos = ["Nome", "Cargo", "Salario"]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(funcionarios_filtrados)

    print(f"Arquivo '{ARQUIVO_ORIGINAL}' criado com sucesso!")
    print(f"Arquivo '{ARQUIVO_NOVO}' criado com sucesso!")

except FileNotFoundError:
    print(f"Erro: O arquivo '{ARQUIVO_ORIGINAL}' não foi encontrado.")

except PermissionError:
    print("Erro: Sem permissão para acessar ou criar o arquivo.")

except ValueError:
    print("Erro: Algum salário está em formato inválido.")

except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")