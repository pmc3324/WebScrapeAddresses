from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time



options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-logging'])
options.add_argument('start-maximized')
options.add_experimental_option('detach', True)


s = Service(executable_path="C:/Users/paulm/Downloads/chromedriver_windows32/chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

url = 'https://www.allstays.com/c/whole-foods-locations-map.htm'

driver.get(url)

button_click = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept Settings')]"))).click()



addressing = driver.find_elements(By.XPATH, "//*[@id='side_bar']/a")

filename = 'whole_foods_addresses2.csv'
f = open(filename, 'w')
headers = "address\n"
f.write(headers)

storages = []
for address in addressing:
    address.click()
    addresses = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "div[style = 'width: 250px;']"))).text
    storages.append(addresses)


address = []
city_state_zip = []
phone_number = []
phone_number_otherstuff = []
store_hours = []
for storage in storages:
    cleaned = storage.split('\n')
    address_city_state_zip = cleaned[1]
    f.write(address_city_state_zip.replace(',', '') + '\n')


driver.close()
