# import mysql.connector

# class database : 
#    def connect(self) :
#       self.db = mysql.connector.connect(
#          user='root', 
#          password='', 
#          host='localhost', 
#          database='Bioskop_pbop'
#       )
#       self.cur = self.db.cursor()

#    def createTbl(self,query):
#          self.cur.execute(query)
#          self.db.commit()

#    def insertValue(self, query, data):
#        self.cur.execute(query, data)
#        self.db.commit()

#    def selectValue(self, query, data=None):
#         cursor = self.db.cursor()
#         try:
#             cursor.execute(query, data)
#             result = cursor.fetchall()
#             return result
#         except Exception as e:
#             print(f"Error executing query: {e}")
#             return None
#         finally:
#             cursor.close()

import mysql.connector

class database:
    def connect(self):
        self.db = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='Bioskop_pbop'
        )
        self.cur = self.db.cursor()

    def createTbl(self, query):
        try:
            self.cur.execute(query)
            self.db.commit()
            print("Table created successfully.")
        except Exception as e:
            print(f"Error creating table: {e}")

    def insertValue(self, query, data):
        try:
            self.cur.execute(query, data)
            self.db.commit()
            print("Data inserted successfully.")
        except Exception as e:
            print(f"Error inserting data: {e}")

    def selectValue(self, query, data=None):
        with self.db.cursor() as cursor:
            try:
                cursor.execute(query, data)
                result = cursor.fetchall()
                return result
            except Exception as e:
                print(f"Error executing query: {e}")
                return None
