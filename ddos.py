import requests

def check_sql_injection(url):
    payloads = ["' OR '1'='1", '" OR "1"="1', "' OR 1=1 --", "' OR 'a'='a"]
    for payload in payloads:
        response = requests.get(url + payload)
        if "error" in response.text or "Warning" in response.text:
            print(f"Potential SQL Injection vulnerability detected at {url} with payload {payload}")
        else:
            print(f"No SQL injection detected with payload {payload}")

def check_xss(url):
    payloads = ["<script>alert('XSS')</script>", "<img src='x' onerror='alert(1)'>"]
    for payload in payloads:
        response = requests.get(url + payload)
        if payload in response.text:
            print(f"Potential XSS vulnerability detected at {url} with payload {payload}")
        else:
            print(f"No XSS vulnerability detected with payload {payload}")

def main():
    target_url = input("Enter the target URL: ")
    print("Checking for SQL Injection vulnerabilities...")
    check_sql_injection(target_url)
    
    print("Checking for XSS vulnerabilities...")
    check_xss(target_url)

if name == "main":
    main()
