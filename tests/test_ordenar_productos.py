from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_ordenar_productos_por_precio_menor_a_mayor(driver):
    # Paso 1: el usuario se loguea como standard_user
    login = LoginPage(driver)
    login.abrir()
    login.loguearse("standard_user", "secret_sauce")

    inventario = InventoryPage(driver)
    assert inventario.obtener_titulo() == "Products", "El login fallo, no se llego a la pagina de productos"

    # Paso 2: ordenar los elementos por "Price (low to high)"
    inventario.ordenar_por("Price (low to high)")
    assert inventario.obtener_orden_seleccionado() == "Price (low to high)"

    # Paso 3: verificar que los elementos esten ordenados
    precios = inventario.obtener_precios()
    assert len(precios) > 0, "No se encontraron productos en la pagina"
    assert precios == sorted(precios), f"Los precios no estan ordenados de menor a mayor: {precios}"
