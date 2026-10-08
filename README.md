# Trabajo Integrador - Módulo 3

Pruebas automatizadas con Python y pytest:
- **UI** sobre https://www.saucedemo.com/ con Selenium.
- **API** sobre https://pokeapi.co/api/v2 con requests.

## Casos automatizados

### Saucedemo (UI)

| Caso | Descripción | Archivo |
|---|---|---|
| Caso 1 | Login con `standard_user`, ordenar por "Price (low to high)" y verificar el orden | `tests/test_ordenar_productos.py` |
| Caso 2 | Agregar todos los productos al carrito, verificarlos y validar los errores de apellido y código postal en el checkout | `tests/test_checkout.py` |
| Caso 3 | Agregar y remover un producto, verificar el carrito vacío, agregar 2 productos y completar la compra | `tests/test_compra.py` |

### PokeAPI (API)

| Caso | Descripción | Archivo |
|---|---|---|
| Caso 1 | GET a `berry/1`: size 20, soil_dryness 15 y firmness "soft" | `tests/test_pokeapi.py` |
| Caso 2 | GET a `berry/2`: firmness "super-hard", size mayor y soil_dryness igual a berry/1 | `tests/test_pokeapi.py` |
| Caso 3 | GET a `pokemon/pikachu`: experiencia base entre 10 y 1000 y tipo "electric" | `tests/test_pokeapi.py` |

## Estructura

- `pages/`: Page Objects de saucedemo (login, inventario, carrito y checkout)
- `tests/`: casos de prueba de UI y de API
- `reports/`: reporte HTML generado
- `conftest.py`: configuración del navegador y del reporte
- `pytest.ini`: configuración de pytest
- `requirements.txt`: librerías necesarias

## Instalación

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Ejecución

    pytest                      # Firefox (por defecto)
    pytest --browser chrome     # Chrome
    pytest --headless           # Sin abrir la ventana del navegador

Al terminar, el reporte queda en `reports/reporte.html`. Si un test de UI falla, el reporte incluye una captura de pantalla del momento del error.

## Ejercicios de Python

| Punto | Descripción | Archivo |
|---|---|---|
| Punto 1 | Dado un número, indica si es primo o no | `ejercicios/punto1.py` |
| Punto 2 | Dados a, b y c, calcula las raíces de una ecuación cuadrática | `ejercicios/punto2.py` |

Para ejecutarlos:

    python3 ejercicios/punto1.py
    python3 ejercicios/punto2.py
