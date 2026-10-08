import pytest
import pytest_html
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox", help="Navegador: firefox o chrome")
    parser.addoption("--headless", action="store_true", help="Ejecutar sin abrir la ventana del navegador")


@pytest.fixture
def driver(request):
    navegador = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if navegador == "chrome":
        opciones = webdriver.ChromeOptions()
        if headless:
            opciones.add_argument("--headless=new")
        driver = webdriver.Chrome(options=opciones)
    else:
        opciones = webdriver.FirefoxOptions()
        if headless:
            opciones.add_argument("--headless")
        driver = webdriver.Firefox(options=opciones)

    driver.maximize_window()
    yield driver
    driver.quit()


# Si un test falla, se saca una captura de pantalla y se agrega al reporte HTML
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    reporte = outcome.get_result()
    extras = getattr(reporte, "extras", [])

    if reporte.when == "call" and reporte.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            captura = driver.get_screenshot_as_base64()
            extras.append(pytest_html.extras.image(captura, "Captura del error"))

    reporte.extras = extras


def pytest_html_report_title(report):
    report.title = "Reporte de ejecucion - Saucedemo"
