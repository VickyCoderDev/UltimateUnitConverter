# gui.py
import tkinter as tk
from tkinter import ttk
from converter import (
    meters_to_kilometers, kilometers_to_meters,
    kilograms_to_pounds, pounds_to_kilograms,
    celsius_to_fahrenheit, fahrenheit_to_celsius,
    liters_to_gallons, gallons_to_liters
)
from utils import validate_input, add_to_history, copy_to_clipboard

# -------------------------------
# FUNCIONES DE CONVERSIÓN CON ANIMACIÓN
# -------------------------------

def convert_length():
    value = validate_input(length_entry.get())
    if value is None:
        length_result.config(text="¡Ingresa un número válido!", fg="red")
        return
    if length_option.get() == "m → km":
        resultado = meters_to_kilometers(value)
        texto = f"{value} m → {resultado} km"
    else:
        resultado = kilometers_to_meters(value)
        texto = f"{value} km → {resultado} m"
    length_result.config(text=texto, fg="green")
    root.after(500, lambda: length_result.config(fg="black"))
    add_to_history(texto)

def convert_weight():
    value = validate_input(weight_entry.get())
    if value is None:
        weight_result.config(text="¡Ingresa un número válido!", fg="red")
        return
    if weight_option.get() == "kg → lbs":
        resultado = kilograms_to_pounds(value)
        texto = f"{value} kg → {resultado} lbs"
    else:
        resultado = pounds_to_kilograms(value)
        texto = f"{value} lbs → {resultado} kg"
    weight_result.config(text=texto, fg="green")
    root.after(500, lambda: weight_result.config(fg="black"))
    add_to_history(texto)

def convert_temp():
    value = validate_input(temp_entry.get())
    if value is None:
        temp_result.config(text="¡Ingresa un número válido!", fg="red")
        return
    if temp_option.get() == "°C → °F":
        resultado = celsius_to_fahrenheit(value)
        texto = f"{value} °C → {resultado} °F"
    else:
        resultado = fahrenheit_to_celsius(value)
        texto = f"{value} °F → {resultado} °C"
    temp_result.config(text=texto, fg="green")
    root.after(500, lambda: temp_result.config(fg="black"))
    add_to_history(texto)

def convert_volume():
    value = validate_input(volume_entry.get())
    if value is None:
        volume_result.config(text="¡Ingresa un número válido!", fg="red")
        return
    if volume_option.get() == "L → gal":
        resultado = liters_to_gallons(value)
        texto = f"{value} L → {resultado} gal"
    else:
        resultado = gallons_to_liters(value)
        texto = f"{value} gal → {resultado} L"
    volume_result.config(text=texto, fg="green")
    root.after(500, lambda: volume_result.config(fg="black"))
    add_to_history(texto)

# -------------------------------
# HISTORIAL
# -------------------------------
def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Historial")
    for item in add_to_history.history:
        tk.Label(history_window, text=item).pack()
    # Botón para guardar historial en archivo
    tk.Button(history_window, text="Guardar historial",
              command=lambda: save_history_to_file()).pack(pady=5)

def save_history_to_file(filename="historial.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for item in add_to_history.history:
            f.write(item + "\n")

# -------------------------------
# TEMA OSCURO / CLARO
# -------------------------------
current_theme = "light"
def toggle_theme():
    global current_theme
    if current_theme == "light":
        root.config(bg="black")
        for widget in root.winfo_children():
            try:
                widget.config(bg="black", fg="white")
            except:
                pass
        current_theme = "dark"
    else:
        root.config(bg="white")
        for widget in root.winfo_children():
            try:
                widget.config(bg="white", fg="black")
            except:
                pass
        current_theme = "light"

# -------------------------------
# VENTANA PRINCIPAL
# -------------------------------
root = tk.Tk()
root.title("Ultimate Unit Converter")
root.geometry("500x500")

# Botón tema
tk.Button(root, text="Cambiar tema", command=toggle_theme).pack(pady=5)

# -------------------------------
# NOTEBOOK / PESTAÑAS
# -------------------------------
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# --------- PESTAÑA LONGITUD ---------
tab_length = tk.Frame(notebook)
notebook.add(tab_length, text="Longitud")
length_option = tk.StringVar(value="m → km")
tk.Label(tab_length, text="Conversión de longitud").pack()
ttk.Combobox(tab_length, textvariable=length_option, values=["m → km", "km → m"]).pack(pady=2)
length_entry = tk.Entry(tab_length)
length_entry.pack()
tk.Button(tab_length, text="Convertir", command=convert_length).pack()
length_result = tk.Label(tab_length, text="")
length_result.pack()
tk.Button(tab_length, text="Copiar resultado",
          command=lambda: copy_to_clipboard(length_result.cget("text"))).pack()

# --------- PESTAÑA PESO ---------
tab_weight = tk.Frame(notebook)
notebook.add(tab_weight, text="Peso")
weight_option = tk.StringVar(value="kg → lbs")
tk.Label(tab_weight, text="Conversión de peso").pack()
ttk.Combobox(tab_weight, textvariable=weight_option, values=["kg → lbs", "lbs → kg"]).pack(pady=2)
weight_entry = tk.Entry(tab_weight)
weight_entry.pack()
tk.Button(tab_weight, text="Convertir", command=convert_weight).pack()
weight_result = tk.Label(tab_weight, text="")
weight_result.pack()
tk.Button(tab_weight, text="Copiar resultado",
          command=lambda: copy_to_clipboard(weight_result.cget("text"))).pack()

# --------- PESTAÑA TEMPERATURA ---------
tab_temp = tk.Frame(notebook)
notebook.add(tab_temp, text="Temperatura")
temp_option = tk.StringVar(value="°C → °F")
tk.Label(tab_temp, text="Conversión de temperatura").pack()
ttk.Combobox(tab_temp, textvariable=temp_option, values=["°C → °F", "°F → °C"]).pack(pady=2)
temp_entry = tk.Entry(tab_temp)
temp_entry.pack()
tk.Button(tab_temp, text="Convertir", command=convert_temp).pack()
temp_result = tk.Label(tab_temp, text="")
temp_result.pack()
tk.Button(tab_temp, text="Copiar resultado",
          command=lambda: copy_to_clipboard(temp_result.cget("text"))).pack()

# --------- PESTAÑA VOLUMEN ---------
tab_volume = tk.Frame(notebook)
notebook.add(tab_volume, text="Volumen")
volume_option = tk.StringVar(value="L → gal")
tk.Label(tab_volume, text="Conversión de volumen").pack()
ttk.Combobox(tab_volume, textvariable=volume_option, values=["L → gal", "gal → L"]).pack(pady=2)
volume_entry = tk.Entry(tab_volume)
volume_entry.pack()
tk.Button(tab_volume, text="Convertir", command=convert_volume).pack()
volume_result = tk.Label(tab_volume, text="")
volume_result.pack()
tk.Button(tab_volume, text="Copiar resultado",
          command=lambda: copy_to_clipboard(volume_result.cget("text"))).pack()

# --------- BOTÓN HISTORIAL ---------
tk.Button(root, text="Ver Historial", command=show_history).pack(pady=5)

# -------------------------------
# EJECUTAR VENTANA
# -------------------------------
root.mainloop()