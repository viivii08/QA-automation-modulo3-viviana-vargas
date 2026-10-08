from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_valida_campos_obligatorios(driver):
    login = LoginPage(driver)
    login.abrir()
    login.loguearse("standard_user", "secret_sauce")

    inventario = InventoryPage(driver)
    assert inventario.obtener_titulo() == "Products", "El login fallo, no se llego a la pagina de productos"

    productos = inventario.obtener_nombres()
    inventario.agregar_todos_al_carrito()
    assert inventario.obtener_cantidad_carrito() == len(productos)

    inventario.ir_al_carrito()
    carrito = CartPage(driver)
    assert carrito.obtener_titulo() == "Your Cart"

    productos_en_carrito = carrito.obtener_nombres()
    assert sorted(productos_en_carrito) == sorted(productos), (
        f"Los productos del carrito no coinciden.\nEsperados: {productos}\nEn el carrito: {productos_en_carrito}"
    )

    carrito.ir_al_checkout()
    checkout = CheckoutPage(driver)

    checkout.ingresar_nombre("Viviana")
    checkout.continuar()

    assert checkout.obtener_error() == "Error: Last Name is required"

    checkout.ingresar_apellido("Vargas")
    checkout.continuar()

    assert checkout.obtener_error() == "Error: Postal Code is required"
