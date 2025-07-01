# Ejercicio de Excepciones I – capturar IndexError

# --- Ejercicio 1: Evitar acceso fuera de rango en una lista ---
def ejercicio_index_error():
    """
    Lee un índice del usuario, intenta mostrar el elemento de una lista
    y captura IndexError si el índice no existe.
    """
    lista = [1, 2, 3, 4]  # lista de ejemplo

    try:
        # Pedimos al usuario un índice
        indice_str = input("Ingrese el índice que desea consultar: ")
        # Converte la cadena a entero (puede lanzar ValueError)
        indice = int(indice_str)
        # Intenta acceder a la lista en esa posición
        valor = lista[indice]
        # Si todo va bien, imprime el valor
        print(f"El elemento en la posición {indice} es {valor}.")

    except IndexError:
        # Capturamos el caso de índice fuera de rango
        print("Intenta acceder una posición que no está en el arreglo.")

    except ValueError:
        # También captura entradas no numéricas
        print("Error: Debes ingresar un número entero como índice.")

ejercicio_index_error()
