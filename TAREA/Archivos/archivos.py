# Importa el módulo para trabajar con archivos CSV
import csv

# Importa la biblioteca principal de tkinter para la GUI
import tkinter as tk
# Importa widgets avanzados (ttk) y la clase messagebox para diálogos
from tkinter import ttk, messagebox

# Nombre del archivo CSV que vamos a procesar
archivo_csv = 'SalesJan2009.csv'

# --- Funciones de procesamiento CSV ---

def obtener_paises(archivo):
    # función que extrae países únicos
    # Crea un set vacío
    # "open" Abre el CSV en modo lectura UTF-8 como "f"
    # "csv.DictReader" Crea lector que devuelve cada fila como dict
    # Itera sobre cada fila del CSV
    # Añade el país al set
    # "sorted" devuelve la lista de países ordenada alfabéticamente
    """Retorna una lista ordenada de países únicos en el CSV."""
    paises = set()
    with open(archivo, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            paises.add(fila['Country'])
    return sorted(paises)

def obtener_metodos_pago(archivo):
    # función que extrae métodos de pago únicos
    # Crea un set vacío
    # Abre el CSV en modo lectura UTF-8 como "f"
    # Crea lector que devuelve cada fila como dict
    # Itera sobre cada fila del CSV
    # Añade el método de pago al set
    # Devuelve la lista de métodos ordenada alfabéticamente
    """Retorna una lista ordenada de métodos de pago únicos en el CSV."""
    pagos = set()
    with open(archivo, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            pagos.add(fila['Payment_Type'])
    return sorted(pagos)

def contar_compras_por_pais(archivo, pais):
    # función que cuenta cuántas compras hay de un país dado
    # Inicializa el contador en 0
    # Abre el CSV en modo lectura UTF-8 como "f"
    # Crea lector que devuelve cada fila como dict
    # Itera sobre cada fila del CSV
    # Si el campo 'Country' coincide con el país dado, incrementa el contador
    # Devuelve el total de coincidencias
    """Cuenta compras en el CSV para un país dado."""
    contador = 0
    with open(archivo, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            if fila['Country'] == pais:
                contador += 1
    return contador

def contar_compras_por_pago(archivo, metodo):
    # función que cuenta cuántas compras hay de un método de pago dado
    # Inicializa el contador en 0
    # Abre el CSV en modo lectura UTF-8 como "f"
    # Crea lector que devuelve cada fila como dict
    # Itera sobre cada fila del CSV
    # Si el campo 'Payment_Type' coincide con el método dado, incrementa el contador
    # Devuelve el total de coincidencias
    """Cuenta compras en el CSV para un método de pago dado."""
    contador = 0
    with open(archivo, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            if fila['Payment_Type'] == metodo:
                contador += 1
    return contador

# --- Funciones vinculadas a la interfaz gráfica ---

def accion_contar_por_pais():
    # obtiene el país seleccionado desde el Combobox
    # si no hay selección, muestra una advertencia y sale
    # llama a contar_compras_por_pais con el país seleccionado
    # muestra el resultado en un cuadro de información
    """Obtiene país seleccionado y muestra el conteo de compras."""
    pais = pais_var.get()
    if not pais:
        messagebox.showwarning("Atención", "Seleccione un país")
        return
    total = contar_compras_por_pais(archivo_csv, pais)
    messagebox.showinfo("Compras por país", f"Compras en {pais}: {total}")

def accion_contar_por_pago():
    # obtiene el método de pago seleccionado desde el Combobox
    # si no hay selección, muestra una advertencia y sale
    # llama a contar_compras_por_pago con el método seleccionado
    # muestra el resultado en un cuadro de información
    """Obtiene método de pago seleccionado y muestra el conteo de compras."""
    metodo = pago_var.get()
    if not metodo:
        messagebox.showwarning("Atención", "Seleccione un método de pago")
        return
    total = contar_compras_por_pago(archivo_csv, metodo)
    messagebox.showinfo("Compras por método", f"Compras con {metodo}: {total}")

# --- Configuración de la ventana principal ---

# Crea la ventana raíz de tkinter
root = tk.Tk()
# Establece el título de la ventana
root.title("Contador de Compras CSV")
# Define el tamaño inicial de la ventana (ancho x alto)
root.geometry("400x250")

# Crea variables de tipo StringVar para enlazar con los Combobox
pais_var = tk.StringVar()
pago_var = tk.StringVar()

# Sección para contar por país
# Etiqueta que indica la sección
tk.Label(root, text="Contar compras por país:").pack(pady=(10,0))
# Combobox de selección de países, valores obtenidos de la función obtener_paises
combobox_paises = ttk.Combobox(
    root,
    textvariable=pais_var,
    values=obtener_paises(archivo_csv),
    state='readonly'
)
combobox_paises.pack(pady=(0,5))
# Botón que dispara la acción de contar por país
btn_pais = tk.Button(
    root,
    text="Contar por país",
    command=accion_contar_por_pais
)
btn_pais.pack(pady=(0,10))

# Sección para contar por método de pago
# Etiqueta que indica la sección
tk.Label(root, text="Contar compras por método de pago:").pack(pady=(10,0))
# Combobox de selección de métodos de pago, valores obtenidos de la función obtener_metodos_pago
combobox_pagos = ttk.Combobox(
    root,
    textvariable=pago_var,
    values=obtener_metodos_pago(archivo_csv),
    state='readonly'
)
combobox_pagos.pack(pady=(0,5))
# Botón que dispara la acción de contar por método de pago
btn_pago = tk.Button(
    root,
    text="Contar por método",
    command=accion_contar_por_pago
)
btn_pago.pack(pady=(0,10))

# Inicia el bucle principal de eventos de la interfaz gráfica
root.mainloop()
