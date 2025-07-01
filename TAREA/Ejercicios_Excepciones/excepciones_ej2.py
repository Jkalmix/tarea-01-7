# Captura TypeError al intentar sumar un número con una cadena

# --- Función que intenta operar a + b ---
def operar(a, b):
    """
    Intenta devolver la suma de a y b.
    Si los tipos no son compatibles, propagará TypeError.
    """
    return a + b  # puede lanzar TypeError si b no es numérico

# --- Función principal que maneja inputs y excepciones ---
def main():
    """
    Lee un entero desde la entrada, define una cadena fija,
    y llama a operar. Captura TypeError y muestra un mensaje.
    """
    try:
        # Solicita al usuario un número entero
        a = int(input("Ingrese un número entero: "))
        # Define b como una cadena (caso de error intencional)
        b = "hola"
        # Intenta sumar a + b
        resultado = operar(a, b)
    except TypeError:
        # Si ocurre TypeError (no se puede sumar int + str),
        #    lo capturamos y mostramos el mensaje indicado
        print("Los tipos de datos no cuadran para hacer la operación.")
    else:
        # Si no hubo excepción, imprimimos el resultado
        print(f"Resultado de la operación: {resultado}")


main()
