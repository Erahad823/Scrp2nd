'''SQL Connection
mysql --host=localhost --user=hestabit --password=hestabit  To connect in Console 
'''

import mysql.connector

def create_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="hestabit",
        password="hestabit",
        database="linked_url"
    )
    return conn


conn = create_connection()
print("Connection....",conn)

cursor = conn.cursor()

query = "SELECT url FROM linkedin_links"
cursor.execute(query)

urls = cursor.fetchall()

def link():

    for url in urls:
        print(url)

    return url 

conn.close()


