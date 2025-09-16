from utils import validate_input, add_to_history, copy_to_clipboard, history

valor = validate_input("25")
if valor is not None:
    resultado = valor * 2
    add_to_history(f"{valor} * 2 = {resultado}")
    copy_to_clipboard(str(resultado))
    print("Resultado:", resultado)
    print("Historial:", history)
else:
    print("El valor ingresado no es válido")