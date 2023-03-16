import os
import time
import psutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
# from database import create_connection

start = time.perf_counter()

# Start monitoring CPU usage
process = psutil.Process()
start_cpu_time = process.cpu_percent()

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
driver.get("https://www.linkedin.com/login")

# Delete all cookies
driver.delete_all_cookies()

# Load the cookies from file
with open("linkedin_cookies.txt", "r") as file:
    cookies = file.read().split(";")
    print(cookies)
    for cookie in cookies:
        if "=" in cookie:
            driver.add_cookie({
                "name": cookie.split("=")[0],
                "value": cookie.split("=")[1],
                "domain": "www.linkedin.com"
            })

# Check if login is successful
if "LinkedIn" in driver.title:
    print("Logged in successfully!")
else:
    # Find email and password input fields using By.NAME
    email_field = driver.find_element(By.NAME, "session_key")
    password_field = driver.find_element(By.NAME, "session_password")

    # Send username and password to input fields
    username = "ahad.hestabit@gmail.com"
    password = "8130928966@Aa"
    email_field.send_keys(username)
    password_field.send_keys(password)

    # Find login button using By.CSS_SELECTOR
    login_button = driver.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/form[1]/div[2]/button')

    # Click on login button using JavaScript executor to avoid any issues with overlaying elements
    driver.execute_script("arguments[0].click();", login_button)

    # Save the cookies to a file
    with open("linkedin_cookies.txt", "w") as file:
        cookies = driver.get_cookies()
        for cookie in cookies:
            file.write(f"{cookie['name']}={cookie['value']};")

# Navigate to LinkedIn homepage
urls = ['https://www.linkedin.com/in/aman-kumar-74911540/',
        'https://www.linkedin.com/in/vijay-gupta-50b55b16/',
        'https://www.linkedin.com/in/devanbhalla/',
        'https://www.linkedin.com/in/nadeem-a23341101/'
        ]

for url in urls:
    try:
        time.sleep(2)
        driver.get(url)
        time.sleep(3)


        # link = driver.execute_script('return document.querySelector("ul > li:nth-child(1) > div > div:nth-child(1) > a")')
        # time.sleep(3)
        # comp_prof = link.get_attribute('href')
        # print(comp_prof)

        # driver.get(comp_prof)
        # time.sleep(4)
    
        # pd = driver.execute_script('return document.querySelector("div.relative > div.ph5.pt3 > div:nth-child(3)")')
        # time.sleep(4)
        # href = driver.execute_script('return arguments[0].querySelector("a").href', pd)
        # print(href)
        # address = driver.find_element(By.CSS_SELECTOR, 'section.pv-contact-info__contact-type.ci-address > div > div.pv-contact-info__contact-item > span').text.strip()
        address = driver.execute_script('return document.querySelector("div.mt2.relative > div.pv-text-details__left-panel.mt2 > span.text-body-small.inline").textContent').strip()
        print(address)
        
    except Exception as e:
        print(f"Unable to print ",{e})

# Close the browser window
driver.quit()

# # Calculate the total time taken for the script to run
# end = time.perf_counter()
# print(f"Script executed successfully in {end - start:0.2f} seconds.")
# print(end-start,'Time')
# print('The CPU usage is: ', psutil.cpu_percent(end-start))
# # Getting % usage of virtual_memory ( 3rd field)
# print('RAM memory % used:', psutil.virtual_memory()[2])
# # Getting usage of virtual_memory in GB ( 4th field)
# print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)
# # End monitoring CPU usage
# end_cpu_time = process.cpu_percent()
# cpu_usage = end_cpu_time - start_cpu_time
# print(f"CPU usage: {cpu_usage}%")

