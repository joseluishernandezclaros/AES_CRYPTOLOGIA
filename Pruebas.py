#Rererencias
import random

matriz_referencia_code = [
    ['0', '00', '01', '10', '11'],
    ['00', '1001', '0100', '1010', '1011'],
    ['01', '1101', '0001', '1000', '0101'],
    ['10', '0110', '0010', '0000', '0011'],
    ['11', '1100', '1110', '1111', '0111']
]

matriz_referencia_inverse = [
    ['0', '00', '01', '10', '11'],
    ['00', '1010', '0101', '1001', '1011'],
    ['01', '0001', '0111', '1000', '1111'],
    ['10', '0110', '0000', '0010', '0011'],
    ['11', '1100', '0100', '1101', '1110']
]

matriz = [
    ['0','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'],
    ['4','0','4','8','C','3','7','B','F','6','2','E','A','5','1','D','9']
]

matriz_inverse2 = [
    ['0','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'],
    ['2','0','2','4','6','8','A','C','E','3','1','7','5','B','9','F','D']
]

matriz_inverse9 = [
    ['0','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'],
    ['9','0','9','1','8','2','B','3','A','4','D','5','C','6','F','7','E']
]

variableCifrado = ''
variableDescifrado = ''

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
binary_number2 = obtener_mensaje_binario("clave")
# ------------EXPAND KEY -----------------------#
RCON_1 = '10000000'
RCON_2 = '00110000'

# DivIdir la clave en dos partes, cada una con 8 bits
w0 = binary_number2[:8]
w1 = binary_number2[8:16]

# Rotar los primeros 8 bits de w1 del final al inicio y viceversa
g_w1 = w1[4:] + w1[:4]

# Realizar la sustitución de nibbles usando la matriz de referencia
g_w1_sustituido = ''

for i in range(0, len(g_w1), 4):
    nibble = g_w1[i:i+4]
    fila = int(nibble[0:2], 2)
    columna = int(nibble[2:], 2)

    # Realizar el corrimiento para encontrar la posición correcta en la matriz
    fila = (fila + 1) % 5
    columna = (columna + 1) % 5

    g_w1_sustituido += matriz_referencia_code[fila][columna]

# Realizar la operación XOR con RCON_1
resultado_xor_rcon1 = ''.join([str(int(bit_g_w1) ^ int(
    bit_rcon1)) for bit_g_w1, bit_rcon1 in zip(g_w1_sustituido, RCON_1)])

# Realiza la operación XOR bit a bit
resultado_xor = ''.join([str(int(bit_w0) ^ int(bit_rcon1))
                        for bit_w0, bit_rcon1 in zip(w0, resultado_xor_rcon1)])
w2 = resultado_xor
# Realiza la operación XOR bit a bit
w3 = ''.join([str(int(bit_w1) ^ int(bit_w2))
            for bit_w1, bit_w2 in zip(w1, w2)])

# Rotar los primeros 8 bits de w3 del final al inicio y viceversa
g_w3 = w3[4:] + w3[:4]

# Realizar la sustitución de nibbles usando la matriz de referencia
g_w3_sustituido = ''

for i in range(0, len(g_w3), 4):
    nibble = g_w3[i:i+4]
    fila = int(nibble[0:2], 2)
    columna = int(nibble[2:], 2)

    # Realizar el corrimiento para encontrar la posición correcta en la matriz
    fila = (fila + 1) % 5
    columna = (columna + 1) % 5

    g_w3_sustituido += matriz_referencia_code[fila][columna]


# Realizar la operación XOR con RCON_2
resultado_xor_rcon2 = ''.join([str(int(bit_g_w3) ^ int(
    bit_rcon2)) for bit_g_w3, bit_rcon2 in zip(g_w3_sustituido, RCON_2)])


resultado_xor2 = ''.join([str(int(bit_w2) ^ int(bit_rcon2))
                        for bit_w2, bit_rcon2 in zip(w2, resultado_xor_rcon2)])

