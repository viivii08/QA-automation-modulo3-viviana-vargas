from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    # Localizadores
    INPUT_NOMBRE = (By.ID, "first-name")
    INPUT_APELLIDO = (By.ID, "last-name")
    INPUT_CODIGO_POSTAL = (By.ID, "postal-code")
    BOTON_CONTINUE = (By.ID, "continue")
    MENSAJE_ERROR = (By.CSS_SELECTOR, "[data-test='error']")

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
