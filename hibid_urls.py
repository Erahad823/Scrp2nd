'''Selenium Web Driver Process '''
# ## import dependencies
# import os
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
# import chromedriver_autoinstaller

# ## create an object of the chrome webdriver

# chromedriver_path = f'{os.getcwd()}/chromedriver'

# if not os.path.exists(chromedriver_path):
#     os.mkdir(chromedriver_path)
# options = webdriver.ChromeOptions()
# chromedriver_path = chromedriver_autoinstaller.install(path=f"{os.getcwd()}/chromedriver")
# # headless on walmart detects bot when scraping
# # options.add_argument('--headless')
# options.add_argument("--start-maximized")
# options.add_argument('--disable-blink-features')
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(service=ChromeService(chromedriver_path), options=options)


# # driver = webdriver.Chrome(executable_path = r'./chromedriver')
# ## open selenium URL in chrome browser
# driver.get('https://www.selenium.dev/')


'''Scrape the Category,URL,Count Inside Antiques '''
# import requests
# from bs4 import BeautifulSoup
# import csv

# response = requests.get("https://hibid.com/lots/antiques")

# soup = BeautifulSoup(response.content, 'html.parser')
# with open("Hibid1.csv","w",newline=None) as f:
#     csvwrite = csv.writer(f)
#     csvwrite.writerow(["Pri_Cat","Sub_Category","Counts"])
#     for item in soup.find_all('a', class_='list-group-item-action'):
#         a = item.text.strip()
#         counts = a.split("(",1)[1].split(")")[0]
#         print(counts)
#         category = a.split(" (",1)[0].replace(" / ", " ")
#         print(category)
#         csvwrite.writerow(['Antiques',category,counts])



'''Scrape Url and Save in Pandas csv Dataframe'''

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd 

# data = pd.read_csv("Hibid1.csv", encoding="ISO-8859-1")
# urls = data['Sub_Url']
# Primary_category = data['Pri_Cat']
# category = data['Sub_Category']
# counts = data['Counts']

# df_list = []
# for url in urls:
#     resp = requests.get(url)
#     repr = BeautifulSoup(resp.content , 'html.parser')
#     repr = repr.find('div',{'id' : "lot-list_info" }).text
#     print(repr)
# for url, pri_cat, sec_cat in zip(urls, Primary_category, category):
#     # initialize page counter
#     page = 1
#     count = 1
#     url_list = []

#     while True:
#         # create URL for the current page
#         page_url = f"{url}?apage={page}"
        
#         # send GET request
#         response = requests.get(page_url)
#         soup = BeautifulSoup(response.content, 'html.parser')

        
#         # scrape data from the page
#         try :
#             for link in soup.find_all('a',class_="lot-number-lead lot-link lot-title-ellipsis lot-preview-link link mb-1 ng-star-inserted"):
#                 href = link.get('href')
#                 total = 0 
#                 if href is not None:
#                     # add 'https://hibid.com' in href
#                     li = 'https://hibid.com'+href
#                     print(count, li, sec_cat)
#                     url_list.append(li)
#                     count += 1
#                     df_list.append([pri_cat,sec_cat,li])
                    
            # # check if there is another page
            # next_button = soup.find('span', class_='d-none d-md-block d-lg-block d-xl-block', string='Next')
            # if not next_button:
            #     break
            
            # # increment page counter
            # page += 1
        
#         except Exception as e:
#             print("Unable to find", e)
#     print(count)

# # create a data frame from the list of dictionaries
# df = pd.DataFrame(data = df_list, columns=(["primary_category","secondry_category","url"]))

# # save the data frame to CSV
# df.to_csv("Hibid_urls.csv", index=False)
# df.head(5)


'''Scrape Data from Hibid Urls and store in csv'''

# from bs4 import BeautifulSoup
# import requests
# import pandas as pd 
# import time

# data = pd.read_csv("Hibid_urls.csv",encoding="ISO-8859-1") 
# urls = data['url'][0:100]
# s_time = time.time()
# for index,url in enumerate(urls,start=1):

#     '''Open the url using requests and then use Beautifulsoup to extract the content from html'''
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content,'html.parser')

#     '''Scrape Product Name'''
#     Product_Name = soup.find("h1").text
#     Name = Product_Name.split("- ",1)[1]

#     '''Scrape Lot Number'''
#     Lot_no = Product_Name.split("- ",1)[0].split(": ",1)[1]

#     '''Scrape Image Url'''
#     image = soup.find('div',class_="ngx-gallery-image ngx-gallery-active ngx-gallery-clickable ng-star-inserted")
#     img_url = image.get('style')
#     img_url = img_url.split("('",1)[1].split("')",1)[0].strip()

#     '''Scrape High Bid Amount'''
#     High_Bid_amt = soup.find("span",class_="lot-high-bid")
#     High_Bid_amt = High_Bid_amt.text.split("USD",1)[0].split(": ",1)[1].strip()

#     '''Scrape Bid Amount'''
#     Bid = soup.find("span",class_="TileDisplayMinBid").text

#     e_time = time.time()
#     print(index,Name,Lot_no, img_url,High_Bid_amt,Bid)
# total_time = f"Total Time is {e_time-s_time} in Seconds"
# print(total_time)

'''Scrape the data from Hibid and store in csv using pandas '''

# from bs4 import BeautifulSoup
# import requests
# import pandas as pd 
# import time

# data = pd.read_csv("Hibid_urlsss.csv",encoding="ISO-8859-1") 
# urls = data['url'][0:10]
# primary_category = data['primary_category'][0:10]
# secondry_category = data['secondry_category'][0:10]


# details = []
# s_time = time.time()
# for primary_category,secondry_category,url in zip(primary_category,secondry_category,urls):

#     '''Open the url using requests and then use Beautifulsoup to extract the content from html'''
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content,'html.parser')

#     '''Scrape Product Name'''
#     Product_Name = soup.find("h1").text
#     Name = Product_Name.split("- ",1)[1]

#     '''Scrape Lot Number'''
#     Lot_no = Product_Name.split("- ",1)[0].split(": ",1)[1]

#     '''Scrape Image Url'''
#     image = soup.find('div',class_="ngx-gallery-image ngx-gallery-active ngx-gallery-clickable ng-star-inserted")
#     img_url = image.get('style')
#     img_url = img_url.split("('",1)[1].split("')",1)[0].strip()

#     '''Product Description'''
#     Description = soup.find("div",class_="text-pre-line").text
#     print(Description)

#     '''Scrape High Bid Amount'''
#     High_Bid_amt = soup.find("span",class_="lot-high-bid")
#     High_Bid_amt = High_Bid_amt.text.split("USD",1)[0].split(": ",1)[1].strip()

#     '''Scrape Bid Amount'''
#     Bid = soup.find("span",class_="TileDisplayMinBid").text
    
#     e_time = time.time()

#     df_list = {
#         "primary_category" : primary_category,
#         "secondry_category" : secondry_category,
#         "urls" : url,
#         "product_name" : Name,
#         "image_url" : img_url,
#         "Description" : Description,
#         "lot" : Lot_no,
#         "bid_amount" : Bid,
#         "Highest_Bid" : High_Bid_amt
#     }
#     details.append(df_list)
#     print(Name,Lot_no, img_url,Description,High_Bid_amt,Bid)
# total_time = f"Total Time is {e_time-s_time} in Seconds"
# print(total_time)
# df = pd.DataFrame(details)
# df.to_csv("Hibid_All.csv",index=False)
