import requests
import json

class token(user_data):

    def get_token(user_data):
        # API Parameters
        URL = 'https://api.invertironline.com/token'
        Host = 'api.invertironline.com'
        ContentType = 'application/x-www-form-urlencoded'
        granttype = 'password'
        
        # Parametros de usuario. Generar un archivo JSON utilizando el ejemplo user_data.json
        # con el nombre de usuario y la contraseña del la cuenta IOL
        
        with open('user_data.json') as json_file:
            user_data = json.load(json_file)
        
        
        data = {
            'Host': Host,
            'username': user_data[0]['username'],
            'password': user_data[0]['password'],
            'grant_type': granttype
        }
        
        headers = {'Content-Type': ContentType}
        
        r = requests.post(url=URL, data=data, headers=headers)
        
        data = r.json()
        
        if 'error' in data.keys():
            print('Error found: ' + data['error'])
        else:
            print
            
            print(data['access_token'])    
            print(data['refresh_token'])
            print(data['.expires'])    
    