def segundo_maior(numeros: list) -> int | None:
    if len(numeros) < 2:
        return None

    maior = numeros[0]
    segundoMaior = None

    for numero in numeros:
        if numero > maior:
            segundoMaior = maior
            maior = numero

        if numero < maior:
            if segundoMaior is None or numero > segundoMaior:
                segundoMaior = numero

    return segundoMaior
        

print(segundo_maior([10, 25, 7, 42, 18]))
print(segundo_maior([10, 10, 8, 5]))
print(segundo_maior([-10, -5, -20, -2]))
print(segundo_maior([7, 7, 7]))