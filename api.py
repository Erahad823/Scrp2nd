from flask import Flask, jsonify
import mysql.connector
import time
import psutil
start = time.perf_counter()

# Start monitoring CPU usage
process = psutil.Process()
start_cpu_time = process.cpu_percent()

# Create a connection to the MySQL database
def create_connection():
    conn = mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )
    return conn
app = Flask(__name__)
@app.route('/greet')
def greet():
    return jsonify({'message': f'Hello, Please enter the sludge name of linkedin profile.. Example http://127.0.0.1:5000/<name>!'})

# Define a route with a dynamic parameter
@app.route('/<linkedin_name>')
def func(linkedin_name):
    import os
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.common.by import By
    import chromedriver_autoinstaller

    start =time.perf_counter()

    options = webdriver.ChromeOptions()
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

    if "LinkedIn" in driver.title:
        print("Logged in successfully!")
    else:
        # Find email and password input fields using By.NAME
        email_field = driver.find_element(By.NAME, "session_key")
        password_field = driver.find_element(By.NAME, "session_password")

        # Send username and password to input fields
        username = "@gmail.com"
        password = ""
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
    url = linkedin_name
    try:
        time.sleep(2)
        driver.get(f'https://www.linkedin.com/in/{url}/')
        time.sleep(3)
        address = driver.execute_script('return document.querySelector("div.mt2.relative > div.pv-text-details__left-panel.mt2 > span.text-body-small.inline").textContent').strip()
        print(address)
        time.sleep(4)


        link = driver.execute_script('return document.querySelector("ul > li:nth-child(1) > div > div:nth-child(1) > a")')
        time.sleep(3)
        comp_linkedin_url = link.get_attribute('href')
        print(comp_linkedin_url)

        driver.get(comp_linkedin_url)
        time.sleep(4)
    
        pd = driver.execute_script('return document.querySelector("div.relative > div.ph5.pt3 > div:nth-child(3)")')
        time.sleep(4)
        comp_domain = driver.execute_script('return arguments[0].querySelector("a").href', pd)
        print(comp_domain)
        comp_name = comp_domain.split('.')[1].strip()
        print(comp_name)
        time.sleep(10)

    except Exception as e:
        print(f"Unable to print ",{e})

    # Close the browser window
    driver.quit()
    
    # Update the data in the database
    conn = create_connection()
    cursor = conn.cursor()
    try:
        query = "UPDATE contacts SET current_company_linkedin_url=%s, location = %s, current_company=%s ,current_company_website =%s WHERE linkedin_slug=%s"
        values = (comp_linkedin_url,address,comp_name,comp_domain, url)
        cursor.execute(query, values)
    except Exception as e:
        print(f'Unable to print{e}')
    conn.commit()
    conn.close()
    end =time.perf_counter()

    print(f'Total Time is {end - start:0.2f} in seconds..')
    end = time.perf_counter()
    print(f"Script executed successfully in {end - start:0.2f} seconds.")
    print(end-start,'Time')
    print('The CPU usage is: ', psutil.cpu_percent(end-start))
    # Getting % usage of virtual_memory ( 3rd field)
    print('RAM memory % used:', psutil.virtual_memory()[2])
    # Getting usage of virtual_memory in GB ( 4th field)
    print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)
    # End monitoring CPU usage
    end_cpu_time = process.cpu_percent()
    cpu_usage = end_cpu_time - start_cpu_time
    print(f"CPU usage: {cpu_usage}%")
    return jsonify({'message': f'Hello, {linkedin_name},!'})

if __name__ == '__main__':
    app.run(debug=True)
