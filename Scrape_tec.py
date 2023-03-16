'''Scrape/Crawl all the urls using Xml file'''
'''For doing this we have three method
1.)
 url/sitemap/ Or url/sitemap.xml
2.) 
 url/robots.txt then take the url of xml file
3.)
 site : url ext:xml

 By using this method this gives all the url inside website
# '''

# import requests
# from bs4 import BeautifulSoup
# import time

# # url = "https://www.winfieldsoutdoors.co.uk/media/sitemapuk.xml"

# url = 'https://www.target.com/sitemap_index.xml.gz'
# response = requests.get(url)
# soup = BeautifulSoup(response.text,'lxml')
# soup = soup.find_all('loc')
# start = time.perf_counter()
# for link in soup:
#     print(link.text)
#     end = time.perf_counter()
# print(f'{end - start} in seconds')
    # for index,urls in enumerate(link):
    #     total = 0 
    #     response = requests.get(urls)
    #     soup = BeautifulSoup(response.text,'lxml')
    #     a = total= total+1
    #     print("Index =",a,index,soup.text)

'''Or'''

# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.target.com/sitemap_index.xml.gz'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# locs = soup.find_all('loc')

# total = 0
# for loc in locs:
#     url = loc.text
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     total += 1
#     print(f"Processed {total} URLs. Index={total}, URL={url}, Content={soup.text}")


'''ASYNC  request is used to speed up the speed it ingage to run multiple task simultaneously'''


# from requests_html import HTMLSession
# import time 
# import asyncio
# import requests
# from bs4 import BeautifulSoup
# # urls = 'https://www.target.com/sitemap_index.xml.gz'

# async def work(session,url):
#     response = await session.get(url)
#     soup = BeautifulSoup(response.text,'lxml')
#     soup = soup.find_all('loc')
#     start = time.perf_counter()
#     for link in soup:
#         print(link.text)
#         end = time.perf_counter()
#         return link
#     print(f'{end - start} in seconds')


# async def main(urls):
#     session = asyncHTMLSession()
#     tasks = (work(session,url='https://www.target.com/sitemap_index.xml.gz'))
#     return await asyncio.gather(*tasks)

# results = asyncio.run(main('https://www.target.com/sitemap_index.xml.gz'))



# import time 
# import asyncio
# import requests
# from bs4 import BeautifulSoup
# from aiohttp import ClientSession
# total =0 
# async def work(session, url):
#     response = await session.get(url)
#     soup = BeautifulSoup(await response.text(), 'lxml')
#     soup = soup.find_all('loc')
#     start = time.perf_counter()
#     total = 0
#     for link in soup:
#         print(link.text)
#         total = total =+ 1
#     end = time.perf_counter()
#     print(f'{end - start} seconds',total)

# async def main(urls):
#     async with ClientSession() as session:
#         tasks = [work(session, url) for url in urls[:2]]
#         await asyncio.gather(*tasks)

# urls = [
#     'https://www.target.com/sitemap_index.xml.gz',
#     'https://www.target.com/p/sitemap_001.xml.gz',
#     'https://www.target.com/p/sitemap_002.xml.gz',
#     'https://www.target.com/p/sitemap_003.xml.gz',
#     'https://www.target.com/p/sitemap_004.xml.gz',
#     'https://www.target.com/p/sitemap_005.xml.gz',
#     'https://www.target.com/p/sitemap_006.xml.gz',
#     'https://www.target.com/p/sitemap_007.xml.gz',
#     'https://www.target.com/p/sitemap_008.xml.gz',
#     'https://www.target.com/p/sitemap_009.xml.gz',
#     'https://www.target.com/p/sitemap_010.xml.gz',
#     'https://www.target.com/p/sitemap_011.xml.gz',
#     'https://www.target.com/p/sitemap_012.xml.gz',
#     'https://www.target.com/p/sitemap_013.xml.gz',
#     'https://www.target.com/p/sitemap_014.xml.gz',
#     'https://www.target.com/p/sitemap_015.xml.gz',
#     'https://www.target.com/p/sitemap_016.xml.gz',
#     'https://www.target.com/p/sitemap_017.xml.gz',
#     'https://www.target.com/p/sitemap_018.xml.gz',
#     'https://www.target.com/p/sitemap_019.xml.gz',
#     'https://www.target.com/p/sitemap_020.xml.gz',
#     'https://www.target.com/c/sitemap_001.xml.gz',
#     'https://www.target.com/s/sitemap_001.xml.gz',
#     'https://www.target.com/s/sitemap_002.xml.gz',
#     'https://www.target.com/s/sitemap_003.xml.gz',
#     'https://www.target.com/fc/sitemap_001.xml.gz',
#     'https://www.target.com/fc/sitemap_002.xml.gz',
#     'https://www.target.com/fc/sitemap_003.xml.gz',
#     'https://www.target.com/fc/sitemap_004.xml.gz',
#     'https://www.target.com/fc/sitemap_005.xml.gz',
#     'https://www.target.com/fc/sitemap_006.xml.gz',
#     'https://www.target.com/fc/sitemap_007.xml.gz',
#     'https://www.target.com/fc/sitemap_008.xml.gz',
#     'https://www.target.com/fc/sitemap_009.xml.gz',
#     'https://www.target.com/sl/sitemap_001.xml.gz'
# ]

# start = time.perf_counter()
# result = asyncio.run(main(urls))
# print(result)

