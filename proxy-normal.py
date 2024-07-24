import os

# กำหนดค่า proxy server
os.environ['HTTP_PROXY'] = 'http://192.168.0.135:6000'
#os.environ['HTTPS_PROXY'] = 'http://your.proxy.server:port'

# ตัวอย่างการใช้งาน
import requests

response = requests.get('https://facebook.com')
print(response.text)
