
SBox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
)

SBoxInv = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
)


def aplicar_relleno_PKCS7(texto, tamaño_bloque):
    longitud_texto = len(texto)
    caracteres_restantes = tamaño_bloque - (longitud_texto % tamaño_bloque)
    if caracteres_restantes != 0:
        texto_relleno = texto + \
            chr(caracteres_restantes) * caracteres_restantes
    else:
        texto_relleno = texto
    return texto_relleno


def rellenar_con_PKCS7(texto, clave):
    longitud_texto = len(texto)
    caracteres_restantes_texto = 16 - (longitud_texto % 16)
    if caracteres_restantes_texto != 0:
        texto_relleno = texto + \
            chr(caracteres_restantes_texto) * caracteres_restantes_texto
    else:
        texto_relleno = texto

    longitud_clave = len(clave)
    caracteres_restantes_clave = 16 - (longitud_clave % 16)
    if caracteres_restantes_clave != 0:
        clave_relleno = clave + \
            chr(caracteres_restantes_clave) * caracteres_restantes_clave
    else:
        clave_relleno = clave

    return texto_relleno[:16], clave_relleno[:16]  # Limitar a 16 caracteres


# Función para generar subclaves


def generar_subclaves(clave):
    subclaves = [clave]

    for i in range(10):
        clave_anterior = list(subclaves[-1])
        clave_anterior = clave_anterior[1:] + clave_anterior[:1]

        for j in range(4):
            clave_anterior[j] = SBox[clave_anterior[j]]

        rcon = [1, 0, 0, 0]
        rcon[0] ^= (rcon[0] << 1) ^ (0x11B & - (rcon[0] >> 7))
        clave_anterior[0] ^= rcon[0]

        subclave = [a ^ b for a, b in zip(
            clave_anterior, subclaves[-4] if len(subclaves) >= 4 else clave)]
        subclave = subclave[:16]  # Asegura que la subclave tenga 16 bytes
        subclaves.append(subclave)

    return subclaves


def add_round_key(estado, subclave):
    # print("Estado antes de Add Round Key:")
    imprimir_estado(estado)  # Imprime el estado antes de aplicar Add Round Key
    # print("Estado antes de Add Round Key:")
    imprimir_estado(estado)  # Imprime el estado antes de aplicar Add Round Key
    # Realiza la operación XOR en cada byte del estado con la subclave
    for i in range(len(estado)):
        estado[i] ^= subclave[i]
   # print("Subclave de la ronda actual:")
    imprimir_estado(subclave)
    # print("Estado después de Add Round Key:")
    imprimir_estado(estado)
   # print("Subclave de la ronda actual:")
    imprimir_estado(subclave)
    # print("Estado después de Add Round Key:")
    imprimir_estado(estado)


def imprimir_estado(estado):
    for fila in range(4):
        for columna in range(4):
            index = fila + columna * 4
            # Imprime el valor en formato hexadecimal con dos dígitos
            # print(f"{estado[index]:02X}", end=" ")
        # print()
            # print(f"{estado[index]:02X}", end=" ")
        # print()


def imprimir_subclave(subclave):
    for fila in range(4):
        for columna in range(4):
            index = fila + columna * 4
            # Imprime el valor en formato hexadecimal con dos dígitos
           # print(f"{subclave[index]:02X}", end=" ")
        # print()
           # print(f"{subclave[index]:02X}", end=" ")
        # print()


def imprimir_estado_y_subclave(ronda, estado, subclave):
   # print(f"\nRonda {ronda}:")
   # print(f"\nRonda {ronda}:")

    # print("Estado antes de Add Round Key:")
    # print("Estado antes de Add Round Key:")
    imprimir_estado(estado)

    # print("Subclave de la ronda actual:")
    # print("Subclave de la ronda actual:")
    imprimir_estado(subclave)

    # print("Estado después de Add Round Key:")
    # print("Estado después de Add Round Key:")
    imprimir_estado(estado)


def sub_bytes(estado):
    for i in range(len(estado)):
        estado[i] = SBox[estado[i]]


def aplicar_sub_bytes(estado):
    for i in range(len(estado)):
        estado[i] = SBox[estado[i]]

