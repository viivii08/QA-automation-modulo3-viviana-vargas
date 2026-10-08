# Automatización Saucedemo - Trabajo Integrador Módulo 3

Pruebas automatizadas sobre https://www.saucedemo.com/ con Selenium, Python y pytest.

## Casos automatizados

| Caso | Descripción | Archivo |
|---|---|---|
| Caso 1 | Login con `standard_user`, ordenar por "Price (low to high)" y verificar el orden | `tests/test_ordenar_productos.py` |
| Caso 2 | Login, agregar todos los productos al carrito, verificar el carrito y validar los errores de apellido y código postal obligatorios en el checkout | `tests/test_checkout.py` |
| Caso 3 | Login, agregar y remover un producto, verificar el carrito vacío, agregar 2 productos y completar la compra | `tests/test_compra.py` |

## Estructura

```
saucedemo-automation/
├── pages/                  # Page Objects (una clase por pantalla)
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/                  # Casos de prueba
│   ├── test_ordenar_productos.py
│   ├── test_checkout.py
│   └── test_compra.py
├── reports/                # Reporte HTML generado
├── conftest.py             # Configuración del navegador y del reporte
├── pytest.ini
└── requirements.txt
```

## Instalación

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

```bash
pytest                      # Firefox (por defecto)
pytest --browser chrome     # Chrome
pytest --headless           # Sin abrir la ventana del navegador
```

Al terminar, el reporte queda en `reports/reporte.html`. Si un test falla, el reporte incluye una captura de pantalla del momento del error.
