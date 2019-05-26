import requests
from requests import session()

Log_In_URL = "https://my.freecycle.org/login"
Request_URL = "https://my.freecycle.org/home/posts"
payload = {
            'action' = 'login' ,
            'username' = "ENTER_USER_NAME" ,
            'password' = "ENTER_PASSWORD"
}

with session() as c :
         c.post(Log_In_URL,data=payload)
         response = c.get(Request_URL)
         print (response.get)
         
         
