#Proxy Git
```sh
git config --global http.proxy http://your.proxy.server:port
git config --global https.proxy https://your.proxy.server:port

```

#Proxy Window
```sh
netsh winhttp set proxy proxy-server="http://your.proxy.server:port"

```

#Proxy MacOS
```sh
export http_proxy="http://your.proxy.server:port"
export https_proxy="http://your.proxy.server:port"
```