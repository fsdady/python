# کد بررسی پروکسی

import requests

def check_proxy(proxy):
    try:
        response = requests.get("https://www.google.com", proxies={"https": proxy}, timeout=5)
        if response.status_code == 200:
            print(f"پروکسی {proxy} فعال است.")
        else:
            print(f"پروکسی {proxy} غیرفعال است.")
    except:
        print(f"پروکسی {proxy} غیرفعال است.")

proxies = [
    "164.92.96.237:3128",
    "192.168.1.2:8080",
    "192.168.1.3:8080"
]

for proxy in proxies:
    check_proxy(proxy)
