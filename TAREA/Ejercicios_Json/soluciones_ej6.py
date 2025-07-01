# Programa que lee 'encriptado.json', reemplaza los símbolos cifrados
# por vocales y guarda el resultado en 'desencriptado.json'.

import json
#Importa la biblioteca para manejar JSON

def desencriptar_cadenas(archivo_entrada, archivo_salida):
    """
    2. Lee un JSON con cadenas cifradas (símbolos en lugar de vocales),
    3. Desencripta cada cadena reemplazando:
       $→a, #→e, *→i, ¬→o, +→u
    4. Guarda el resultado en un nuevo JSON.
    """
    # Diccionario de mapeo símbolo→vocal
    mapa = {
        '$': 'a',  # a
        '#': 'e',  # e
        '*': 'i',  # i
        '¬': 'o',  # o
        '+': 'u'   # u
    }

    # Abrir y cargar el JSON cifrado
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        data = json.load(f)
        # 'data' es un dict con clave→texto cifrado

    # Preparar dict para guardar textos desencriptados
    resultado = {}

    # Iterar sobre cada par (clave, texto) en el JSON original
    for clave, texto in data.items():
        # Reconstruir la cadena: por cada caracter, si está en 'mapa' lo mapeamos,
        # si no, lo dejamos igual
        descifrado = ''.join(
            mapa.get(ch, ch) for ch in texto
        )
        # Guardar la cadena desencriptada bajo la misma clave
        resultado[clave] = descifrado

    # Escribir el dict con textos ya desencriptados a un nuevo archivo JSON
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, ensure_ascii=False, indent=4)

    # Informar al usuario del resultado
    print(f"Archivo '{archivo_salida}' creado con {len(resultado)} entradas desencriptadas.")

# --- Bloque principal de ejecución ---

entrada = "encriptado.json"       # Nombre del JSON de entrada
salida  = "desencriptado.json"    # Nombre del JSON de salida
desencriptar_cadenas(entrada, salida)