# fin = time.perf_counter()
# print(fin - start, total)


'''Async can be complicated for beginners, managing coroutines and event loops - but in this video I show you an alternative using grequests - all the benefits of Async with the hard work taken care of. Async works by concurrently creating requests to the server without having to wait for each response in turn, it manages them all at the same time. This greatly speeds up the web scraping process when scraping multiple pages. 

We can't include the parsing part asychronously, but that it a CPU intense task and is very quick.I expand on the last video that was on a sandbox site with this real world Python web scraping project that can be implemented to different sites and scaled to many more pages.
'''

'''GRequests allows you to use Requests with Gevent to make asynchronous HTTP Requests easily'''

# from bs4 import BeautifulSoup
# import grequests
# import pandas as pd

# def get_urls():
#     urls = []
#     for x in range(1,11):
#         urls.append(f'https://www.canoeandkayakstore.co.uk/collections/activity-recreational-beginner?page={x}')
#     return urls

# def get_data(urls):
#     reqs = [grequests.get(link) for link in urls]
#     resp = grequests.map(reqs)
#     return resp

# def parse(resp):
#     productlist = []
#     for r in resp:
#         sp = BeautifulSoup(r.text, 'lxml')
#         items = sp.find_all('div', {'class': 'product-grid-item__info'})
#         for item in items:
#             product = {
#             'title' : item.find_all('a')[0].text.strip(),
#             'price': item.find('span', {'class': 'product-grid-item-price'}).find_all('span')[0].text.strip(),
#             'avail': item.find('span', {'class': 'product-grid-item__info__availability--value'}).text.strip(),
#             }
#             productlist.append(product)
#             print('Added: ', product)
#     return productlist


# urls = get_urls()
# resp = get_data(urls)
# df = pd.DataFrame(parse(resp))
# df.to_csv('canoes.csv', index=False)


'''Hibid Urls AND data '''
'''Scrape using Aiohttp and async and calculate CPU usage '''

from bs4 import BeautifulSoup
import requests
import pandas as pd 
import time
import asyncio
from aiohttp import ClientSession
import aiohttp
import os
import psutil

data = pd.read_csv("Hibid_urlsss.csv", encoding="ISO-8859-1") 
urls = data['url'].tolist()[0:10]  # Convert DataFrame column to list
primary_categories = data['primary_category'].tolist()[0:10]
secondary_categories = data['secondry_category'].tolist()[0:10]

async def work(session, url, primary_category, secondary_category):

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    s_time = time.time()
    details = []

    '''Open the url using requests and then use Beautifulsoup to extract the content from html'''
    try:
        response = await session.get(url,headers = headers)
        response.raise_for_status() 
        soup = BeautifulSoup(await response.text(), 'lxml')
        print(urls)
        '''Scrape Product Name'''
        Product_Name = soup.find("h1").text
        Name = Product_Name.split("- ", 1)[1]

        '''Scrape Lot Number'''
        Lot_no = Product_Name.split("- ", 1)[0].split(": ", 1)[1]

        '''Scrape Image Url'''
        image = soup.find('div', class_="ngx-gallery-image ngx-gallery-active ngx-gallery-clickable ng-star-inserted")
        img_url = image.get('style')
        img_url = img_url.split("('", 1)[1].split("')", 1)[0].strip()

        '''Product Description'''
        Description = soup.find("div", class_="text-pre-line").text
        # print(Description)

        '''Scrape High Bid Amount'''
        High_Bid_amt = soup.find("span", class_="lot-high-bid")
        High_Bid_amt = High_Bid_amt.text.split("USD", 1)[0].split(": ", 1)[1].strip()

        '''Scrape Bid Amount'''
        Bid = soup.find("span", class_="TileDisplayMinBid").text

        df_list = {
            "primary_category": primary_category,
            "secondary_category": secondary_category,
            "urls": url,
            "product_name": Name,
            "image_url": img_url,
            "Description": Description,
            "lot": Lot_no,
            "bid_amount": Bid,
            "Highest_Bid": High_Bid_amt
        }
        details.append(df_list)
        print(Name, Lot_no, img_url, High_Bid_amt, Bid)
    except (aiohttp.ClientError, requests.RequestException, ValueError, AttributeError) as e:
        print(f"Error occurred while scraping {url}: {e}")
    e_time = time.time()
    print(f"{e_time - s_time}", "in Seconds")
    return details


async def main(urls, primary_categories, secondary_categories):
    connector = aiohttp.TCPConnector(limit = 100)
    async with ClientSession(connector=connector) as session:
        details = []  # initialize the list outside the loop
        for url, primary_category, secondary_category in zip(urls, primary_categories, secondary_categories):
            result = await work(session, url, primary_category, secondary_category)
            details.extend(result)  # append the product details to the list
        df = pd.DataFrame(details)
        df.to_csv('canoes.csv', index=False)  # save the data to CSV file after the loop
        return details

start = time.perf_counter()
result = asyncio.run(main(urls, primary_categories, secondary_categories))
# print(result)
fin = time.perf_counter()
print(fin-start,'Time')
print('The CPU usage is: ', psutil.cpu_percent(fin-start))
# Getting % usage of virtual_memory ( 3rd field)
print('RAM memory % used:', psutil.virtual_memory()[2])
# Getting usage of virtual_memory in GB ( 4th field)
print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)
