"""Contar palabras de un archivo de texto"""

import sys
import time

start_time = time.time()
diccionario_frecuencia = {}
# pylint: disable-msg=C0103
total_palabras = 0
# pylint: disable-msg=C0103
respuesta = ""

# Leer el nombre del archivo del argumento de entrada
FILENAME = sys.argv[1]
RESULTHEADER = f"\n\nResultados del archivo {FILENAME}\n"

with open(FILENAME, encoding="utf-8") as file:
    for line in file:
        palabras_en_linea = line.split()
        for palabra in palabras_en_linea:
            if palabra not in diccionario_frecuencia:
                diccionario_frecuencia[palabra] = 1
            else:
                diccionario_frecuencia[palabra] += 1
        total_palabras += len(palabras_en_linea)
        total_palabras_string = f"Total de palabras {total_palabras}\n"

for palabra, frecuencia in diccionario_frecuencia.items():
    respuesta_parcial = f"{palabra} {frecuencia}"
    print(respuesta_parcial)
    respuesta = respuesta + respuesta_parcial + "\n"

execution_time = time.time() - start_time
string_ejecucion = f"Tiempo de ejecucion en segundos: {execution_time}"
print(string_ejecucion)
print(total_palabras_string)

# Generar archivo de resultados
with open("WordCountResults.txt", "a", encoding="utf-8") as file:
    file.write(
        RESULTHEADER
        + respuesta
        + total_palabras_string
        + string_ejecucion
    )
