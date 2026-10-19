from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:
    URL = "https://www.saucedemo.com/"

    INPUT_USUARIO = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BOTON_LOGIN = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.URL)

    def loguearse(self, usuario, password):
        self.wait.until(EC.visibility_of_element_located(self.INPUT_USUARIO)).send_keys(usuario)
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys(password)
        self.driver.find_element(*self.BOTON_LOGIN).click()


class InventoryPage:
    TITULO = (By.CLASS_NAME, "title")
    SELECT_ORDEN = (By.CLASS_NAME, "product_sort_container")
    PRECIOS = (By.CLASS_NAME, "inventory_item_price")
    NOMBRES = (By.CLASS_NAME, "inventory_item_name")
    BOTONES_AGREGAR = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    BADGE_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")
    LINK_CARRITO = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self):
        return self.wait.until(EC.visibility_of_element_located(self.TITULO)).text

    def ordenar_por(self, texto_opcion):
        select = Select(self.wait.until(EC.element_to_be_clickable(self.SELECT_ORDEN)))
        select.select_by_visible_text(texto_opcion)

    def obtener_orden_seleccionado(self):
        select = Select(self.driver.find_element(*self.SELECT_ORDEN))
        return select.first_selected_option.text

    def obtener_precios(self):
        elementos = self.driver.find_elements(*self.PRECIOS)
        return [float(e.text.replace("$", "")) for e in elementos]

    def obtener_nombres(self):
        return [e.text for e in self.driver.find_elements(*self.NOMBRES)]

    def agregar_todos_al_carrito(self):
        botones = self.driver.find_elements(*self.BOTONES_AGREGAR)
        while botones:
            botones[0].click()
            botones = self.driver.find_elements(*self.BOTONES_AGREGAR)

    def agregar_producto(self, nombre):
        id_boton = "add-to-cart-" + nombre.lower().replace(" ", "-")
        self.wait.until(EC.element_to_be_clickable((By.ID, id_boton))).click()

    def obtener_cantidad_carrito(self):
        badges = self.driver.find_elements(*self.BADGE_CARRITO)
        return int(badges[0].text) if badges else 0

    def carrito_tiene(self, cantidad):
        try:
            self.wait.until(lambda d: self.obtener_cantidad_carrito() == cantidad)
            return True
        except TimeoutException:
            return False

    def ir_al_carrito(self):
        self.driver.find_element(*self.LINK_CARRITO).click()


class CartPage:
    TITULO = (By.CLASS_NAME, "title")
    NOMBRES = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    BADGE_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")
    BOTON_CHECKOUT = (By.ID, "checkout")
    BOTON_CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self):
        return self.wait.until(EC.visibility_of_element_located(self.TITULO)).text

    def obtener_nombres(self):
        return [e.text for e in self.driver.find_elements(*self.NOMBRES)]

    def carrito_vacio(self):
        try:
            self.wait.until(lambda d: not d.find_elements(*self.BADGE_CARRITO))
            return True
        except TimeoutException:
            return False

    def remover_producto(self, nombre):
        id_boton = "remove-" + nombre.lower().replace(" ", "-")
        self.wait.until(EC.element_to_be_clickable((By.ID, id_boton))).click()
        self.wait.until(EC.invisibility_of_element_located((By.ID, id_boton)))

    def continuar_comprando(self):
        self.driver.find_element(*self.BOTON_CONTINUE_SHOPPING).click()

    def ir_al_checkout(self):
        self.driver.find_element(*self.BOTON_CHECKOUT).click()


class CheckoutPage:
    INPUT_NOMBRE = (By.ID, "first-name")
    INPUT_APELLIDO = (By.ID, "last-name")
    INPUT_CODIGO_POSTAL = (By.ID, "postal-code")
    BOTON_CONTINUE = (By.ID, "continue")
    MENSAJE_ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    TITULO = (By.CLASS_NAME, "title")
    BOTON_FINISH = (By.ID, "finish")
    MENSAJE_CONFIRMACION = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def ingresar_nombre(self, nombre):
        self.wait.until(EC.visibility_of_element_located(self.INPUT_NOMBRE)).send_keys(nombre)

    def ingresar_apellido(self, apellido):
        self.driver.find_element(*self.INPUT_APELLIDO).send_keys(apellido)

    def ingresar_codigo_postal(self, codigo):
        self.driver.find_element(*self.INPUT_CODIGO_POSTAL).send_keys(codigo)

    def continuar(self):
        self.driver.find_element(*self.BOTON_CONTINUE).click()

    def obtener_error(self):
        return self.wait.until(EC.visibility_of_element_located(self.MENSAJE_ERROR)).text

    def completar_datos(self, nombre, apellido, codigo_postal):
        self.ingresar_nombre(nombre)
        self.ingresar_apellido(apellido)
        self.ingresar_codigo_postal(codigo_postal)

    def esta_en_pantalla(self, titulo):
        try:
            self.wait.until(EC.text_to_be_present_in_element(self.TITULO, titulo))
            return True
        except TimeoutException:
            return False

    def finalizar_compra(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_FINISH)).click()

    def obtener_mensaje_confirmacion(self):
        return self.wait.until(EC.visibility_of_element_located(self.MENSAJE_CONFIRMACION)).text


def iniciar_sesion(driver):
    login = LoginPage(driver)
    login.abrir()
    login.loguearse("standard_user", "secret_sauce")
    inventario = InventoryPage(driver)
    assert inventario.obtener_titulo() == "Products", "El login fallo, no se llego a la pagina de productos"
    return inventario


def test_caso_1_ordenar_productos_por_precio_menor_a_mayor(driver):
    inventario = iniciar_sesion(driver)

    inventario.ordenar_por("Price (low to high)")
    assert inventario.obtener_orden_seleccionado() == "Price (low to high)"

    precios = inventario.obtener_precios()
    assert len(precios) > 0, "No se encontraron productos en la pagina"
    assert precios == sorted(precios), f"Los precios no estan ordenados de menor a mayor: {precios}"


def test_caso_2_checkout_valida_campos_obligatorios(driver):
    inventario = iniciar_sesion(driver)

    productos = inventario.obtener_nombres()
    inventario.agregar_todos_al_carrito()
    assert inventario.carrito_tiene(len(productos))

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


def test_caso_3_remover_producto_y_realizar_compra(driver):
    inventario = iniciar_sesion(driver)

    inventario.agregar_producto("Sauce Labs Backpack")
    assert inventario.carrito_tiene(1)

    inventario.ir_al_carrito()
    carrito = CartPage(driver)
    assert carrito.obtener_titulo() == "Your Cart"

    carrito.remover_producto("Sauce Labs Backpack")
    assert carrito.obtener_nombres() == [], "El carrito todavia tiene productos"
    assert carrito.carrito_vacio(), "El icono del carrito sigue mostrando productos"

    carrito.continuar_comprando()
    assert inventario.obtener_titulo() == "Products"

    productos = ["Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"]
    for producto in productos:
        inventario.agregar_producto(producto)
    assert inventario.carrito_tiene(2)

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
