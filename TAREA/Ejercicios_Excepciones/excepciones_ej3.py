# Captura KeyError al intentar acceder a una llave inexistente en un diccionario

# --- Función principal que maneja el acceso al diccionario ---
def main():
    """
    1. Define un diccionario de ejemplo.
    2. Muestra las llaves disponibles.
    3. Pide al usuario que ingrese una llave.
    4. Intenta obtener el valor; si la llave no existe, captura KeyError.
    """
    # Diccionario de ejemplo: nombre → lenguaje favorito
    lenguajes = {
        'James':   'Java',
        'Dennis':  'C',
        'Das':     'Python'
    }

    # Mostrar al usuario las llaves disponibles
    print("Llaves disponibles en el diccionario:")
    for llave in lenguajes.keys():
        print(f"- {llave}")

    # Pedir al usuario la llave que quiere consultar
    llave_input = input("\nIngrese una de las llaves anteriores: ")

    try:
        # Intentar acceder al valor asociado a la llave
        valor = lenguajes[llave_input]
        # Si existe, imprimir el resultado
        print(f"El lenguaje de {llave_input} es {valor}.")

    except KeyError:
        # Si la llave no está definida en el diccionario, mostrar mensaje de error
        print("Intenta acceder una llave que no está en el diccionario.")

main()
