import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EDGE_DRIVER_PATH = "/Users/ricjimen/Downloads/edgedriver_mac64_m1/msedgedriver"
WEBPAGE_TESTED = "https://practicetestautomation.com/practice-test-login/"

@pytest.fixture(scope="function")
def driver():
    print("executing driver func")
    service = EdgeService(executable_path=EDGE_DRIVER_PATH)
    options = webdriver.EdgeOptions()
    options.add_argument("--headless")  #remove for visible browser
    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()

def test_login_success(driver):
    driver.get(WEBPAGE_TESTED)
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    WebDriverWait(driver, 10).until(EC.url_contains("logged-in-successfully"))

    assert "logged-in-successfully" in driver.current_url
    assert "Congratulations" in driver.page_source

def test_login_failure(driver):
    driver.get(WEBPAGE_TESTED)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "submit").click()

    error = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "error")))

    assert "Your username is invalid!" in error.text
