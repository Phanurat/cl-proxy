import requests

# กำหนดค่า proxy server
proxies = {
    'http': 'http://192.168.0.135:6000',
    'https': 'http://192.168.0.135:6000'
}

# ฟังก์ชันในการตรวจสอบ IP ที่ใช้ในการเข้าถึงเว็บไซต์
def get_public_ip(proxies=None):
    try:
        response = requests.get('https://api.ipify.org?format=json', proxies=proxies, timeout=10)
        return response.json()['ip']
    except requests.RequestException as e:
        return f"Error: {e}"

# ตรวจสอบ IP ก่อนใช้ proxy
original_ip = get_public_ip()
print(f"Original IP Address: {original_ip}")

# ส่งคำขอ (request) ผ่าน proxy
try:
    response = requests.get('https://www.facebook.com', proxies=proxies, timeout=10)
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Error during request: {e}")

# ตรวจสอบ IP หลังใช้ proxy
proxied_ip = get_public_ip(proxies)
print(f"Proxied IP Address: {proxied_ip}")
