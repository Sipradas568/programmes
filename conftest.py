import pytest
#import configs
import time
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as Chromeservice
from selenium.webdriver.edge.service import Service as Edgeservice
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "chrome")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture

def setup(browser):
    if browser == "chrome":
        service = Chromeservice(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window
  
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    if rep.when in ("setup","call") and rep.failed:
        driver = item.funcargs.get("driver",None)

        if driver:
            screenshot_name = f"screenshots/{item.name}.png"
            driver.save_screeshot(screenshot_name)
            print("screenshot saved  {screenshot_name}")
    
   

    
