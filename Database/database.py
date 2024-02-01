'''SQL Connection
mysql --host=localhost --user=hestabit --password=hestabit  To connect in Console 
'''


import mysql.connector

def create_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="",
        password="",
        database=""
    )
    return conn


conn = create_connection()
print("Connection....",conn)

cursor = conn.cursor()

query = "SELECT linkedin_slug FROM contacts"
cursor.execute(query)

urls = cursor.fetchone()

for url in urls:
    print(url)

conn.close()

'''To Connect with Mysql'''

# import mysql.connector

# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = '',
#     password ='',
#     database = ''
# )
# print(mydb.connection_id)

# '''To Create Database (Cursor() is must to perform any operation in Mysql)'''

# # conn = mydb.cursor()
# # conn.execute('CREATE DATABASE db1')

# '''To Create Table inside database
#    First use the database inside mydb where you want to create the table
#    the make query to create table 
#    "CREATE TABLE book(bookid integer(5),title varchar(20),price float(5,2))"
#    book = 'Table Name'
#    bookid integer(5) = Column name with 5 integer value 
#    title varchar(20) = Title with 20 charecter 
#    price float(5,2) = price with 5 value and 2 float digit 

# '''
# # curr = mydb.cursor()
# # query = "CREATE TABLE book(bookid integer(5),title varchar(20),price float(5,2))"
# # curr.execute(query)


# ''' INSERT INTO TABLE NAME book
#     b1 = replace the VALUES(%s,%s,%s)
#     mydb.commit is used to save any changes
# '''

# curr = mydb.cursor()
# query = "INSERT INTO book (bookid,title,price) VALUES(%s,%s,%s)"
# b1 = (1234,'python3',459.553)
# curr.execute(query,b1)
# mydb.commit()


# '''To Connect with Mysql'''
# import mysql.connector

# class Nosql:
#     def __init__(self, host, user, password):
#         self.host = host
#         self.user = user
#         self.password = password

# class Access(Nosql):
#     def __init__(self, host, user, password, database_name):
#         super().__init__(host, user, password)
#         self.database_name = database_name

#     def create_connection(self):
#         self.mydb = mysql.connector.connect(
#             host=self.host,
#             user=self.user,
#             password=self.password,
#             database=self.database_name
#         )
#         return self.mydb
    
#     '''To Create Database (Cursor() is must to perform any operation in Mysql)'''

#     def create_database(self):
#         cursor = self.mydb.cursor()
#         cursor.execute('CREATE DATABASE db4')
#         return cursor
    
#     '''To Create Table inside database'''

#     def Create_table(self):
#         cursor = self.mydb.cursor()
#         query = "CREATE TABLE book2(bookid integer(4),title varchar(20),price float(4,2))"
#         cursor.execute(query)


# client = Access('localhost', 'hestabit', 'hestabit', 'db1')
# client.create_connection()

# conn = client.mydb
# print("Connection....", conn)
# print(conn.connection_id)

# client.create_database()
# client.Create_table()

# cursor = conn.cursor()


