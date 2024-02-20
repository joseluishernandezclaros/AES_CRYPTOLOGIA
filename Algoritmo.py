# Rererencias
matriz_referencia = [
    ['0', '00', '01', '10', '11'],
    ['00', '1001', '0100', '1010', '1011'],
    ['01', '1101', '0001', '1000', '0101'],
    ['10', '0110', '0010', '0000', '0011'],
    ['11', '1100', '1110', '1111', '0111']
]


def obtener_mensaje_binario(mensaje_tipo):
    while True:
        mensaje_hex = input(f"Ingrese {mensaje_tipo} en hexadecimal: ")[:4]

        # Verificar si se ingresó un mensaje hexadecimal
        if mensaje_hex:
            try:
                # Convertir el mensaje hexadecimal a su representación binaria de 16 bits
                binarios = [format(int(mensaje_hex, 16), '016b')]
                return binarios[0]
            except ValueError:
                print("Ingrese un valor hexadecimal válido.")
        else:
            print("Debe ingresar un mensaje válido en hexadecimal.")


# Obtener mensajes válidos en hexadecimal


binary_number = obtener_mensaje_binario("mensaje")
binary_number2 = obtener_mensaje_binario("clave")


'''
binary_number = "1101011100101000"
binary_number2 = "0100101011110101"
'''

print("El mensaje en binario es:", binary_number)
print("La clave en binario es:", binary_number2)


# ------------EXPAND KEY -----------------------#

RCON_1 = '10000000'
RCON_2 = '00110000'

# Dividir la clave en dos partes, cada una con 8 bits
w0 = binary_number2[:8]
w1 = binary_number2[8:16]

# Mostrar las dos partes en consola
# print("w0:", w0)
# print("w1:", w1)

# Rotar los primeros 8 bits de w1 del final al inicio y viceversa
g_w1 = w1[4:] + w1[:4]

# Mostrar el resultado en consola
# print("g(w1) rotado:", g_w1)

# Realizar la sustitución de nibbles usando la matriz de referencia
g_w1_sustituido = ''

for i in range(0, len(g_w1), 4):
    nibble = g_w1[i:i+4]
    fila = int(nibble[0:2], 2)
    columna = int(nibble[2:], 2)

    # Realizar el corrimiento para encontrar la posición correcta en la matriz
    fila = (fila + 1) % 5
    columna = (columna + 1) % 5

    g_w1_sustituido += matriz_referencia[fila][columna]

# Mostrar el resultado en consola
# print("g(w1) sustituido:", g_w1_sustituido)


# Realizar la operación XOR con RCON_1
resultado_xor_rcon1 = ''.join([str(int(bit_g_w1) ^ int(
    bit_rcon1)) for bit_g_w1, bit_rcon1 in zip(g_w1_sustituido, RCON_1)])

# Mostrar el resultado en consola
# print("Resultado XOR con RCON_1:", resultado_xor_rcon1)

# Realiza la operación XOR bit a bit
resultado_xor = ''.join([str(int(bit_w0) ^ int(bit_rcon1))
                        for bit_w0, bit_rcon1 in zip(w0, resultado_xor_rcon1)])

# Muestra el resultado en consola
# print("Resultado XOR entre w0 y resultado_xor_rcon1:", resultado_xor)


w2 = resultado_xor

# Realiza la operación XOR bit a bit
w3 = ''.join([str(int(bit_w1) ^ int(bit_w2))
             for bit_w1, bit_w2 in zip(w1, w2)])

# Muestra el resultado en consola
# print("w3:", w3)

# Rotar los primeros 8 bits de w3 del final al inicio y viceversa
g_w3 = w3[4:] + w3[:4]

# Mostrar el resultado en consola
# print("g(w3) rotado:", g_w3)

# Realizar la sustitución de nibbles usando la matriz de referencia
g_w3_sustituido = ''

for i in range(0, len(g_w3), 4):
    nibble = g_w3[i:i+4]
    fila = int(nibble[0:2], 2)
    columna = int(nibble[2:], 2)

    # Realizar el corrimiento para encontrar la posición correcta en la matriz
    fila = (fila + 1) % 5
    columna = (columna + 1) % 5

    g_w3_sustituido += matriz_referencia[fila][columna]

# Mostrar el resultado en consola
# print("g(w3) sustituido:", g_w3_sustituido)

# Realizar la operación XOR con RCON_2
resultado_xor_rcon2 = ''.join([str(int(bit_g_w3) ^ int(
    bit_rcon2)) for bit_g_w3, bit_rcon2 in zip(g_w3_sustituido, RCON_2)])

# Mostrar el resultado en consola
# print("Resultado XOR con RCON_2:", resultado_xor_rcon2)

resultado_xor2 = ''.join([str(int(bit_w2) ^ int(bit_rcon2))
                          for bit_w2, bit_rcon2 in zip(w2, resultado_xor_rcon2)])

# Muestra el resultado en consola
# print("Resultado XOR entre w2 y resultado_xor_rcon2:", resultado_xor)

w4 = resultado_xor2

# Realiza la operación XOR bit a bit
w5 = ''.join([str(int(bit_w4) ^ int(bit_w3))
              for bit_w4, bit_w3 in zip(w4, w3)])

# Muestra el resultado en consola
# print("w5:", w5)


k0 = w0+w1
# print("k0:" + k0)

k1 = w2+w3
# print("k0:" + k1)

