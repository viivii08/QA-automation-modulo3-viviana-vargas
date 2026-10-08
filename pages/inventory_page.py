from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    # Localizadores
    TITULO = (By.CLASS_NAME, "title")
    SELECT_ORDEN = (By.CLASS_NAME, "product_sort_container")
    PRECIOS = (By.CLASS_NAME, "inventory_item_price")

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
        # Los precios vienen como texto "$7.99", se saca el $ y se pasan a numero
        elementos = self.driver.find_elements(*self.PRECIOS)
        return [float(e.text.replace("$", "")) for e in elementos]
