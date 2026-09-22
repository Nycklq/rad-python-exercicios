def somar_numeros(numero: int):
    soma = 0
    for i in range(1,numero + 1):
        soma += i
    return soma

print(somar_numeros(5))
print(somar_numeros(3))
print(somar_numeros(10))
print(somar_numeros(20))
print(somar_numeros(1))