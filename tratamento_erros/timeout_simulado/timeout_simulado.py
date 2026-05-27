from connectionException import ConnectionTimeoutError
import random

def simular_requisicao():
    numero = random.randint(1, 10)

    print(f"Número gerado: {numero}")

    if numero % 2 == 0:
        raise ConnectionTimeoutError("Tempo de conexão esgotado.")

    return "Requisição realizada com sucesso!"


def main():
    try:
        resposta = simular_requisicao()
        print(resposta)

    except ConnectionTimeoutError as erro:
        print(f"Erro de conexão: {erro}")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")


if __name__ == "__main__":
    main()