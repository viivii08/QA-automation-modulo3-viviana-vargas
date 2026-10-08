from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_valida_campos_obligatorios(driver):
    # Paso 1: el usuario se loguea como standard_user
    login = LoginPage(driver)
    login.abrir()
    login.loguearse("standard_user", "secret_sauce")

    inventario = InventoryPage(driver)
    assert inventario.obtener_titulo() == "Products", "El login fallo, no se llego a la pagina de productos"

    # Paso 2: incorporar al carrito todos los elementos
    productos = inventario.obtener_nombres()
    inventario.agregar_todos_al_carrito()
    assert inventario.obtener_cantidad_carrito() == len(productos)

    # Paso 3: ir al carrito
    inventario.ir_al_carrito()
    carrito = CartPage(driver)
    assert carrito.obtener_titulo() == "Your Cart"

    # Paso 4: verificar que todos los elementos esten en el carrito
    productos_en_carrito = carrito.obtener_nombres()
    assert sorted(productos_en_carrito) == sorted(productos), (
        f"Los productos del carrito no coinciden.\nEsperados: {productos}\nEn el carrito: {productos_en_carrito}"
    )

    # Paso 5: ir al checkout
    carrito.ir_al_checkout()
    checkout = CheckoutPage(driver)

    # Paso 6: ingresar nombre y clickear "Continue"
    checkout.ingresar_nombre("Viviana")
    checkout.continuar()

    # Paso 7: verificar el error de apellido obligatorio
    assert checkout.obtener_error() == "Error: Last Name is required"

    # Paso 8: ingresar apellido y clickear "Continue"
    checkout.ingresar_apellido("Vargas")
    checkout.continuar()

    # Paso 9: verificar el error de codigo postal obligatorio
    assert checkout.obtener_error() == "Error: Postal Code is required"
