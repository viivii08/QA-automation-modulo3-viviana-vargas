from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_remover_producto_y_realizar_compra(driver):
    # Paso 1: el usuario se loguea como standard_user
    login = LoginPage(driver)
    login.abrir()
    login.loguearse("standard_user", "secret_sauce")

    inventario = InventoryPage(driver)
    assert inventario.obtener_titulo() == "Products", "El login fallo, no se llego a la pagina de productos"

    # Paso 2: agregar un elemento al carrito
    inventario.agregar_producto("Sauce Labs Backpack")
    assert inventario.obtener_cantidad_carrito() == 1

    # Paso 3: ir al carrito
    inventario.ir_al_carrito()
    carrito = CartPage(driver)
    assert carrito.obtener_titulo() == "Your Cart"

    # Paso 4: remover el articulo
    carrito.remover_producto("Sauce Labs Backpack")

    # Paso 5: verificar que el sitio no tiene articulos agregados
    assert carrito.obtener_nombres() == [], "El carrito todavia tiene productos"
    assert carrito.obtener_cantidad_carrito() == 0, "El icono del carrito sigue mostrando productos"

    # Paso 6: ir a "Continue Shopping"
    carrito.continuar_comprando()
    assert inventario.obtener_titulo() == "Products"

    # Paso 7: agregar 2 elementos
    productos = ["Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"]
    for producto in productos:
        inventario.agregar_producto(producto)
    assert inventario.obtener_cantidad_carrito() == 2

    # Paso 8: ir al carrito
    inventario.ir_al_carrito()

    # Paso 9: verificar que los elementos existan
    productos_en_carrito = carrito.obtener_nombres()
    assert sorted(productos_en_carrito) == sorted(productos), (
        f"Los productos del carrito no coinciden.\nEsperados: {productos}\nEn el carrito: {productos_en_carrito}"
    )

    # Paso 10: hacer el checkout
    carrito.ir_al_checkout()
    checkout = CheckoutPage(driver)
    checkout.completar_datos("Viviana", "Vargas", "1900")
    checkout.continuar()
    assert checkout.esta_en_pantalla("Checkout: Overview"), "No se llego a la pantalla de resumen de la compra"

    # Paso 11: finalizar la compra
    checkout.finalizar_compra()

    # Paso 12: verificar que la compra fue realizada
    assert checkout.esta_en_pantalla("Checkout: Complete!"), "No se llego a la pantalla de compra finalizada"
    assert checkout.obtener_mensaje_confirmacion() == "Thank you for your order!"
