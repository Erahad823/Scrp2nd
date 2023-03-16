import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller

class driver_instance:

    def __init__(self, driver):
        self.driver = driver 

    def driver_control(self): 
        
        start = time.perf_counter()
        # Set up ChromeDriver options
        self.options = webdriver.ChromeOptions()
        # options.add_argument("--start-maximized")
        # options.add_argument("--headless")
        self.options.add_argument("--disable-blink-features")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--disable-extensions')
        self.options.add_argument('--disable-plugins-discovery')
        self.options.add_argument('--disable-features=VizDisplayCompositor')
        self.options.add_argument('--disable-features=RendererCodeIntegrity')
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.options.add_experimental_option('useAutomationExtension', False)

        # Set up ChromeDriver service

        self.chromedriver_path = f'{os.getcwd()}/chromedriver'

        if not os.path.exists(self.chromedriver_path):
            os.mkdir(self.chromedriver_path)

        self.chromedriver_path = chromedriver_autoinstaller.install(path=f'{os.getcwd()}/chromedriver')

        service = ChromeService(executable_path=self.chromedriver_path)

        # Initialize ChromeDriver instance
        self.driver = webdriver.Chrome(service=service, options=self.options)
        return self.driver


if __name__ == '__main__':

    driver = driver_instance(None)
    driver.driver_control()
    driver = driver.driver.get("https://www.google.com")
    
