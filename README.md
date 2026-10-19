# TP Integrador - QA Automation (Módulo 3)

**Alumna:** Viviana Vargas
**Curso:** Diplomatura QA Automation - Módulo 3

## Archivos

| Archivo | Qué contiene |
|---|---|
| `Punto 1.py` | Indica si un número es primo. Se repite hasta escribir `terminar`. |
| `Punto 2.py` | Calcula las raíces de una ecuación cuadrática. Se repite hasta escribir `terminar`. |
| `Test_Punto_3_Saucedemo.py` | Casos 1, 2 y 3 sobre https://www.saucedemo.com/ (Selenium) |
| `Test_Punto_3_Pokeapi.py` | Casos 1, 2 y 3 sobre https://pokeapi.co/api/v2 (requests) |
| `conftest.py` | Configuración del navegador y del reporte |
| `reporte_saucedemo.html` | Resultado de las pruebas de Saucedemo |
| `reporte_pokeapi.html` | Resultado de las pruebas de PokeAPI |

## Casos del punto 3

**Saucedemo**
1. Ordenar los productos por precio de menor a mayor y verificar el orden.
2. Agregar todos los productos al carrito y validar los errores de apellido y código postal en el checkout.
3. Agregar y quitar un producto, agregar dos y completar la compra.

**PokeAPI**
1. `berry/1`: size 20, soil_dryness 15 y firmness "soft".
2. `berry/2`: firmness "super-hard", size mayor y soil_dryness igual a berry/1.
3. `pokemon/pikachu`: experiencia base entre 10 y 1000 y tipo "electric".

## Cómo ejecutarlo

Requisitos: Python, Firefox o Chrome, y las librerías `selenium`, `pytest`, `pytest-html` y `requests`.

    pip install selenium pytest pytest-html requests

Ejercicios:

    python "Punto 1.py"
    python "Punto 2.py"

Pruebas y reportes:

    pytest Test_Punto_3_Saucedemo.py --html=reporte_saucedemo.html --self-contained-html
    pytest Test_Punto_3_Pokeapi.py --html=reporte_pokeapi.html --self-contained-html

Para usar Chrome en lugar de Firefox, agregar `--browser chrome`.
