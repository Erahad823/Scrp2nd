
'''While loop doest work in Auction website it goes to infinite their is bugs in website'''


# import os 
# import requests
# import time 
# from bs4 import BeautifulSoup
# from datetime import date
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# import chromedriver_autoinstaller

# # Get today's date
# today = date.today()

# # Set ChromeOptions to disable unnecessary features
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-gpu")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--no-sandbox")
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--disable-plugins-discovery')
# options.add_argument('--disable-features=VizDisplayCompositor')
# options.add_argument('--disable-features=RendererCodeIntegrity')
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_argument('--disable-extensions')

# # Install Chromedriver if needed and set ChromeService
# chromedriver_path = chromedriver_autoinstaller.install()
# service = ChromeService(executable_path=chromedriver_path)

# # Initialize ChromeDriver instance
# driver = webdriver.Chrome(service=service, options=options)

# # Scrape main page for auction links
# url = f'https://www.auctionzip.com/online-auctions/?catalogDate={today}&country=&catID=1'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'lxml')
# list_of_links = []
# for link in soup.find_all('div', class_='row cat-list-item mt-4 mb-2'):
#     url = link.find('a')
#     img = link.find('img', {'alt': True})
#     href = url.get('href')
#     urls = 'https://www.auctionzip.com/' + href
#     list_of_links.append(urls)

# # Scrape each auction link for individual item links
# url_list = []
# for link in list_of_links:
#     count = 0 
#     page = 1
#     while True:
#         page_url = f'{link}?pageNum={page}'
#         print(page_url)
#         driver.get(page_url)
#         time.sleep(4)
        
#         # # Get item links
        # for new_link in driver.execute_script('return document.querySelectorAll("#catalog-id .col-6.col-md-4.col-lg-3.my-4.px-3 a")'):
        #     href = new_link.get_attribute('href')
        #     print(href)
        #     url_list.append(href)
        
#         # Check if there is a next page
#         # document.querySelector("#pagination-nav-").getAttribute('href')
#         next_button = driver.execute_script('return document.querySelector("#pagination-nav-")')
#         next = driver.execute_script("return arguments[0].getAttribute('href')", next_button)

#         if not next:
#             break
        
#         # Increment page counter
#         page += 1
#         count +=1

# # Print number of items scraped and list of item links
# print(f"Scraped {len(url_list)} items.")
# print(url_list)

# # Close the ChromeDriver instance
# driver.quit()


'''Scrape All the urls inside each page number inside auction website by using Selenium and beautifulSoup '''

# import requests
# from bs4 import BeautifulSoup
# from datetime import date
# from driver_controller import *
# # Get today's date
# today = date.today()

# # Scrape main page for auction links
# url = f'https://www.auctionzip.com/online-auctions/?catalogDate={today}&country=&catID=1'
# print(url)
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'lxml')
# list_of_links = []
# for link in soup.find_all('div', class_='row cat-list-item mt-4 mb-2'):
#     url = link.find('a')
#     img = link.find('img', {'alt': True})
#     href = url.get('href')
#     urls = 'https://www.auctionzip.com/' + href
#     list_of_links.append(urls)
# print(f"Scraped {len(list_of_links)} links.")
# # print(list_of_links)
# # Scrape each auction link for individual item links
# for link in list_of_links:
#     response = requests.get(link)
#     soup = BeautifulSoup(response.content,'lxml')
#     url_list = []
#     for page_links in soup.find_all('ol',class_='pagination justify-content-center'):
#         for link in page_links.find_all('a'):
#             url = link.get('href').split('?',1)[0].strip()
            
#             url_list.append(url)
    
#     # Print number of links scraped and list of links
#     print(f"Scraped {len(url_list)} links.")
#     # print(url_list)
#     page = []
#     for i in range(len(url_list))[1:]:
#         page_url = f'https://www.auctionzip.com/{url_list[i]}?pageNum={i}'

#         if '#' in url_list[i]:
#             page_url = page_url.replace('#', url_list[2])

#         # print(page_url)
#         page.append(page_url)
#     # print(page)

#     for f_url in page:
#         driver = driver_instance(None)
#         driver.driver_control()
#         driver.driver.get(f_url)
#         # loop through the link elements and extract their href attributes
#         url_ls = []
#         for new_link in driver.driver.execute_script('return document.querySelectorAll("#catalog-id .col-6.col-md-4.col-lg-3.my-4.px-3 a")'):
#             href = new_link.get_attribute('href')
#             print(href)
#             url_ls.append(href)



