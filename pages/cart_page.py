from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def obtener_cantidad_carrito(self):
        badges = self.driver.find_elements(*self.BADGE_CARRITO)
        return int(badges[0].text) if badges else 0

    def remover_producto(self, nombre):
        id_boton = "remove-" + nombre.lower().replace(" ", "-")
        self.wait.until(EC.element_to_be_clickable((By.ID, id_boton))).click()
        self.wait.until(EC.invisibility_of_element_located((By.ID, id_boton)))

    def continuar_comprando(self):
        self.driver.find_element(*self.BOTON_CONTINUE_SHOPPING).click()

    def ir_al_checkout(self):
        self.driver.find_element(*self.BOTON_CHECKOUT).click()
