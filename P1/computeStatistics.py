"""Compute statics de un archivo de texto"""

import sys
from collections import Counter
import time

start_time = time.time()
numeros = []

# Leer el nombre del archivo del argumento de entrada
file_name = sys.argv[1]
RESULTHEADER = f"\n\nResultados del archivo {file_name}\n"


def calcular_median(numeros_median, total_de_numeros_median):
    """Funcion para calcular median"""
    numeros_median.sort()
    if total_de_numeros_median % 2 == 0:
        median1 = numeros_median[total_de_numeros_median // 2]
        median2 = numeros_median[total_de_numeros_median // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = numeros[total_de_numeros_median // 2]
    return median


def calcular_mode(numeros_mode, total_de_numeros_mode):
    """Funcion para calcular moda"""
    numeros_contados = Counter(numeros_mode)
    diccionario_numeros_contados = dict(numeros_contados)
    mayor_frecuencia = max(diccionario_numeros_contados.values())
    mode = [
        numero
        for numero, frecuencia in diccionario_numeros_contados.items()
        if frecuencia == mayor_frecuencia
    ]
    if len(mode) == total_de_numeros_mode:
        return "N/A"
    return mode


def calcular_varianza(numeros_varianza, mean, total_numeros_varianza):
    """Funcion para calcular varianza"""
    diferencia_cuadrada = [(x - mean) ** 2 for x in numeros_varianza]
    varianza = sum(diferencia_cuadrada) / (total_numeros_varianza - 1)
    return varianza


def calcular_std(numeros_std, mean, total_numeros_dtf):
    """Funcion para calcular desviacion estandar"""
    diferencia_cuadrada = [(x - mean) ** 2 for x in numeros_std]
    varianza = sum(diferencia_cuadrada) / total_numeros_dtf
    std = varianza ** 0.5
    return std


# Abrir el archivo y leer los números línea por línea
with open(file_name, encoding="utf-8") as file:
    numbers = [line.rstrip() for line in file]

# Ciclar por todas las líneas del archivo
for number in numbers:
    try:
        number = float(number)
        numeros.append(number)
    except ValueError:
        print(f"El valor {number} no es un número y se ignorará.")

# Calcular todas las métricas
TOTALNUMEROS = len(numeros)
suma_de_numeros_final = sum(numeros)
mean_final = suma_de_numeros_final / TOTALNUMEROS
median_final = calcular_median(numeros, TOTALNUMEROS)
mode_final = calcular_mode(numeros, TOTALNUMEROS)
varianza_final = calcular_varianza(numeros, mean_final, TOTALNUMEROS)
std_final = calcular_std(numeros, mean_final, TOTALNUMEROS)

RESULTSTRING = (
    f"Las estadisticas calculadas para el archivo:"
    f"{file_name} son las siguientes\n"
    f"Total de numeros: {TOTALNUMEROS}\n"
    f"Mean: {mean_final}\n"
    f"Median: {median_final}\n"
    f"Mode: {mode_final}\n"
    f"SD: {std_final}\n"
    f"Variance: {varianza_final}\n"
)

# Imprimir las métricas
print(RESULTSTRING)

execution_time = time.time() - start_time
STRINGEJECUCION = f"Tiempo de ejecucion en segundos: {execution_time}"
print(STRINGEJECUCION)

# Generar archivo de resultados
with open("StatisticsResults.txt", "a", encoding="utf-8") as file:
    file.write(
        RESULTHEADER
        + RESULTSTRING
        + STRINGEJECUCION
    )
