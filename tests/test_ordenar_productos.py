from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_ordenar_productos_por_precio_menor_a_mayor(driver):
    login = LoginPage(driver)
    login.abrir()
    login.loguearse("standard_user", "secret_sauce")

    inventario = InventoryPage(driver)
    assert inventario.obtener_titulo() == "Products", "El login fallo, no se llego a la pagina de productos"

    inventario.ordenar_por("Price (low to high)")
    assert inventario.obtener_orden_seleccionado() == "Price (low to high)"

    precios = inventario.obtener_precios()
    assert len(precios) > 0, "No se encontraron productos en la pagina"
    assert precios == sorted(precios), f"Los precios no estan ordenados de menor a mayor: {precios}"
