import mysql.connector
import sys

class Dbhelper:
    
    def __init__(self):
        
        try:
            self.conn = mysql.connector.connect(host="localhost", port="3307", user="root", password="", database="hit-db-demo")
            self.mycursor = self.conn.cursor()  # mycursor is the name
            #  this step is risky bcz it is now connected to the database , so put the whole step in try block
        except:
            print("Could not connect to database. Try again")
            sys.exit(0)
        else:
            print("Connnected to the database.")
            
            
            
    def registration(self, name, email, password):
        
        try:
            # database se baat krne ke liye cursor object use krenge
            self.mycursor.execute("""
            INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}')                      
            """.format(name, email, password))
            
            self.conn.commit()   # commiting (ACID Properties) the changes to the database to store them permanently
        except:
            return -1
        else:
            return 1
        
        
        
    def search(self, email, password):
        
        self.mycursor.execute("""
        SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'
        """.format(email, password))
        
        # fetches all the data stored in mycursor when reading type operation is performed in the database
        data = self.mycursor.fetchall()
        print(data)