def divisao_segura(num,num2):
    try:
        if num2 == 0:
            raise ZeroDivisionError("Divisao por zero")

        resultado = num / num2

        print(f"Resultado: {resultado}")

    except ZeroDivisionError as e:
        print(f"Erro: {e}")

    except ValueError:
        print("Erro: digite apenas números, não letras.")

if __name__ == "__main__":
    num1 = float(input("Numero1: "))
    num2 = float(input("Numero2: "))
    divisao_segura(num1,num2)