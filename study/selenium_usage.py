from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EDGE_DRIVER_PATH = "/Users/ricjimen/Downloads/edgedriver_mac64_m1/msedgedriver"  

service = EdgeService(executable_path=EDGE_DRIVER_PATH)
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)

try:
    driver.get("https://practicetestautomation.com/practice-test-login/")f


    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    input("✅ Login submitted. Press Enter to close the browser...")

finally:
    driver.quit()
