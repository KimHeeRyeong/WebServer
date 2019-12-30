'''
Created on 2019. 12. 18.

@author: admin
'''
import pymysql

db=pymysql.connect(host='localhost'
                   ,port=3306
                   ,user='root'
                   ,passwd='autoset'
                   ,db='gamedb',charset='utf8')

try:
    cursor = db.cursor()
    sql = "INSERT INTO users(id, pass, nic) VALUES ('user7', PASSWORD(1234), 'pass1234') " 
    cursor.execute(sql)
    db.commit()
    
    sql="SELECT * FROM users"
    sql = "SELECT * FROM users WHERE user_idx"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row_data in result:
        print(row_data[0])
        print(row_data[1])
        print(row_data[2])
        print(row_data[3])
        

finally:
    db.close()