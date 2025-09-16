import pyperclip

# Lista global de historial
history = []

# Valida que el valor ingresado sea un número
def validate_input(value):
    try:
        return float(value)
    except ValueError:
        return None

# Agrega la conversión al historial
def add_to_history(conversion):
    history.append(conversion)

# Copia un texto al portapapeles
def copy_to_clipboard(text):
    pyperclip.copy(text)