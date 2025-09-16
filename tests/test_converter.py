import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar todas las funciones de converter.py
from converter import meters_to_kilometers, kilometers_to_meters
from converter import kilograms_to_pounds, pounds_to_kilograms
from converter import celsius_to_fahrenheit, fahrenheit_to_celsius
from converter import liters_to_gallons, gallons_to_liters

# --------- LONGITUD ---------
def test_meters_to_kilometers():
    assert meters_to_kilometers(1000) == 1
    assert meters_to_kilometers(500) == 0.5

def test_kilometers_to_meters():
    assert kilometers_to_meters(1) == 1000
    assert kilometers_to_meters(0.5) == 500

# --------- PESO ---------
def test_kilograms_to_pounds():
    assert round(kilograms_to_pounds(1), 5) == 2.20462
    assert round(kilograms_to_pounds(0), 5) == 0

def test_pounds_to_kilograms():
    assert round(pounds_to_kilograms(2.20462), 5) == 1
    assert pounds_to_kilograms(0) == 0

# --------- TEMPERATURA ---------
def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100

# --------- VOLUMEN ---------
def test_liters_to_gallons():
    assert round(liters_to_gallons(1), 5) == 0.26417
    assert liters_to_gallons(0) == 0

def test_gallons_to_liters():
    assert round(gallons_to_liters(0.264172), 5) == 1
    assert gallons_to_liters(0) == 0  