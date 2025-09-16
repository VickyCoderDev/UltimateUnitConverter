import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import validate_input, add_to_history, copy_to_clipboard, history

# ---------------- VALIDAR INPUT ----------------
def test_validate_input_valid_number():
    assert validate_input("25") == 25.0
    assert validate_input("3.1415") == 3.1415
    assert validate_input("-10") == -10.0

def test_validate_input_invalid_number():
    assert validate_input("abc") is None
    assert validate_input("") is None
    assert validate_input("25a") is None

# ---------------- HISTORIAL ----------------
def test_add_to_history():
    history.clear()  # Limpiar historial antes de test
    add_to_history("25 * 2 = 50")
    add_to_history("10 m -> 0.01 km")
    assert len(history) == 2
    assert history[0] == "25 * 2 = 50"
    assert history[1] == "10 m -> 0.01 km"

# ---------------- PORTAPAPELES ----------------
def test_copy_to_clipboard():
    copy_to_clipboard("Test Clipboard")
    import pyperclip
    assert pyperclip.paste() == "Test Clipboard"