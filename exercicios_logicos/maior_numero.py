def encontrar_maior(numeros: list) -> int:
    maior_numero = numeros[0]

    for numero in numeros:
        if numero > maior_numero:
            maior_numero = numero

    return maior_numero


print(encontrar_maior([10, 25, 7, 42, 18]))
print(encontrar_maior([3, 8, 2, 15, 6]))
print(encontrar_maior([-10, -5, -20, -2]))
print(encontrar_maior([7]))