# Trabajo Integrador - QA Automation - Módulo 3 - Viviana Vargas

**Alumna:** Viviana Vargas
**Curso:** Diplomatura QA Automation - Módulo 3

Pruebas automatizadas de interfaz web y de API, más dos ejercicios de programación en Python.

## Tecnologías

| Herramienta | Para qué se usa |
|---|---|
| Python 3 | Lenguaje de todo el proyecto |
| Selenium | Automatizar el navegador (pruebas de UI en Saucedemo) |
| requests | Hacer las consultas a la API (pruebas de PokeAPI) |
| pytest | Organizar y ejecutar las pruebas |
| pytest-html | Generar el reporte HTML con los resultados |
| Git y GitHub | Control de versiones |

## Contenido

### Punto 1 y 2: ejercicios de Python

| Punto | Descripción | Archivo |
|---|---|---|
| 1 | Indica si un número ingresado es primo o no | `ejercicios/punto1.py` |
| 2 | Calcula las raíces de una ecuación cuadrática a partir de a, b y c | `ejercicios/punto2.py` |

Los dos programas muestran un mensaje de bienvenida, se repiten hasta que el usuario escribe `terminar` y validan los datos ingresados (por ejemplo, si se escriben letras en lugar de números).

### Punto 3: pruebas automatizadas

**Saucedemo (UI)** - https://www.saucedemo.com/

| Caso | Qué verifica | Archivo |
|---|---|---|
| 1 | Login con `standard_user`, ordenar por "Price (low to high)" y comprobar que los precios queden de menor a mayor | `tests/test_ordenar_productos.py` |
| 2 | Agregar todos los productos al carrito, verificar que estén todos y validar los errores "Last Name is required" y "Postal Code is required" en el checkout | `tests/test_checkout.py` |
| 3 | Agregar y quitar un producto, verificar el carrito vacío, agregar 2 productos y completar la compra | `tests/test_compra.py` |

**PokeAPI (API)** - https://pokeapi.co/api/v2

| Caso | Qué verifica | Archivo |
|---|---|---|
| 1 | `berry/1`: size 20, soil_dryness 15 y firmness "soft" | `tests/test_pokeapi.py` |
| 2 | `berry/2`: firmness "super-hard", size mayor y soil_dryness igual a berry/1 | `tests/test_pokeapi.py` |
| 3 | `pokemon/pikachu`: experiencia base entre 10 y 1000 y tipo "electric" | `tests/test_pokeapi.py` |

## Estructura del proyecto

    ejercicios/       Puntos 1 y 2
    pages/            Page Objects: una clase por pantalla de Saucedemo
    tests/            Casos de prueba de UI y de API
    reports/          Reporte HTML de la última ejecución
    conftest.py       Configuración del navegador y del reporte
    pytest.ini        Configuración de pytest
    requirements.txt  Librerías necesarias

Las pruebas de Saucedemo usan el patrón **Page Object Model**: cada pantalla (login, productos, carrito y checkout) tiene su propia clase con sus localizadores y acciones, y los tests solo describen los pasos.

## Instalación

Requisitos: Python 3, Git y Firefox (o Chrome).

**Linux**

    git clone https://github.com/viivii08/QA-automation-modulo3-viviana-vargas.git
    cd QA-automation-modulo3-viviana-vargas
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

**Windows (PowerShell)**

    git clone https://github.com/viivii08/QA-automation-modulo3-viviana-vargas.git
    cd QA-automation-modulo3-viviana-vargas
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt

## Ejecución

**Pruebas automatizadas**

    pytest                      Todas las pruebas, con Firefox
    pytest --browser chrome     Con Chrome
    pytest --headless           Sin abrir la ventana del navegador
    pytest tests/test_pokeapi.py   Solo las pruebas de API

Al terminar, el reporte queda en `reports/reporte.html`. Si una prueba de UI falla, el reporte incluye una captura de pantalla del momento del error.

**Ejercicios** (en Windows se usa `python` en lugar de `python3`)

    python3 ejercicios/punto1.py
    python3 ejercicios/punto2.py
