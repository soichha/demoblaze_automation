import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1366,768")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(5)

    driver.get("https://www.demoblaze.com/")


    try:
        driver.execute_script("window.localStorage.clear();")
    except Exception:
        pass

    yield driver
    driver.quit()