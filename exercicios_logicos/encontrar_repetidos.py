def encontrar_repetidos(numeros: list) -> list:
    numeros_repetidos = []

    for numero in numeros:
        cont = 0

        for item in numeros:
            if numero == item:
                cont += 1

        if cont > 1 and numero not in numeros_repetidos:
            numeros_repetidos.append(numero)

    return numeros_repetidos

print(encontrar_repetidos([2, 5, 2, 8, 5, 10, 3]))
print(encontrar_repetidos([1, 1, 1, 2, 2, 3]))
print(encontrar_repetidos([4, 5, 6, 7]))
print(encontrar_repetidos([9, 9, 9, 9]))
print(encontrar_repetidos([]))