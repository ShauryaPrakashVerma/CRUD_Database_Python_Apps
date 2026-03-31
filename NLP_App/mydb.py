import json

class Database:
    
    
    
    # whole data is getting duplicated (previous data, previous data + next data)
    def add_data(self, name, email, password):
        
        # with .get function
        with open("db.json","r+") as rf:
            database = json.load(rf)
            if email in database:
                return 0
            else:
                database[email] = [name, password]
                rf.seek(0) 
                rf.truncate()
                json.dump(database, rf, indent=4)
            
        return 1
    
    def search(self, email, password):
        
        with open("db.json", "r") as rf:
            database = json.load(rf)
            
            if email in database:
                if database[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 2