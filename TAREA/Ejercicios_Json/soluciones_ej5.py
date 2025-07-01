# soluciones_ej5.py
# Programa para leer 'estudiantes.json', pedir un código,
# calcular su promedio de notas y guardar el resultado en 'promedio.json'.

import json                             # 1. Trabajar con JSON

def promedio_un_estudiante(archivo_entrada, archivo_salida):
    """
    Carga todo el JSON de estudiantes.
    Muestra los códigos disponibles.
    Pide al usuario elegir uno.
    Calcula el promedio de su lista 'notas'.
    Guarda {codigo: promedio} en el JSON de salida.
    """
    # Leer el archivo de entrada
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        estudiantes = json.load(f)      
        # carga dict de estudiantes

    # Mostrar códigos disponibles
    print("Códigos disponibles:")
    for codigo in estudiantes.keys():   # recorre las claves que son los códigos
        print(f"- {codigo}")

    # Pedir al usuario que seleccione uno
    codigo_sel = input("\nIngrese uno de los códigos anteriores: ")

    # Validar que exista ese código
    if codigo_sel not in estudiantes:
        print(f"Error: el código '{codigo_sel}' no está en la lista.")
        return                           # sale si no es válido

    # Extraer la lista de notas de ese estudiante
    registro = estudiantes[codigo_sel]
    lista_notas = estudiantes[codigo_sel]['notas']
    nombre_completo = f"{registro['nombres']} {registro['apellidos']}"

    # Calcular el promedio (asume al menos una nota)
    promedio = sum(lista_notas) / len(lista_notas)

    #Prepara el resultado incluyendo el nombre
    resultado = {
        codigo_sel: {
            "nombre": nombre_completo,
            "promedio": promedio
        }
    }

    # Escribir el JSON de salida
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, ensure_ascii=False, indent=4)
    print(f"\nPromedio de {codigo_sel} ({promedio:.2f}) guardado en '{archivo_salida}'.")



entrada = "estudiantes.json"         
# debe existir junto a este script
salida  = "promedio.json"            
# se creará o sobrescríbe
promedio_un_estudiante(entrada, salida)