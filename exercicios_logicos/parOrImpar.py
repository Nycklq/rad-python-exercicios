def verificar_numero(num: int):
    if num % 2 == 0:
        return "Par"
    else:
        return "impar"

print(verificar_numero(8))
print(verificar_numero(5))
print(verificar_numero(0))