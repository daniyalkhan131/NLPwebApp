#for dealing with database we do this in seperate file this db file
import json

class Database:
    def insert(self,name,email,password):
        with open('templates/users.json', 'r') as rf:
            users=json.load(rf)

            if email in users:
                return 0
            else:
                users[email]=[name,password]

        with open('templates/users.json', 'w') as wf:
            json.dump(users,wf,indent=4)#indent is for displaying json file properly with indentation
            return 1

    def search(self,email,password):
        with open('templates/users.json', 'r') as rf:
            users=json.load(rf)

            if email in users:
                if users[email][1]==password:
                    return 1
                else:
                    return 0
            else:
                return 0
