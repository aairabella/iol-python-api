import requests
import json

class Token:

    def __init__(self, file_data):

        # API Parameters
        self.URL = 'https://api.invertironline.com/token'
        self.Host = 'api.invertironline.com'
        self.ContentType = 'application/x-www-form-urlencoded'
        self.granttype = 'password'

        self.file_data = file_data


        with open(self.file_data) as json_file:
            self.user_data = json.load(json_file)
        
        
        self.data = {
            'Host': self.Host,
            'username': self.user_data[0]['username'],
            'password': self.user_data[0]['password'],
            'grant_type': self.granttype
        }
        
        self.headers = {'Content-Type': self.ContentType}
        
    def get_token(self):

        
        # Parametros de usuario. Generar un archivo JSON utilizando el ejemplo user_data.json
        # con el nombre de usuario y la contraseña del la cuenta IOL
        
        r = requests.post(url=self.URL, data=self.data, headers=self.headers)
        
        data = r.json()
        
        if 'error' in data.keys():
            print('Error found: ' + data['error'])
        else:
            print
            
            print(data['access_token'])    
            print(data['refresh_token'])
            print(data['.expires'])    
    