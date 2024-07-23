import urllib.request

proxy = urllib.request.ProxyHandler({
    'http': 'http://your.proxy.server:port',
    'https': 'http://your.proxy.server:port',
})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)

response = urllib.request.urlopen('http://example.com')
print(response.read().decode('utf-8'))
