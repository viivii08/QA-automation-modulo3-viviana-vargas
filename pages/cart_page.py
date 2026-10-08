from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    # Localizadores
    TITULO = (By.CLASS_NAME, "title")
    NOMBRES = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    BOTON_CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self):
        return self.wait.until(EC.visibility_of_element_located(self.TITULO)).text

    def obtener_nombres(self):
        return [e.text for e in self.driver.find_elements(*self.NOMBRES)]

    def ir_al_checkout(self):
        self.driver.find_element(*self.BOTON_CHECKOUT).click()