# Función para guardar la salida en un archivo


# Función para guardar la salida en un archivo
def guardar_en_archivo(texto):
    with open("resultado_aes.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto)


def shift_rows(estado):
    # Realiza la operación "Shift Rows" en el estado.
    for fila in range(1, 4):  # Comienza desde la segunda fila
        # Desplaza la fila hacia la izquierda en función de su índice
        estado[fila * 4:(fila + 1) * 4] = estado[fila * 4:(fila + 1)
                                                 * 4][fila:] + estado[fila * 4:(fila + 1) * 4][:fila]


def mix_columns(estado):
    # Matriz fija de mezcla para MixColumns
    matriz_mezcla = [
        0x02, 0x03, 0x01, 0x01,
        0x01, 0x02, 0x03, 0x01,
        0x01, 0x01, 0x02, 0x03,
        0x03, 0x01, 0x01, 0x02
    ]

    nuevo_estado = [0] * 16

    for columna in range(4):
        for fila in range(4):
            resultado = 0
            for i in range(4):
                resultado ^= gf_mult(
                    matriz_mezcla[i + columna * 4], estado[i + fila * 4])
            nuevo_estado[columna * 4 + fila] = resultado

    return nuevo_estado


def gf_mult(a, b):
    resultado = 0
    for _ in range(8):
        if b & 1:
            resultado ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11B  # Polinomio irreducible para AES
        b >>= 1
    return resultado

# Función para agregar la clave principal al texto plano
# Función para agregar la clave principal al texto plano


def add_round_key_inicio(estado, clave_principal):
    for i in range(len(estado)):
        estado[i] ^= clave_principal[i]


def inversa_mix_columns(estado):
    matriz_mezcla_inversa = [
        0x0E, 0x0B, 0x0D, 0x09,
        0x09, 0x0E, 0x0B, 0x0D,
        0x0D, 0x09, 0x0E, 0x0B,
        0x0B, 0x0D, 0x09, 0x0E
    ]

    nuevo_estado = [0] * 16

    for columna in range(4):
        for fila in range(4):
            resultado = 0
            for i in range(4):
                resultado ^= gf_mult(
                    matriz_mezcla_inversa[i + columna * 4], estado[i + fila * 4])
            nuevo_estado[columna * 4 + fila] = resultado

    return nuevo_estado


def inverso_sub_bytes(estado):
    for i in range(len(estado)):
        estado[i] = SBoxInv[estado[i]]


def inverso_shift_rows(estado):
    for fila in range(1, 4):
        estado[fila * 4:(fila + 1) * 4] = estado[fila * 4:(fila + 1)
                                                 * 4][-fila:] + estado[fila * 4:(fila + 1) * 4][:-fila]


def descifrar_aes(entrada, clave):
    clave_bytes = [ord(caracter) for caracter in clave]
    subclaves = generar_subclaves(clave_bytes)

    # Aplicar AddRoundKey al comienzo con la clave principal
    add_round_key_inicio(entrada, subclaves[-1])

    for ronda in range(9, -1, -1):
        subclave_actual = subclaves[ronda]

        # Deshacer AddRoundKey
        for i in range(len(entrada)):
            entrada[i] ^= subclave_actual[i]

        # Deshacer ShiftRows
        inverso_shift_rows(entrada)

        # Deshacer SubBytes
        inverso_sub_bytes(entrada)

        # No aplicar inverso MixColumns en la última ronda
        if ronda < 9:
            entrada = inversa_mix_columns(entrada)

    # Deshacer AddRoundKey Inicial
    add_round_key_inicio(entrada, clave_bytes)

    # Convierte la lista de enteros nuevamente a una cadena
    mensaje_descifrado = ''.join([chr(byte) for byte in entrada])

    return mensaje_descifrado


def guardar_pasos_descifrado_en_archivo(pasos_descifrado):
    with open("paso_a_paso_descifrado.txt", "w", encoding="utf-8") as archivo:
        archivo.write(pasos_descifrado)


# Línea divisoria
salida = '=' * 100 + '\n'

# Reemplaza esta parte del código para ingresar texto y clave con relleno
entrada = input("Por favor, ingresa un texto: ")[
    :16]  # Limita el texto a 16 caracteres
clave = input("Por favor, ingresa una clave: ")[
    :16]  # Limita la clave a 16 caracteres
texto_descifrado = entrada

# Con la llamada a la función rellenar_con_PKCS7
entrada, clave = rellenar_con_PKCS7(entrada, clave)

# Imprimir el texto con relleno y la clave con relleno
print(f"Texto con relleno: {entrada}")
print(f"Clave con relleno: {clave}")


# Convierte la entrada a una lista de enteros
entrada = [ord(caracter) for caracter in entrada]

# Convierte la clave en una lista de bytes
clave_bytes = [ord(caracter) for caracter in clave]

subclaves = generar_subclaves(clave_bytes)


# Generar e imprimir subclaves en formato hexadecimal y en matrices 4x4
for i, subclave in enumerate(subclaves):
    salida += f"\nSubclave {i} en formato hexadecimal:\n"
    for fila in range(4):
        for columna in range(4):
            index = fila + columna * 4
            salida += f"{subclave[index]:02X} "
        salida += '\n'


salida += '=' * 100 + '\n'

# Aplica "Add Round Key" al comienzo con la clave principal
add_round_key_inicio(entrada, clave_bytes)

# Agrega esta parte para mostrar el Add Round Key Inicial en el archivo
salida += "Estado de Add Round Key Inicial:\n"
for fila in range(4):
    for columna in range(4):
        index = fila + columna * 4
        salida += f"{entrada[index]:02X} "
    salida += '\n'


salida += '=' * 100 + '\n'

# Aplica "Add Round Key" al comienzo con la clave principal
add_round_key_inicio(entrada, clave_bytes)

# Agrega esta parte para mostrar el Add Round Key Inicial en el archivo
salida += "Estado de Add Round Key Inicial:\n"
for fila in range(4):
    for columna in range(4):
        index = fila + columna * 4
        salida += f"{entrada[index]:02X} "
    salida += '\n'

salida += '=' * 100 + '\n'

for ronda in range(10):
    subclave_actual = subclaves[ronda]
    salida += f"\nRonda {ronda}:\n"

    sub_bytes(entrada)  # Aplica Sub Bytes

    salida += "Estado después de Sub Bytes:\n"
    for fila in range(4):
        for columna in range(4):
            index = fila + columna * 4
            salida += f"{entrada[index]:02X} "
        salida += '\n'

    shift_rows(entrada)  # Aplica Shift Rows

    salida += "Estado después de Shift Rows:\n"
    for fila in range(4):
        for columna in range(4):
            index = fila + columna * 4
            salida += f"{entrada[index]:02X} "
        salida += '\n'

    if ronda < 9:  # No aplicar MixColumns en la última ronda
        # Realiza MixColumns
        entrada = mix_columns(entrada)

        salida += "Estado después de Mix Columns:\n"
        for fila in range(4):
            for columna in range(4):
                index = fila + columna * 4
                salida += f"{entrada[index]:02X} "
            salida += '\n'

    salida += "Estado antes de Add Round Key:\n"
    for fila in range(4):
        for columna in range(4):
            index = fila + columna * 4
            salida += f"{entrada[index]:02X} "
        salida += '\n'

    salida += "Subclave de la ronda actual:\n"
    for fila in range(4):
        for columna in range(4):
            index = fila + columna * 4
            salida += f"{subclave_actual[index]:02X} "
        salida += '\n'

    # Realiza Add Round Key
    for i in range(len(entrada)):
        entrada[i] ^= subclave_actual[i]

    salida += "Estado después de Add Round Key:\n"
    for fila in range(4):
        for columna in range(4):
            index = fila + columna * 4
            salida += f"{entrada[index]:02X} "
        salida += '\n'
        for fila in range(4):
            for columna in range(4):
                index = fila + columna * 4
                salida += f"{entrada[index]:02X} "
            salida += '\n'

    salida += "Estado antes de Add Round Key:\n"
    for fila in range(4):
        for columna in range(4):
            index = fila + columna * 4
            salida += f"{entrada[index]:02X} "
        salida += '\n'

    salida += "Subclave de la ronda actual:\n"
    for fila in range(4):
        for columna in range(4):
            index = fila + columna * 4
            salida += f"{subclave_actual[index]:02X} "
        salida += '\n'

    # Realiza Add Round Key
    for i in range(len(entrada)):
        entrada[i] ^= subclave_actual[i]

    salida += "Estado después de Add Round Key:\n"
    for fila in range(4):
        for columna in range(4):
            index = fila + columna * 4
            salida += f"{entrada[index]:02X} "
        salida += '\n'


salida += '=' * 100 + '\n'

# Guarda la salida en un archivo
guardar_en_archivo(salida)


# Inicializa la variable pasos_descifrado
pasos_descifrado = ""

salida += '=' * 100 + '\n'

for ronda in range(10):
    subclave_actual = subclaves[ronda]
    pasos_descifrado += f"\nRonda {ronda}:\n"

    sub_bytes(entrada)  # Aplica Sub Bytes

    pasos_descifrado += "Estado después de Inverso SubBytes:\n"
    for fila in range(4):
        for columna in range(4):
            index = fila + columna * 4
            pasos_descifrado += f"{entrada[index]:02X} "
        pasos_descifrado += '\n'

    shift_rows(entrada)  # Aplica Shift Rows

    pasos_descifrado += "Estado después de Inverso ShiftRows:\n"
    for fila in range(4):
        for columna in range(4):
            index = fila + columna * 4
            pasos_descifrado += f"{entrada[index]:02X} "
        pasos_descifrado += '\n'

    if ronda < 9:  # No aplicar MixColumns en la última ronda
        # Realiza MixColumns
        entrada = mix_columns(entrada)

        pasos_descifrado += "Estado después de Inversa MixColumns:\n"
        for fila in range(4):
            for columna in range(4):
                index = fila + columna * 4
                pasos_descifrado += f"{entrada[index]:02X} "
            pasos_descifrado += '\n'

    pasos_descifrado += "Estado antes de Add Round Key:\n"
    for fila in range(4):
        for columna in range(4):
            index = fila + columna * 4
            pasos_descifrado += f"{entrada[index]:02X} "
        pasos_descifrado += '\n'

    pasos_descifrado += "Subclave de la ronda actual:\n"
    for fila in range(4):
        for columna in range(4):
            index = fila + columna * 4
            pasos_descifrado += f"{subclave_actual[index]:02X} "
        pasos_descifrado += '\n'

    # Realiza Add Round Key
    for i in range(len(entrada)):
        entrada[i] ^= subclave_actual[i]

    pasos_descifrado += "Estado después de Add Round Key:\n"
    for fila in range(4):
        for columna in range(4):
            index = fila + columna * 4
            pasos_descifrado += f"{entrada[index]:02X} "
        pasos_descifrado += '\n'

salida += '=' * 100 + '\n'

# Guardar los pasos de descifrado en un archivo separado
guardar_pasos_descifrado_en_archivo(pasos_descifrado)

# Imprimir el mensaje cifrado en la misma línea
print("Mensaje cifrado:", ''.join([f"{byte:02X}" for byte in entrada]))

texto_cifrado = entrada
clave_descifrado = clave

# Realiza el proceso de descifrado
texto_decifrado = descifrar_aes(texto_cifrado, clave_descifrado)

# Convierte el texto descifrado en una lista de bytes
texto_descifrado_bytes = [ord(caracter) for caracter in texto_descifrado]

# Elimina el relleno PKCS7 al final del texto descifrado
relleno = texto_descifrado_bytes[-1]
texto_descifrado_bytes = texto_descifrado_bytes[:-relleno]

# Convierte la lista de bytes nuevamente a una cadena de caracteres
texto_decifrado = ''.join([chr(byte) for byte in texto_descifrado_bytes])

# Imprime el texto descifrado
print("Mensaje descifrado: ", texto_descifrado)

# Imprime mensaje de finalización
print("Paso a paso cifrado guardado en 'resultado_aes.txt'")
print("Paso a paso descifrado guardado en 'paso_a_paso_descifrado.txt'")

# Pausa la ejecución para que la consola no se cierre inmediatamente
input("Presiona Enter para salir...")
