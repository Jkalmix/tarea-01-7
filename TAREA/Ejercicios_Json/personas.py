import json
# importa el módulo para trabajar con JSON

# Nombre del archivo JSON con los datos de las personas
archivo_personas = "personas.json"      

# --- Ejercicio 1: Imprimir quienes practican un deporte dado ---
def imprimir_por_deporte(archivo_json):
    """
    Abre el JSON y da una lista de los deporta.
    solicita un deporte y da una lista de quienes prectican
    el deporte ingresado.
    """
    # abre el archivo JSON en modo lectura UTF-8 como "f"
    with open(archivo_json, 'r', encoding='utf-8') as f:
    # carga todo el contenido del archivo en el diccionario "data"
        data = json.load(f)

    # extrae la lista de deportes únicos de todas las personas
    deportes_unicos = set() 
    for persona in data.values():
        # recorre cada persona en el diccionario
        for deporte in persona['deportes']:
            # recorre la lista de deportes de la persona
            deportes_unicos.add(deporte)
            # añade el deporte al set

    # muestra al usuario los deportes disponibles
    print("\n")
    print("Deportes disponibles:")

    for d in sorted(deportes_unicos):
        # ordena alfabéticamente
        print(f"- {d}") 
        # lista con guión

    # solicita al usuario el deporte a buscar
    deporte_input = input("\nIngrese un deporte de la lista anterior: ")
    # pasa la entrada a minúsculas para comparación insensible a mayúsculas
    deporte_input_lower = deporte_input.lower()

    # recorre cada persona y comprueba si practica el deporte ingresado
    for persona in data.values():
        # convierte la lista de deportes de la persona a minúsculas
        lista_lower = [d.lower() for d in persona['deportes']]
        # si el deporte ingresado (en minúsculas) está en esa lista...
        if deporte_input_lower in lista_lower:
        # imprime los nombres y apellidos concatenados
            print(f"{persona['nombres']} {persona['apellidos']}")

# --- Ejercicio 2: Imprimir quienes están en un rango de edades ---
def imprimir_por_rango_edad(archivo_json):
    """
    Abre el JSON y pide al usuario un rango de edades.
    Valida que sean números enteros y que el mínimo no supere al máximo.
    Imprime nombre y apellidos de quienes estén en ese rango.
    """
    # Abrir y cargar el JSON
    with open(archivo_json, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Bucle de validación de ingreso de rango
    while True:
        # Pedir las entradas como cadenas
        minimo_str = input("Edad mínima: ")
        maximo_str = input("Edad máxima: ")
        #  Verificar que ambas sean dígitos (números enteros no negativos)
        if not (minimo_str.isdigit() and maximo_str.isdigit()):
            print("Error: Debes ingresar números enteros. Intenta de nuevo.\n")
            continue  # vuelve a pedir los dos valores
        # Convertir a enteros
        minimo = int(minimo_str)
        maximo = int(maximo_str)
        # Comprobar que mínimo no sea mayor que máximo
        if minimo > maximo:
            print("Error: La edad mínima no puede ser mayor que la máxima. Intenta de nuevo.\n")
            continue  # vuelve a pedir el rango completo
        # Si todo está bien, salir del bucle
        break

    # Recorre los datos e imprime los que caen en el rango válido
    for clave, persona in data.items():
        edad = persona['edad']
        # extrae la edad de la persona
        if minimo <= edad <= maximo:
        # verifica si está en el rango
            print(f"{persona['nombres']} {persona['apellidos']}")




# --- Ejercicio 3: Crear JSON que agrupe IDs por deporte ---
def crear_json_deportes(archivo_json, salida_json):
    # abre el archivo JSON en modo lectura UTF-8 como "f"
    with open(archivo_json, 'r', encoding='utf-8') as f:
        # carga todo el contenido del archivo en el diccionario "data"
        data = json.load(f)
    # inicializa un diccionario vacío para agrupar IDs por deporte
    deportes_map = {}
    # recorre cada par (clave, persona) en el diccionario "data"
    for clave, persona in data.items():
        # recorre cada deporte practicado por esta persona
        for deporte in persona['deportes']:
            # si el deporte aún no tiene una lista en el mapa, créala
            if deporte not in deportes_map:
                deportes_map[deporte] = []
            # añade la clave (ID) de la persona a la lista de este deporte
            deportes_map[deporte].append(clave)
    # abre el archivo de salida en modo escritura UTF-8 como "f"
    with open(salida_json, 'w', encoding='utf-8') as f:
        # vuelca el diccionario "deportes_map" a JSON con indentación
        json.dump(deportes_map, f, ensure_ascii=False, indent=4)
    # informa al usuario que el archivo se creó correctamente
    print(f"'{salida_json}' creado correctamente con el agrupamiento por deporte.")

# --- Bloque principal: ejecutar los tres ejercicios en orden ---

    # imprime encabezado para el Ejercicio 1
print("=== Ejercicio 1: Imprimir por deporte ===")
    # llama a la función de ejercicio 1
imprimir_por_deporte(archivo_personas)

print("\n")

    # imprime encabezado para el Ejercicio 2
print("=== Ejercicio 2: Imprimir por rango de edad ===")
    # llama a la función de ejercicio 2
imprimir_por_rango_edad(archivo_personas)
print("\n")

    # imprime encabezado para el Ejercicio 3
print("=== Ejercicio 3: Crear JSON de deportes ===")
    # llama a la función de ejercicio 3 y guarda en 'deportes.json'
crear_json_deportes(archivo_personas, "deportes.json")
print("\n")
