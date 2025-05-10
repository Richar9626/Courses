import subprocess
try:
    from selenium import webdriver
    print("Module slenium is already installed.")
except ImportError:
    print("Module slenium is not installed. Attempting to install...")

    # Use pip to install the module
    try:
        subprocess.check_call(['pip', 'install', 'selenium'])
        print("Module selenium has been successfully installed.")
    except subprocess.CalledProcessError:
        print("Failed to install module selenium. Please install it manually.")

try:
    from webdriver_manager.chrome import ChromeDriverManager
    print("Module webdriver-manager is already installed.")
except ImportError:
    print("Module webdriver-manager is not installed. Attempting to install...")

    # Use pip to install the module
    try:
        subprocess.check_call(['pip', 'install', 'webdriver-manager'])
        print("Module webdriver-manager has been successfully installed.")
    except subprocess.CalledProcessError:
        print("Failed to install module webdriver-manager. Please install it manually.")

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

file_name = 'chromedriver-win64.zip'
url = 'https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/win64/chromedriver-win64.zip'
subprocess.call(['curl','-o' , file_name, url])
subprocess.call(['powershell','Expand-Archive' ,'-Path', file_name])

#service = Service(executable_path="chromedriver.exe")
options = Options()
options.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

# Open a webpage
driver.get('https://practicetestautomation.com/practice-test-login/')

# Find an input field by its name and fill it out
input_field = driver.find_element_by_name('username')
input_field.send_keys('student')

# Find an input field by its name and fill it out
input_field = driver.find_element_by_name('password')
input_field.send_keys('Password123')

# Find an element by its ID and click it
element = driver.find_element_by_id('login')
element.click()
