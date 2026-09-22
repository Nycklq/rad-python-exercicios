def contar_ocorrencias(numeros: list, alvo: int) -> int:
    
    cont = 0

    for numero in numeros:
        if numero == alvo:
            cont += 1

    return cont


print(contar_ocorrencias([2, 5, 2, 8, 2, 10, 5], 2))
print(contar_ocorrencias([1, 3, 3, 7, 3], 3))
print(contar_ocorrencias([4, 5, 6], 9))
print(contar_ocorrencias([], 2))
print(contar_ocorrencias([7, 7, 7, 7], 7))
print(contar_ocorrencias([-1, 2, -1, 3], -1))