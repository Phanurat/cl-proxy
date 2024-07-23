import requests

proxy = {
    'http': 'http://your.proxy.server:port',
    'https': 'http://your.proxy.server:port',
}

response = requests.get('http://example.com', proxies=proxy)
print(response.text)