w4 = resultado_xor2

# Realiza la operación XOR bit a bit
w5 = ''.join([str(int(bit_w4) ^ int(bit_w3))
            for bit_w4, bit_w3 in zip(w4, w3)])

k0 = w0+w1
k1 = w2+w3
k2 = w4+w5

def bin_to_hex(binario):
    # Asegurarse de que la longitud sea un múltiplo de 4
    while len(binario) % 4 != 0:
        binario = '0' + binario  # Agregar ceros a la izquierda si no es múltiplo de 4

    # Dividir el número binario en grupos de 4 bits
    grupos = [binario[i:i + 4] for i in range(0, len(binario), 4)]

    # Mapear los grupos binarios a sus equivalentes hexadecimales
    hexa = ''.join(hex(int(grupo, 2))[2:] for grupo in grupos)

    return hexa.upper()  # Devolver en mayúsculas, por convención hexadecimal


key0Hex = bin_to_hex(k0)
key1Hex = bin_to_hex(k1)
key2Hex = bin_to_hex(k2)

def proceso(mensaje,clave1,clave2,clave3):

    key0Hex = clave1
    key1Hex = clave2
    key2Hex = clave3

    messageHex = mensaje

    # Convertir hexadecimal a binario
    messageInt = int(messageHex, 16) 
    messageBin = bin(messageInt)[2:].zfill(16) 
    key0Int = int(key0Hex, 16) 
    key0Bin = bin(key0Int)[2:].zfill(16)

    #------------ADD ROUND KEY -----------------------#

    #Funcion convertir numeros binarios en matrices
    def convertir_matriz(numero):
        numero_binario = numero
        segmentos = [numero_binario[i:i+4] for i in range(0, len(numero_binario), 4)]
        matriz = [segmentos[:2], segmentos[2:]]
        matriz[0][1], matriz[1][0] = matriz[1][0], matriz[0][1]
        return matriz

    # Función para realizar la operación XOR entre los elementos correspondientes de las matrices de numeros binarios
    def xor_matrices(matriz1, matriz2):
        resultado = []
        for i in range(len(matriz1)):
            fila = []
            for j in range(len(matriz1[i])):
                num1 = int(matriz1[i][j], 2)
                num2 = int(matriz2[i][j], 2)
                resultado_xor = num1 ^ num2
                fila.append(format(resultado_xor, '04b'))
            resultado.append(fila)
        return resultado

    #Funcion AddRoundKey recibe el mensaje y la llave como un numero binario
    def AddRoundKey(binary_number, binary_number2):
        matriz1 = convertir_matriz(binary_number)
        matriz2 = convertir_matriz(binary_number2)
        # Realizar la operación XOR entre las matrices y obtener el resultado
        resultado_xor_matrices = xor_matrices(matriz1, matriz2)
        return(resultado_xor_matrices)
        
    matrizAddRoundKey = AddRoundKey(messageBin,key0Bin)

    #-----------------NIBBLE SUBSTITUTION -------------

    def nibbleSubstitution(mi_matriz,matriz_referencia):
        matriz = mi_matriz
        def encontrar_posiciones(matriz):
            posiciones = []
            for fila in matriz:
                for celda in fila:
                    primera_mitad = celda[:2]
                    for i, columna in enumerate(matriz_referencia):
                        if primera_mitad == columna[0]:
                            posiciones.append((i, 0))
                            break

            return posiciones

        def encontrar_posiciones2(matriz):
            posiciones = []
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    segunda_mitad = matriz[i][j][2:]
                    for y in range(len(matriz_referencia[0])):
                        if matriz_referencia[0][y] == segunda_mitad:
                            posiciones.append((0, y))

            return posiciones

        resultado_primeras_posiciones = encontrar_posiciones(mi_matriz)
        resultado_segundas_posiciones = encontrar_posiciones2(mi_matriz)
        resultado_primeras_posiciones[1], resultado_primeras_posiciones[2] = resultado_primeras_posiciones[2], resultado_primeras_posiciones[1]
        resultado_segundas_posiciones[1], resultado_segundas_posiciones[2] = resultado_segundas_posiciones[2], resultado_segundas_posiciones[1]
        #Combinamos ambos vectores para formar un unico vector con las posiciones a intercambiar
        resultado = [(x[0], y[1]) for x, y in zip(resultado_primeras_posiciones, resultado_segundas_posiciones)]

        #Algoritmo  crea la matriz a partir de las coordenadas
        def crear_matriz_resultante(matriz_referencia, coordenadas):
            matriz_resultante = [['', ''], ['', '']]
            for idx, coordenada in enumerate(coordenadas):
                fila, columna = coordenada
                valor = matriz_referencia[fila][columna]
                matriz_resultante[idx % 2][idx // 2] = valor
            return matriz_resultante
        # Arreglo de coordenadas
        coordenadas = resultado
        # Crear la matriz resultante
        matriz_resultante = crear_matriz_resultante(matriz_referencia, coordenadas)
        return matriz_resultante

    matrizNibbleSubstition = nibbleSubstitution(matrizAddRoundKey,matriz_referencia_code)

    #---------------------SHIFT ROWS--------------
    def shiftRows(matriz_resultante):
        matriz_shift = [['', ''], ['', '']]
        matriz_shift = matriz_resultante
        # Intercambiar los valores en las posiciones [1][0] y [1][1]
        matriz_shift[1][0], matriz_shift[1][1] = matriz_shift[1][1], matriz_shift[1][0]
        return matriz_shift

    matrizShifRows = shiftRows(matrizNibbleSubstition)

    #--------------------------MIX COLUMNNS-------------
    def mixColumns(matriz_shift):
        matriz_hex = []
        for fila in matriz_shift:
            fila_hex = [hex(int(valor_binario, 2))[2:].upper() for valor_binario in fila]
            matriz_hex.append(fila_hex)

        mix_matriz = [['', ''],['', '']]
        mix_matriz = matriz_hex
        Sa = mix_matriz[0][0]
        Sb = mix_matriz[1][0]
        Sc = mix_matriz[0][1]
        Sd = mix_matriz[1][1]

        def buscar_valor(matriz, valor):
            
            if valor == '0':
                return '0'
            
            valor = valor.upper()

            if valor in matriz[0]:
                indice = matriz[0].index(valor)
                resultado = matriz[1][indice]
                return resultado
            else:
                return None  
        #Definimos los cuatro elementos las variables que van a guardar el resultados de las operaciones en GF(16)
        a = buscar_valor(matriz,Sa)
        b = buscar_valor(matriz,Sb)
        c = buscar_valor(matriz,Sc)
        d = buscar_valor(matriz,Sd)

        S0 = int(Sa,16) ^ int(b,16)
        bin_S0 = format(S0, '04b')
        S1 = int(a,16) ^ int(Sb,16)
        bin_S1 = format(S1, '04b')
        S2 = int(Sc,16) ^ int(d,16)
        bin_S2 = format(S2, '04b')
        S3 = int(c,16) ^ int(Sd,16)
        bin_S3 = format(S3, '04b')

        #Contruimos la matriz resultado del MixColumns
        matriz_resultado = [
            [S0, S2],
            [S1, S3]
        ]
        mix_matriz_hex = []
        for fila in matriz_resultado:
            fila_hex = [hex(valor_decimal)[2:].upper() for valor_decimal in fila]
            mix_matriz_hex.append(fila_hex)
        return(mix_matriz_hex)


    matrizMixColumns = mixColumns(matrizShifRows)
    #CONVERSIONES
    arreglo = []
    for fila in matrizMixColumns:
        for elemento in fila:
            arreglo.append(elemento)

    arreglo[1],arreglo[2] = arreglo[2],arreglo[1]
    # Unir los elementos del arreglo en una sola cadena
    hexadecimal = ''.join(arreglo)
    # Convertir la cadena hexadecimal a un número entero
    numero = int(hexadecimal, 16)
    # Convertir el número de nuevo a una cadena en formato hexadecimal
    hexadecimal_final = hex(numero)[2:].upper()  # [2:] para quitar '0x' al inicio y upper() para convertir a mayúsculas


    # Add Round Key. Con el resultado que nos quedó de Mix Columns y la Key1

    messageInt2 = int(hexadecimal_final, 16)  # Convierte de hexadecimal a decimal
    messageBin2 = bin(messageInt2)[2:].zfill(16)  # Convierte de decimal a binario y asegura que tenga 16 bits
    key1Int = int(key1Hex, 16)  # Convierte de hexadecimal a decimal
    key1Bin = bin(key1Int)[2:].zfill(16)  # Convierte de decimal a binario y asegura que tenga 16 bits

    #------------ADD ROUND KEY -----------------------#

    matrizAddRoundKey2 = AddRoundKey(messageBin2,key1Bin)

    #-------------- NIBBLE SUBSTITION 2 --------------------#
    matrizNibbleSubstition2 = nibbleSubstitution(matrizAddRoundKey2,matriz_referencia_code)

    #-------------- SHIFT ROW 2 --------------------#
    matrizShifRows2 = shiftRows(matrizNibbleSubstition2)


    #------------ADD ROUND KEY 3 ----------------#
    key2Int = int(key2Hex, 16)  # Convierte de hexadecimal a decimal
    key2Bin = bin(key2Int)[2:].zfill(16)  # Convierte de decimal a binario y asegura que tenga 16 bits

    def bin_to_hex(numero_binario):
        # Convertir binario a decimal y luego a hexadecimal
        decimal = int(numero_binario, 2)
        hexadecimal = hex(decimal)[2:].upper()  # [2:] para quitar '0x' al inicio y upper() para convertir a mayúsculas
        return hexadecimal
    # Convertir la matriz de binario a hexadecimal
    matriz_hex = [
        [bin_to_hex(numero) for numero in fila] for fila in matrizShifRows2
    ]

    #CONVERSIONES
    arreglo2 = []
    for fila in matriz_hex:
        for elemento in fila:
            arreglo2.append(elemento)

    arreglo2[1],arreglo2[2] = arreglo2[2],arreglo2[1]
    # Unir los elementos del arreglo en una sola cadena
    hexadecimal = ''.join(arreglo2)
    # Convertir la cadena hexadecimal a un número entero
    numero = int(hexadecimal, 16)
    # Convertir el número de nuevo a una cadena en formato hexadecimal
    hexadecimal_final2 = hex(numero)[2:].upper()  # [2:] para quitar '0x' al inicio y upper() para convertir a mayúsculas

    messageInt3 = int(hexadecimal_final2, 16)  # Convierte de hexadecimal a decimal
    messageBin3 = bin(messageInt3)[2:].zfill(16)  # Convierte de decimal a binario y asegura que tenga 16 bits


    #------------ADD ROUND KEY -----------------------#
    matrizAddRoundKey3 = AddRoundKey(messageBin3,key2Bin)


    matrizAddRoundKey3[1][0], matrizAddRoundKey3[0][1] = matrizAddRoundKey3[0][1], matrizAddRoundKey3[1][0]
    def matriz_a_binario(matriz):
        # Concatenar todos los elementos de la matriz
        binario = ''.join([''.join(fila) for fila in matriz])
        return binario
    mensajeCifrado = matriz_a_binario(matrizAddRoundKey3)

    #<-------------------Descifrado---------------------------->
    matrizAddRoundKey3Inverse = AddRoundKey(mensajeCifrado,key2Bin)

    #InverseShiftRows
    matrizShifRowsInverse = shiftRows(matrizAddRoundKey3Inverse)

    #InverseNibbleSubstitution 1
    matrizNibbleSubstitionInverse1 = nibbleSubstitution(matrizAddRoundKey3Inverse,matriz_referencia_inverse)
 
    #InverseAddRoundKey2
    matrizNibbleSubstitionInverse1[1][0], matrizNibbleSubstitionInverse1[0][1] = matrizNibbleSubstitionInverse1[0][1], matrizNibbleSubstitionInverse1[1][0]
    InverseBinary = matriz_a_binario(matrizNibbleSubstitionInverse1)
    matrizAddRoundKey2Inverse = AddRoundKey(InverseBinary,key1Bin)

    #InverseMixColumns
    #--------------------------MIX COLUMNNS-------------
    def mixColumnsInverse(matriz_shift):
        matriz_hex = []
        for fila in matriz_shift:
            fila_hex = [hex(int(valor_binario, 2))[2:].upper() for valor_binario in fila]
            matriz_hex.append(fila_hex)

        mix_matriz = [['', ''],['', '']]
        mix_matriz = matriz_hex
        Sa = mix_matriz[0][0]
        Sb = mix_matriz[1][0]
        Sc = mix_matriz[0][1]
        Sd = mix_matriz[1][1]

        def buscar_valor(matriz, valor):
            
            if valor == '0':
                return '0'
            
            valor = valor.upper()

            if valor in matriz[0]:
                indice = matriz[0].index(valor)
                resultado = matriz[1][indice]
                return resultado
            else:
                return None  
        #Definimos los cuatro elementos las variables que van a guardar el resultados de las operaciones en GF(16)
        a = buscar_valor(matriz_inverse2,Sa)
        b = buscar_valor(matriz_inverse2,Sb)
        c = buscar_valor(matriz_inverse2,Sc)
        d = buscar_valor(matriz_inverse2,Sd)

        aa = buscar_valor(matriz_inverse9,Sa)
        bb = buscar_valor(matriz_inverse9,Sb)
        cc = buscar_valor(matriz_inverse9,Sc)
        dd = buscar_valor(matriz_inverse9,Sd)

        S0 = int(aa,16) ^ int(b,16)
        bin_S0 = format(S0, '04b')
        S1 = int(a,16) ^ int(bb,16)
        bin_S1 = format(S1, '04b')
        S2 = int(cc,16) ^ int(d,16)
        bin_S2 = format(S2, '04b')
        S3 = int(c,16) ^ int(dd,16)
        bin_S3 = format(S3, '04b')

        #Contruimos la matriz resultado del MixColumns
        matriz_resultado = [
            [S0, S2],
            [S1, S3]
        ]
        mix_matriz_hex = []
        for fila in matriz_resultado:
            fila_hex = [hex(valor_decimal)[2:].upper() for valor_decimal in fila]
            mix_matriz_hex.append(fila_hex)
        return(mix_matriz_hex)


    matrizMixColumnsInverse = mixColumnsInverse(matrizAddRoundKey2Inverse)

    #InverseShiftRows2
    matrizShifRowsInverse2 = shiftRows(matrizMixColumnsInverse)


    def matriz_hex_a_bin(matriz_hex):
        matriz_bin = []
        for fila in matriz_hex:
            fila_bin = [format(int(valor, 16), '04b') for valor in fila]
            matriz_bin.append(fila_bin)
        return matriz_bin

    # Convertir a matriz binaria
    matrizShifRowsInverse2Bin = matriz_hex_a_bin(matrizShifRowsInverse2)

    #InverseNibbleSubstitution 2
    matrizNibbleSubstitionInverse2 = nibbleSubstitution(matrizShifRowsInverse2Bin,matriz_referencia_inverse)

    #InverseAddRoundKey3
    matrizNibbleSubstitionInverse2[1][0], matrizNibbleSubstitionInverse2[0][1] = matrizNibbleSubstitionInverse2[0][1], matrizNibbleSubstitionInverse2[1][0]
    InverseBinary2 = matriz_a_binario(matrizNibbleSubstitionInverse2)

    matrizAddRoundKey3Inverse = AddRoundKey(InverseBinary2,key0Bin)

    matrizAddRoundKey3Inverse[1][0], matrizAddRoundKey3Inverse[0][1] = matrizAddRoundKey3Inverse[0][1], matrizAddRoundKey3Inverse[1][0]
    def matriz_a_binario(matriz):
        # Concatenar todos los elementos de la matriz
        binario = ''.join([''.join(fila) for fila in matriz])
        return binario
    mensajeDescifrado = matriz_a_binario(matrizAddRoundKey3Inverse)

    matriz_final = [mensajeCifrado,mensajeDescifrado]
    return matriz_final


def dividir_palabra_hex(palabra):
    hex_palabra = palabra.encode().hex().upper()
    grupos = [hex_palabra[i:i + 4] for i in range(0, len(hex_palabra), 4)]
    nombres_variables = []

    numeros_agregados = 0
    grupo_con_ceros = None

    for i, grupo in enumerate(grupos):
        if len(grupo) < 4:
            ceros_faltantes = 4 - len(grupo)
            grupos[i] = grupo.ljust(4, '0')
            numeros_agregados += ceros_faltantes
            grupo_con_ceros = i + 1

        # Guardar el nombre de la variable en un arreglo
        nombres_variables.append(f'hexa{i+1}')

    return grupos, nombres_variables, numeros_agregados, grupo_con_ceros


palabraInput = input("Ingresa una palabra: ")
# Ejemplo de uso
palabra = palabraInput
grupos_hex, nombres_variables, num_agregados, grupo_ceros = dividir_palabra_hex(palabra)

print(f"La representación hexadecimal de '{palabra}' es: {palabra.encode().hex().upper()}")
#for i, grupo in enumerate(grupos_hex):
#    print(f"{nombres_variables[i]} = {grupo}")
#print(f"Números agregados = {num_agregados}")

#if grupo_ceros is not None:
#    print(f"Se agregaron ceros al {nombres_variables[grupo_ceros - 1]}")

# Guardar los hexa en un arreglo
arreglo_hexa = grupos_hex
arreglo_original = arreglo_hexa

#Generamos cadena aleatoria
cadena_aleatoria = ''.join(random.choice('01') for _ in range(8))
#Con esa cadena vamos a hacer XOR
# Aplicar la función de cifrado a cada elemento y almacenar los resultados en un nuevo arreglo
nuevo_arreglo = [proceso(elemento,key0Hex,key1Hex,key2Hex) for elemento in arreglo_original]

def binario_a_hexadecimal(arreglo_binario):
    arreglo_hexadecimal = []
    for fila in arreglo_binario:
        fila_hex = []
        for celda in fila:
            # Convierte la celda de binario a hexadecimal de cuatro bits
            hexadecimal = format(int(celda, 2), 'X').zfill(4)
            fila_hex.append(hexadecimal)
        arreglo_hexadecimal.append(fila_hex)
    return arreglo_hexadecimal


# Convertir a hexadecimal y mostrar el resultado
arreglo_hexadecimal = binario_a_hexadecimal(nuevo_arreglo)

def obtener_mensaje_cifrado(matriz):
    valores_primera_columna = ''
    for fila in matriz:
        valores_primera_columna += fila[0]  # Agregar el valor de la primera columna
    return valores_primera_columna

cadena = obtener_mensaje_cifrado(nuevo_arreglo)
print("MENSAJE CIFRADO:", cadena)


def obtener_mensaje_descifrado(matriz):
    valores_segunda_columna = ''
    for fila in matriz:
        valores_segunda_columna += fila[1]  # Agregar el valor de la segunda columna
    return valores_segunda_columna

cadena = obtener_mensaje_descifrado(nuevo_arreglo)
print("MENSAJE DESCRIFRADO:", cadena)