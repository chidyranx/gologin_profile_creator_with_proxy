import time

from gologin import GoLogin
import requests
import os
from datetime import datetime
token = "{{ your gologin token/api }}"
API_URL = 'https://api.gologin.com'
PROFILES_URL = 'https://gprofiles-new.gologin.com/'
response = requests.get(  "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25",  headers={ "Authorization": "{{ your webshare token/api }}" })

if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(data["results"])
    results_list = data["results"]

    # Iterate through the list of dictionaries
    entry_number = 1
    for i, entry in enumerate(data["results"], start=1):
        username = entry['username']
        password = entry['password']
        proxy_address = entry['proxy_address']
        port = entry['port']
        print(f'{i}.Username: {username} Password: {password} Proxy Address: {proxy_address} Port: {port}')
    print(len(data["results"]))

else:
    print(f"Request failed with status code: {response.status_code}")

gl = GoLogin({
	"token": token,
	})
num_iterations = len(data["results"])
path = "C:\\Users\\HP\\Desktop\\GologinProfiles"

# Check if the path exists
if not os.path.exists(path):
    # Create the directory
    # 'path' can also be replaced with the variable you have defined
    os.makedirs(path)

for i in range(num_iterations):
    # Specify the path where you want to create the folder
    num_items = len(os.listdir(path))
    position_to_access = num_items + 1

    # Check if the specified position is valid
    if 1 <= position_to_access <= len(results_list):
        # Access the data for the specified position (subtract 1 from the position)
        entrys = results_list[position_to_access - 1]
        usernames = entrys['username']
        passwords = entrys['password']
        proxy_addresss = entrys['proxy_address']
        ports = entrys['port']

        # Print the data for the specified position
        print(
            f'{position_to_access}. Username: {username} Password: {password} Proxy Address: {proxy_address} Port: {port}')
    else:
        print(f'Invalid position: {position_to_access}')
    profile_id = gl.create({
        "name": num_items + 1,
        "os": 'mac',
        "navigator": {
            "language": 'en-US',
            "userAgent": 'random',  # Your userAgent (if you don't want to change, leave it at 'random')
            "resolution": '1024x768',  # Your resolution (if you want a random resolution - set it to 'random')
            "platform": 'win',
        },
        'proxyEnabled': True,  # Specify 'false' if not using proxy
        'proxy': {
            'mode': 'http',
            'host': proxy_addresss,
            'port': ports,
            'username': usernames,
            'password': passwords,
        },
        "webRTC": {
            "mode": "alerted",
            "enabled": True,
        },
    });
    profile = gl.getProfile(profile_id);
    file_number = f'{num_items + 1} - {profile_id}.txt'
    text_file_path = os.path.join(path, file_number)
    with open(text_file_path, 'w') as f:
        f.write(str(num_items))





