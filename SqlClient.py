import mysql.connector

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'port': 3306,
    'database': 'com.zwc',
    'charset': 'utf8'
}

try:
    cnn = mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))
cursor = cnn.cursor()
try:
    sql_query = 'select id,username from tb_member ;'
    cursor.execute(sql_query)
    for id, username in cursor:
        print (id, username)
except mysql.connector.Error as e:
    print('query error!{}'.format(e))
finally:
    cursor.close()
    cnn.close()