k2 = w4+w5
# print("k0:" + k2)


# ------------ADD ROUND KEY -----------------------#
# Convertimos esos numeros binarios en matrices 2x2


def convertir_matriz(numero):
    # Número binario de 16 bits
    numero_binario = numero
    # Dividir el número binario en segmentos de 4 bits
    segmentos = [numero_binario[i:i+4]
                 for i in range(0, len(numero_binario), 4)]
    # Crear una matriz 2x2 con los segmentos
    matriz = [segmentos[:2], segmentos[2:]]
    return matriz


matriz1 = convertir_matriz(binary_number)
matriz2 = convertir_matriz(binary_number2)

# AddRoundKey

# Función para realizar la operación XOR entre los elementos correspondientes de las matrices


def xor_matrices(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[i])):
            num1 = int(matriz1[i][j], 2)
            num2 = int(matriz2[i][j], 2)
            resultado_xor = num1 ^ num2
            # Agrega el resultado a la fila en formato binario de 4 bits
            fila.append(format(resultado_xor, '04b'))
        resultado.append(fila)
    return resultado


# Realizar la operación XOR entre las matrices y obtener el resultado
resultado_xor_matrices = xor_matrices(matriz1, matriz2)


# Mostrar el resultado
'''
for fila in resultado_xor_matrices:
    print(fila)
'''

# -----------------NIBBLE SUBSTITUTION -------------


# Concatenar las cadenas en cada fila y unirlas
n1 = ''.join([''.join(fila) for fila in resultado_xor_matrices])

# Mostrar el resultado
# print("La cadena resultante es:", n1)

# Variable para almacenar el resultado de la sustitución
n1_sustituido = ''

# Aplicar la sustitución a cada nibble en la cadena n1
for i in range(0, len(n1), 4):
    nibble = n1[i:i+4]
    fila = int(nibble[0:2], 2)
    columna = int(nibble[2:], 2)

    # Realizar el corrimiento para encontrar la posición correcta en la matriz
    fila = (fila + 1) % 5
    columna = (columna + 1) % 5

    # Agregar el resultado de la sustitución a la cadena final
    n1_sustituido += matriz_referencia[fila][columna]

# Mostrar el resultado de la sustitución
# print("La cadena sustituida es:", n1_sustituido)


# ---------------------SHIFT ROWS--------------


# Convertir la cadena en una lista para facilitar la manipulación
lista_caracteres = list(n1_sustituido)

# Posiciones a intercambiar
posiciones_a_intercambiar = [5, 6, 7, 8]
posiciones_destino = [13, 14, 15, 16]

# Intercambiar los caracteres en las posiciones especificadas
for pos_origen, pos_destino in zip(posiciones_a_intercambiar, posiciones_destino):
    lista_caracteres[pos_origen - 1], lista_caracteres[pos_destino -
                                                       1] = lista_caracteres[pos_destino - 1], lista_caracteres[pos_origen - 1]

# Convertir la lista de nuevo a cadena
cadena_resultante = ''.join(lista_caracteres)

# Mostrar el resultado
# print("shift row: " + cadena_resultante)


# MIX COLUMNNS


# Función para imprimir valores en bloques de 4 bits en el archivo (16 bits)
def imprimir_valores_16_bits(archivo, titulo, valores):
    archivo.write("{}: ".format(titulo))

    for valor in valores:
        resultado_formateado = ''.join(valor)
        for i in range(0, len(resultado_formateado), 4):
            bloque = resultado_formateado[i:i+4]
            archivo.write(bloque + " ")

    archivo.write("\n")


# Crear un archivo de texto para almacenar los resultados
with open('resultados_s-aes.txt', 'w') as archivo:

    archivo.write(
        "w0: {}\n".format(w0))
    archivo.write(
        "w1: {}\n".format(w1))
    archivo.write(
        "w2: {}\n".format(w2))
    archivo.write(
        "w3: {}\n".format(w3))
    archivo.write(
        "w4: {}\n".format(w4))
    archivo.write(
        "w5: {}\n".format(w5))

    # Llama a la función correspondiente para imprimir el valor de k0, k1 y k2 en el archivo
    imprimir_valores_16_bits(archivo, "k0", [k0])
    imprimir_valores_16_bits(archivo, "k1", [k1])
    imprimir_valores_16_bits(archivo, "k2", [k2])

    salida = '=' * 100 + '\n'
    archivo.write(salida)

    # Round 0 (AddRoundKey)

    archivo.write("Round 0 \n")
    salida = '=' * 100 + '\n'
    archivo.write(salida)

    # Imprime la variable en bloques de 4 bits en el archivo
    archivo.write("Add Round Key: ")
    for fila in resultado_xor_matrices:
        resultado_formateado = ''.join(fila)
        for i in range(0, len(resultado_formateado), 4):
            bloque = resultado_formateado[i:i+4]
            archivo.write(bloque + " ")
    archivo.write("\n")

    salida = '=' * 100 + '\n'
    archivo.write(salida)

    # Round 1

    archivo.write("Round 1 \n")
    salida = '=' * 100 + '\n'
    archivo.write(salida)

    # nibble
    imprimir_valores_16_bits(archivo, "Nibble Substitution", [n1_sustituido])

    # shift rows
    imprimir_valores_16_bits(archivo, "Shift Rows", [cadena_resultante])

    salida = '=' * 100 + '\n'
    archivo.write(salida)
