import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
start = time.perf_counter()
# Set up ChromeDriver options
options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# options.add_argument("--headless")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-extensions')
options.add_argument('--disable-plugins-discovery')
options.add_argument('--disable-features=VizDisplayCompositor')
options.add_argument('--disable-features=RendererCodeIntegrity')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

# Set up ChromeDriver service

chromedriver_path = f'{os.getcwd()}/chromedriver'

if not os.path.exists(chromedriver_path):
    os.mkdir(chromedriver_path)

chromedriver_path = chromedriver_autoinstaller.install(path=f'{os.getcwd()}/chromedriver')

service = ChromeService(executable_path=chromedriver_path)

# Initialize ChromeDriver instance
driver = webdriver.Chrome(service=service, options=options)

# Navigate to login page
driver.get("https://line1.staroceanmall.com/index/user/login.html")

# Wait for login form to load using WebDriverWait and By.CLASS_NAME
wait = WebDriverWait(driver, 10)
login_form = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "login-register-form")))

# Find email and password input fields using By.NAME
email_field = login_form.find_element(By.NAME, "email")
password_field = login_form.find_element(By.NAME, "password")

# Send username and password to input fields
username = ""
password = "9"
email_field.send_keys(username)
password_field.send_keys(password)

# Find login button using By.CSS_SELECTOR
login_button = login_form.find_element(By.CSS_SELECTOR, ".login")

# Click on login button using JavaScript executor to avoid any issues with overlaying elements
driver.execute_script("arguments[0].click();", login_button)
time.sleep(3)
driver.get("https://line1.staroceanmall.com/index/rot_order/")
time.sleep(4)
# document.querySelector("body > div.main-wrapper > div.about-area.pb-100px > div > div:nth-child(2) > div.col-md-12 > div:nth-child(3) > p").innerText
total = driver.execute_script('return document.querySelector("body > div.main-wrapper > div.about-area.pb-100px > div > div:nth-child(2) > div.col-md-12 > div:nth-child(3) > p").textContent')
    
print(total)
time.sleep(4)
while total != '10':
    try:
        driver.get("https://line1.staroceanmall.com/index/rot_order/")

        # Use WebDriverWait to wait for the notification element to appear and have a text of "1"
        noti = driver.execute_script('return document.querySelector("body > div.main-wrapper > div.about-area.pb-100px > div > div:nth-child(2) > div.col-md-12 > div:nth-child(7) > p")')
        # If the notification text is "1", navigate to the desired page and click on the desired element
        if noti.text == '1':
            print(noti.text)
            driver.get('https://line1.staroceanmall.com/index/order/index.html#')
            time.sleep(3)
            button = driver.execute_script('return document.querySelector(".product-wishlist-cart a" )')
            driver.execute_script("arguments[0].click();", button)
            time.sleep(3)

        else:
            driver.get("https://line1.staroceanmall.com/index/rot_order/")
            time.sleep(3)
            grab_button = driver.find_element(By.CLASS_NAME, "submit-btn")
            driver.execute_script("arguments[0].click();", grab_button)
            grab_but = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/div")
            driver.execute_script("arguments[0].click();", grab_but)
            time.sleep(5)


    except Exception as e:

        print(f'Error: {str(e)}')

    while total == '10':
        break
driver.get('https://line1.staroceanmall.com/index/my/dashboard.html')
money = driver.execute_script('return document.getElementsByClassName("col-md-4 text-md-end")[0].textContent')
detail = money.split('₹')[1].split('Click',1)[0].strip()
print('The Amount you have ',detail)
end = time.perf_counter()
driver.quit()
total_time = (f'Total Time Taken is {end-start} in seconds')
print(total_time)
