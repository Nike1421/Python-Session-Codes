import mysql

import mysql.connector
#pip install mysql-connector-python
class db:
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost",user="root",passwd="root",database="java_demo",auth_plugin='mysql_native_password')
        self.cursor = self.db.cursor()
    def read(self):
        self.cursor.execute("SELECT * FROM login")
        self.res = self.cursor.fetchall()
        print(self.cursor._check_executed())
        for i in self.res:
            print(i[0]+i[1])
    
    def insert(self,username,password):
        sql = "INSERT INTO login (user_name, password) VALUES (%s, %s)"
        val = (username, password)
        self.cursor.execute(sql, val)
        self.db.commit()
    
    def update(self,username,password):
        query = "UPDATE login SET password = %s  WHERE user_name = %s"
        val=(username,password)
        self.cursor.execute(query,val)
        self.db.commit()
        
        