import pymysql

db = pymysql.connect(host='localhost', user='root',
                     password='root', port=3306, db='world')
cursor = db.cursor()
sql = 'select * from countrylanguage WHERE Language="English" '
res = cursor.execute(sql)
sql2 = 'insert into countrylanguage ()'
print(res)