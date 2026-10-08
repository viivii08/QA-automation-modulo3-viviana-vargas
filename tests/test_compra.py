from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_remover_producto_y_realizar_compra(driver):
    login = LoginPage(driver)
    login.abrir()
    login.loguearse("standard_user", "secret_sauce")

    inventario = InventoryPage(driver)
    assert inventario.obtener_titulo() == "Products", "El login fallo, no se llego a la pagina de productos"

    inventario.agregar_producto("Sauce Labs Backpack")
    assert inventario.obtener_cantidad_carrito() == 1

    inventario.ir_al_carrito()
    carrito = CartPage(driver)
    assert carrito.obtener_titulo() == "Your Cart"

    carrito.remover_producto("Sauce Labs Backpack")

    assert carrito.obtener_nombres() == [], "El carrito todavia tiene productos"
    assert carrito.obtener_cantidad_carrito() == 0, "El icono del carrito sigue mostrando productos"

    carrito.continuar_comprando()
    assert inventario.obtener_titulo() == "Products"

    productos = ["Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"]
    for producto in productos:
        inventario.agregar_producto(producto)
    assert inventario.obtener_cantidad_carrito() == 2

    inventario.ir_al_carrito()

    productos_en_carrito = carrito.obtener_nombres()
    assert sorted(productos_en_carrito) == sorted(productos), (
        f"Los productos del carrito no coinciden.\nEsperados: {productos}\nEn el carrito: {productos_en_carrito}"
    )

    carrito.ir_al_checkout()
    checkout = CheckoutPage(driver)
    checkout.completar_datos("Viviana", "Vargas", "1900")
    checkout.continuar()
    assert checkout.esta_en_pantalla("Checkout: Overview"), "No se llego a la pantalla de resumen de la compra"

    checkout.finalizar_compra()

    assert checkout.esta_en_pantalla("Checkout: Complete!"), "No se llego a la pantalla de compra finalizada"
    assert checkout.obtener_mensaje_confirmacion() == "Thank you for your order!"
