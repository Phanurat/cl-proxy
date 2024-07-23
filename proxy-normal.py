import os

# กำหนดค่า proxy server
os.environ['HTTP_PROXY'] = 'http://your.proxy.server:port'
os.environ['HTTPS_PROXY'] = 'http://your.proxy.server:port'

# ตัวอย่างการใช้งาน
import requests

response = requests.get('http://example.com')
print(response.text)
