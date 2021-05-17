import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'post'
DATABASE = 'dvdrental'

connection = psycopg2.connect(host='localhost', user='postgres', password='post', dbname='dvdrental' )
cursor = connection.cursor()

query =  "select * from customer limit 20;"
cursor.execute(query)
results= cursor.fetchall()
connection.close()

print(results)
# or
for item in results:
    print (item)


