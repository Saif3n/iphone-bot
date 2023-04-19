from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time

print("iPhone Automation Purchase Script")
print("==========================================================================================================================================")
print("Thanks for using this iPhone bot script. Please ensure that the details requested are correct, as they will be used in your order summary.")
print("\n Please note that no information is stored at all. The questions are only so that the order can be palced on your behalf.")
print("==========================================================================================================================================")

input_dict = {}

town = input("Enter your town/city (this must be exact for the script to work!): ")
postcode = input("Enter your postcode: ")

input_dict['First Name'] = input("Enter your first name: ")
input_dict['Last Name'] = input("Enter your last name: ")
input_dict['Street Address'] = input("Enter your street address (please note that this MUST be accurate, example format: 11 Symonds Street): ")
input_dict['Additional Address Info (optional)'] = input("(Optional) Additional address info: ")
input_dict['Suburb/Town (optional)'] = input("(Optional) Suburb/Town: ")
input_dict['Email'] = input("Email: ")
input_dict['Mobile Phone Number'] = input("Mobile Phone Number: ")

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.apple.com/nz/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

def retry_click(new):
    element = wait.until(new)

    try:
        element.click()
    except StaleElementReferenceException:
        # Re-try the operation after a small delay
        time.sleep(1)
        print('----')
        retry_click(new)


link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'iphone_14')]")))
link.click()

retry_click(EC.element_to_be_clickable((By.XPATH, "//label[.//span[@class='form-selector-title' and contains(text(), 'iPhone 14 Pro')]]")))

retry_click(EC.element_to_be_clickable((By.CLASS_NAME, "colornav-item")))

retry_click(EC.element_to_be_clickable((By.XPATH, "//label[.//span[@class='form-selector-title' and contains(text(), '128')]]")))

retry_click(EC.element_to_be_clickable((By.XPATH, "//label[.//span[@class='form-selector-title' and contains(text(), 'No AppleCare+ coverage')]]")))

retry_click(EC.element_to_be_clickable((By.XPATH, "//span[.//button[@class='button button-block']]")))

retry_click(EC.element_to_be_clickable((By.XPATH, "//button[@class='button button-block button-super' and @title='Review Bag']")))

retry_click(EC.element_to_be_clickable((By.XPATH, "//button[@id='shoppingCart.actions.navCheckout']")))

retry_click(EC.element_to_be_clickable((By.XPATH, "//button[@id='signIn.guestLogin.guestLogin']")))

retry_click(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Select a location')]")))

# finding input elements for location

span_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='City, Town']")))
div_element = span_element.find_element(By.XPATH, "./parent::div")
input_element = div_element.find_element(By.XPATH, "./input")

input_element.send_keys(town)
input_element.send_keys(Keys.RETURN)

retry_click(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'AUCKLAND')]")))

# finding input elements for postcode
span_element_post = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Postcode']")))
div_element_post = span_element_post.find_element(By.XPATH, "./parent::div")
input_element_post = div_element_post.find_element(By.XPATH, "./input")

input_element_post.send_keys(postcode)
input_element_post.send_keys(Keys.RETURN)


retry_click(EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Apply')]]")))

retry_click(EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Continue to Shipping Address')]]")))

# checkout info

for key, value in input_dict.items():

    info_find = wait.until(EC.presence_of_element_located((By.XPATH, f"//span[text()='{key}']")))
    info_locate_parent = info_find.find_element(By.XPATH, "./parent::div")
    info_insert = info_locate_parent.find_element(By.XPATH, "./input")
    info_insert.send_keys(value)


retry_click(EC.element_to_be_clickable((By.XPATH, "//button[.//span[.//span[contains(text(), 'Continue to Payment')]]]")))