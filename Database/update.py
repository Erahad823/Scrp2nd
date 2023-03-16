# from worker import worker
from database_controller import NoSqlClient
# import getandupdatedata



'''Save data in json format'''

# @worker.app.task(name='records_update', rate_limit='200/m')
# def update_records(value: dict, collection: str) -> None:
#     try:
#         with open(f'scraping_result/{collection}-items.json','r') as file:
#             data = json.load(file)
#     except Exception:
#         data = []
#     data.append(value)
#     with open(f'scraping_result/{collection}-items.json','w') as file:
#         json.dump(data, file, indent=4)

'''Save data to mongo database'''

# nosql_db = NoSqlClient()
# @worker.app.task(name='records_update')
# def update_records(value: dict, collection: str) -> None:
#     print('Database update initialized')
#     key = {'Url': value.get('Url')}
#     value = {'$set': value}
#     nosql_db.add_to_collection(collection, key ,value)

'''
UPDATE data into SQL database 
'''

# @worker.app.task(name='records_update', rate_limit='200/m')
# def update_records(value: dict, collection: str) -> None:
#     url = value.get('Url', None)
#     price = value.get('Price', None)
#     if price and price not in ["", "Not Found"]:
#         try:
#             if "$" in price: 
#                 price = price.strip()
#                 price = price[price.index("$") + 1:]
#                 price = float(price.strip())
#             else:
#                 price = float(price.strip())
#         except ValueError:
#             print(f"Error: unable to convert price value '{price}' to float")
#             return
#         object_data = getandupdatedata.getAndUpdateDatas()
#         status = object_data.updateData(url, price, collection)


'''Save data into Sql database '''

# @worker.app.task(name='records_update', rate_limit='200/m')
# def update_records(value: dict, collection: str) -> None:
#     url = value['Url']
#     price = value['Price']
#     if price not in ["", "Price not found"]:
#         if "$" in price: 
#             price = float(price[1:])
#         else:
#             price = float(price)
#         objectData = getandupdatedata.getAndUpdateDatas()
#         status = objectData.updateData(url, price, collection)

'''Save data to mongo database'''


# nosql_db = NoSqlClient()
# @worker.app.task(name='records_update')
# def update_records(value: dict, collection: str) -> None:
#     print('Database update initialized')
#     key = {'Url': value.get('Url')}
#     value = {'$set': value}
#     nosql_db.add_to_collection(collection, key ,value)