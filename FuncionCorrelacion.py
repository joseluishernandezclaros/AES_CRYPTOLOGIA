def calculate_mcc(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("Las secuencias deben tener la misma longitud")
    a = b = c = d = 0
    for i in range(len(seq1)):
        if seq1[i] == 1 and seq2[i] == 1:
            a += 1
        elif seq1[i] == 1 and seq2[i] == 0:
            b += 1
        elif seq1[i] == 0 and seq2[i] == 1:
            c += 1
        elif seq1[i] == 0 and seq2[i] == 0:
            d += 1
    mcc = (a * d - b * c) / ((a + b) * (a + c) * (b + d) * (c + d)
                             )**0.5 if (a + b) * (a + c) * (b + d) * (c + d) != 0 else 0
    return mcc


# Ejemplo de uso:
mensaje = '100011100110001100110011010010011110101001111101101000011010111101011001011011000011000111001001'
mensaje2 = '000010111100110000111101000111111001010000100011001011100001111011011111100100000011001010011111'
secuencia_1 = [int(digito) for digito in mensaje]
secuencia_2 = [int(digito) for digito in mensaje2]


resultado_mcc = calculate_mcc(secuencia_1, secuencia_2)
print(
    f"El coeficiente de correlación de Matthews (MCC) entre las secuencias es: {resultado_mcc}")
