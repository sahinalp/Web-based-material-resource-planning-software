import psycopg2
import numpy as np
from dotenv import load_dotenv
import os

class DbHelper:
    def __init__(self):
    # Connect to the database
        load_dotenv(dotenv_path="Resources\config.env")

        self.conn = psycopg2.connect(
            host=os.getenv("DB_Host"),
            database=os.getenv("DB_Database"),
            user=os.getenv("DB_User"),
            password=os.getenv("DB_Password"))
        
        self.conn.autocommit=True

    def closeConnection(self):
        self.conn.close()
    
    def readStock(self):
        cursor=self.conn.cursor()
        numrows = cursor.execute("SELECT * FROM flask.stock order by id")
        response = cursor.fetchall()
        numRows = int(cursor.rowcount)

        datas=np.ravel(response)
        datas=datas.reshape(numRows,-1)

        return datas
        
    def readSalesOrders(self):
        cursor=self.conn.cursor()
        numrows = cursor.execute("SELECT * FROM flask.salesorders order by id")
        response = cursor.fetchall()
        numRows = int(cursor.rowcount)

        datas=np.ravel(response)
        datas=datas.reshape(numRows,-1)

        return datas
        
    def updateStock(self,code,quantity):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE flask.stock set quantity = %s where code= %s", (quantity, code))
        self.conn.commit()

        cursor.close()

    def insertNewSalesOrder(self,code,total,shipped,orderNo):

        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO flask.salesorders (code,total,shipped,orderNo) VALUES (%s, %s, %s,%s)", (code,total,shipped,orderNo))
        self.conn.commit()

        cursor.close()

    def updateSalesOrders(self,code, total, shipped, orderNo):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE flask.salesorders SET code=%s, total=%s, shipped=%s where orderNo= %s", (code, total, shipped, orderNo))
        self.conn.commit()

        cursor.close()
        