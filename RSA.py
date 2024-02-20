modulus = 64000

for d in range(1, modulus):
    if (7 * d) % modulus == 1:
        print(f"The modular inverse of 7 modulo 64000 is d = {d}")
        break


def calcular_claves_privadas_parejas(p, q, e):
    phi_n = (p - 1) * (q - 1)
    n = p * q

    # Calcular la primera clave privada
    d = pow(e, -1, phi_n)

    claves_privadas_parejas = [d]
    gamma = (p - 1) * (q - 1)

    # Calcular las claves privadas parejas adicionales
    for i in range(1, 5):  # Puedes ajustar el rango según tus necesidades
        d_gamma = pow(e, -1, gamma)
        d_i = d_gamma + i * gamma
        claves_privadas_parejas.append(d_i)

    return claves_privadas_parejas


# Datos dados
p = 257
q = 251
e = 7

# Calcular claves privadas parejas
claves_privadas_parejas = calcular_claves_privadas_parejas(p, q, e)

# Imprimir los resultados
for i, clave_privada in enumerate(claves_privadas_parejas):
    print(f'Clave privada pareja {i + 1}: {clave_privada}')
