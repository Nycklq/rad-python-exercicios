def classificar_nota(nota: float):
    if nota < 0 or nota > 10:
        return "Nota inválida"

    if nota >= 9 and nota <= 10:
        return "Excelente"
    elif nota >= 7 and nota < 9:
        return "Bom" 
    elif nota >= 5 and nota < 7:
        return "Regular" 
    else:
        return "Insuficiente" 

print(classificar_nota(9.5))
print(classificar_nota(7))
print(classificar_nota(4.5))
print(classificar_nota(11))