import mysql.connector


config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'port': 3306,
    'database': 'com.zwc',
    'charset': 'utf8'
}

def  insert(sql_cmd, param):
    """
    :param sql_cmd sql 命令
    :param param 参数
    """
    try:
        conn = mysql.connector.connect(**config)
    except mysql.connector.Error as e:
        print('connect fails!{}'.format(e))

    cursor = conn.cursor()
    try:
        cursor.execute(sql_cmd, param)
    except mysql.connector.Error as e:
        print('connect fails!{}'.format(e))
    finally:
        cursor.close()
        conn.close()

class Member:
    def __init__(self,id,username):
        self.id = id
        self.username = username

def  select(sql_query):
    """
    :param sql_cmd sql 命令
    :param param 参数
    """
    try:
        conn = mysql.connector.connect(**config)
    except mysql.connector.Error as e:
        print('connect fails!{}'.format(e))

    cursor = conn.cursor()
    list = [];
    try:
        cursor.execute(sql_query)
        for id, username in cursor:
            member = Member(id,username)
            list.append(member);
        return list
    except mysql.connector.Error as e:
        print('connect fails!{}'.format(e))
    finally:
        cursor.close()
        conn.close()

if __name__ ==  '__main__':
    sql_cmd = "insert into stu (name, age, sex) value (%s, %s, %s)"
    sql_query = 'select id,username from tb_member ;'
    param = ('yangguo', 28, 'male')
    resule = select(sql_query)
    for Member in  resule:
        print(Member.id,Member.username)