 def save_data(self):
     data = {
        "users" : self.users,
        "account numbers" : self.account_numbers,
        "accounts":self.accounts
    }
     with open("bank_users.json","w") as file:
        json.dump(data,file,indent=4)

    def load_data(self):
     with open("bank_users.json","r") as file:
      data = json.load(file)
      self.users = data.get("users")
      self.account_numbers = data.get("account numbers")
      self.accounts = data.get("accounts")

 {
   
  2- 
   
    "users": {
        "intisar": {
            "password": "Intisar12@",
            "full_name": "Intisar",
            "Mobile Number": "0504856624",
            "email": "intisar.warfa12@gmail.com",
            "address": "angered",
            "dob": "29-10-2005"
        },
        "ikram": {
            "password": "Ikram123@",
            "full_name": "Ikram",
            "Mobile Number": "0504856634",
            "email": "ikram.warfa12@gmail.com",
            "address": "angered",
            "dob": "29-10-2005"
        },
        "sireen": {
            "password": "Sireen12@",
            "full_name": "Sireen",
            "Mobile Number": "0504856624",
            "email": "sireen.abujami@gmail.com",
            "address": "firhamnsporten",
            "dob": "29-10-2005"
        }
    },
    "account numbers": {
        "intisar": 0,
        "ikram": 0,
        "sireen": "6792271013"
    },
    "accounts": {
        "intisar": 0,
        "ikram": 0,
        "sireen": 0
    }
}     