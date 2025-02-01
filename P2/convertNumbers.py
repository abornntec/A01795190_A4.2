"""Convertir numeros a binarios y hexadecimal"""

import sys
import time

start_time = time.time()
numeros = []
binarios = []
hexa = []
# pylint: disable-msg=C0103
resultado = ""

# Leer el nombre del archivo del argumento de entrada
file_name = sys.argv[1]
RESULTSHEADER = f"\n\nResultados del archivo {file_name}\n"


def convertir_positivo_a_binario(numero):
    """Convertir numero positivos a binario"""
    bits = []
    while numero > 0:
        bits.append(str(numero % 2))
        numero = numero // 2
    binario_convertido = ''.join(bits[::-1])
    return binario_convertido


def convertir_negativo_a_binario(numero):
    """Convertir numero negativos a binario"""
    positivo_binario = convertir_positivo_a_binario(abs(numero)).zfill(10)
    complemento_uno = ''.join(
        '1' if bit == '0' else '0' for bit in positivo_binario
    )
    complemento_dos = sumar_uno_binario(complemento_uno)
    return complemento_dos.zfill(10)


def sumar_uno_binario(binario_a_sumar):
    """Sumar unos a binario para numeros negativos"""
    binario_a_sumar = list(binario_a_sumar)
    carry = 1

    for i in range(len(binario_a_sumar) - 1, -1, -1):
        if binario_a_sumar[i] == '0':
            binario_a_sumar[i] = '1'
            carry = 0
            break
        binario_a_sumar[i] = '0'

    if carry == 1:
        binario_a_sumar.insert(0, '1')

    return ''.join(binario_a_sumar)


def convertir_a_binario(numero):
    """Convertir numero a binario"""
    if numero > 0:
        return convertir_positivo_a_binario(numero)
    if numero == 0:
        return 0
    return convertir_negativo_a_binario(numero)


def convertir_positivo_a_hexadecimal(numero):
    """Convertir numero positivo a hexadecimal"""
    bits = []
    while numero > 0:
        bit = numero % 16
        bits.append(convertir_a_hex(bit))
        numero //= 16
    hexadecimal = ''.join(bits[::-1])
    return hexadecimal


def convertir_negativo_a_hexadecimal(numero):
    """Convertir numero negativo a hexadecimal"""
    positivo_binario = convertir_positivo_a_binario(abs(numero)).zfill(40)
    complemento_uno = ''.join(
        '1' if bit == '0' else '0' for bit in positivo_binario
    )
    complemento_dos = sumar_uno_binario(complemento_uno)
    numero_decimal = int(complemento_dos, 2)
    return convertir_positivo_a_hexadecimal(numero_decimal).zfill(40 // 4)


def convertir_a_hex(valor):
    """Convertir digito a valor hexadecimal"""
    if 0 <= valor <= 9:
        return str(valor)
    return chr(ord('A') + valor - 10)


def convertir_a_hexadecimal(numero):
    """Convertir numero a hexadecimal"""
    if numero > 0:
        return convertir_positivo_a_hexadecimal(numero)
    if numero == 0:
        return 0
    return convertir_negativo_a_hexadecimal(numero)


# Abrir el archivo y leer los números línea por línea
with open(file_name, encoding="utf-8") as file:
    numbers = [line.rstrip() for line in file]

# Ciclar por todas las líneas del archivo
for number in numbers:
    try:
        number = int(number)
        numeros.append(number)
        binario = convertir_a_binario(number)
        hexa = convertir_a_hexadecimal(number)
        resultado_numero = f"{number} en binario {binario} en hexa {hexa}"
        resultado = resultado + resultado_numero + "\n"
        print(resultado_numero)
    except ValueError:
        print(f"El valor {number} no es un número y se ignorará.")

execution_time = time.time() - start_time
string_ejecucion = f"Tiempo de ejecucion en segundos: {execution_time}"
print(string_ejecucion)

# Generar archivo de resultados
with open("ConvertionResults.txt", "a", encoding="utf-8") as file:
    file.write(
        RESULTSHEADER
        + resultado
        + string_ejecucion
    )
