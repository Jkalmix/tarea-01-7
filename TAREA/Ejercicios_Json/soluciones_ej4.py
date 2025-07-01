# Código para el Ejercicio 4: leer dos archivos JSON y generar un tercero
# con las entradas (clave:valor) que sean exactamente iguales en ambos.

import json  # Importa el módulo para trabajar con JSON

def coincidencias_entre_jsons(archivo1, archivo2, salida_json):
    """
    Lee dos archivos JSON, encuentra las claves cuyo valor
    complete coincida en ambos, y guarda esas coincidencias
    en un nuevo archivo JSON.
    """
    # Abre y carga el primer JSON en el diccionario data1
    with open(archivo1, 'r', encoding='utf-8') as f1:
        data1 = json.load(f1)
    # Abre y carga el segundo JSON en el diccionario data2
    with open(archivo2, 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)

    # Inicializa un diccionario vacío para almacenar coincidencias
    comunes = {}

    # Itera sobre la intersección de claves de ambos diccionarios
    for clave in data1.keys() & data2.keys():
        # Comprueba si los valores para esa clave son exactamente iguales
        if data1[clave] == data2[clave]:
            # Si coinciden, añade la entrada al diccionario comunes
            comunes[clave] = data1[clave]

    # Abre el archivo de salida en modo escritura UTF-8
    with open(salida_json, 'w', encoding='utf-8') as fout:
        # Vuelca el diccionario comunes a JSON con indentación
        json.dump(comunes, fout, ensure_ascii=False, indent=4)

    # Informa al usuario del resultado
    print(f"'{salida_json}' creado con {len(comunes)} coincidencia(s).")


    # Define aquí los dos archivos de entrada y el de salida
archivo1 = "personas.json"         # primer JSON con datos de personas
archivo2 = "personas2.json" # segundo JSON con más registros
salida   = "coincidencias.json"    # archivo donde guardaremos las coincidencias

    # Llama a la función para generar el archivo de coincidencias
coincidencias_entre_jsons(archivo1, archivo2, salida)