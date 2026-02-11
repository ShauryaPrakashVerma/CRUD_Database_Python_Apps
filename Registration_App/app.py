import sys
from dbhelper import Dbhelper

class Flipkart:
    
    def __init__(self):
        
        # Connect to the database in this step
        self.db = Dbhelper() #object created of the Dbhelper class in dbhelper.py. This automatically runs the code in the constructor of the Dbhelper class, which is the code to connect to the database.
        
        self.menu()
        
        
    def menu(self):
        
        user_input = input('''
        1. Enter 1 to register.
        2. Enter 2 to login.
        3. Enter anything else to exit
        ''')
        
        if user_input == '1':
            self.register()
        elif user_input == '2':
            self.login()
        else:
            sys.exit(1000)
            
    def register(self):
        name = input("Enter the name: ")
        email = input("Enter the email: ")
        password = input("Enter the password: ")
        
        response = self.db.registration(name, email, password)
        if response == -1:
            print("Error occured")
        else:
            print("Successfully completed registration")
        
        self.menu()
        
    def login(self):
        email = input("Enter the email: ")
        password = input("Enter the password: ")
        
        data = self.db.search(email, password)
        print(data)
        if data:
            print("Invalid User")
            self.login()
        else:
            print("Login Successful. Hello ",data[0][1])
        
obj = Flipkart()