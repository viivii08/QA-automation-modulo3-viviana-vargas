from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


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

    def ir_al_carrito(self):
        self.driver.find_element(*self.LINK_CARRITO).click()
