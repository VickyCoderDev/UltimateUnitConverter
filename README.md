Ultimate Unit Converter 

¡Bienvenido a Ultimate Unit Converter!
Una aplicación en Python para convertir unidades de forma rápida, confiable y con interfaz gráfica profesional.

---

Descripción del proyecto**

Este proyecto permite convertir entre distintas unidades de:

- **Longitud**: metros ↔ kilómetros  
- **Peso**: kilogramos ↔ libras  
- **Temperatura**: Celsius ↔ Fahrenheit  
- **Volumen**: litros ↔ galones  

Además:

- Valida que los valores ingresados sean correctos.  
- Mantiene un **historial de conversiones**.  
- Permite **copiar resultados al portapapeles**.  
- Interfaz gráfica profesional usando **Tkinter**.  

Este proyecto demuestra **modularidad, buenas prácticas y tests unitarios**, ideales para mostrar en GitHub y para MIT.

---

Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/TU_USUARIO/UltimateUnitConverter.git
cd UltimateUnitConverter
2. Crear un entorno visual 
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
3. Instalar dependencias 
pip install -r requirements.txt
Las librerias que use han sido: 
tk → para la interfaz gráfica
pyperclip → para copiar al portapapeles
Para ejecutar la app debe: 
Colocar python main.py desde la terminal
Tests Unitarios: Mi proyecto incluye tests unitarios para cada una de las funciones. Para poder ejecutar tests debe: pytest tests/
Este proyecto cuenta con tests de converter.py y tambien cuenta con tests de utils.py. Este proyecto es PERSONAL, pero usted puede sugerirme mejoras via GitHub. 
