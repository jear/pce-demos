import requests
import sys

INSTANCE_ID = morpheus['instance']['id']
TOKEN = sys.argv[1]
FOLDER_NAME = morpheus['customOptions']['dbfoldernewname']
URL = f'https://10.69.0.160/api/instances/{INSTANCE_ID}'
HEADERS = {"Authorization": f'BEARER {TOKEN}', "Content-Type": "application/json"}
PAYLOAD = {"instance": {"name": FOLDER_NAME}}

response = requests.put(URL, json=PAYLOAD, headers=HEADERS, verify=False)
print('Successfully reset instance name')
