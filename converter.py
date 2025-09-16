# converter.py

# =========================
# FUNCIONES DE CONVERSIÓN
# =========================

# LONGITUD
def meters_to_kilometers(meters):
    return meters / 1000

def kilometers_to_meters(km):
    return km * 1000

# PESO
def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(lb):
    return lb / 2.20462

# TEMPERATURA
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# VOLUMEN
def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gal):
    return gal / 0.264172

# VELOCIDAD
def kmh_to_mph(kmh):
    return kmh * 0.621371

def mph_to_kmh(mph):
    return mph / 0.621371