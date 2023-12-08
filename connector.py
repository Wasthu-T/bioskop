import mysql.connector

class database : 
   def connect(self) :
      self.db = mysql.connector.connect(
         user='root', 
         password='', 
         host='localhost', 
         database='Bioskop_pbop'
      )
      self.cur = self.db.cursor()

   def createTbl(self,query):
         self.cur.execute(query)
         self.db.commit()

