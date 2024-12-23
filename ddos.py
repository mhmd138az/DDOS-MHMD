import requests

def check_sql_injection(url):
    payload = "' OR '1'='1"
    full_url = url + payload
    try:
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"Potential SQL Injection vulnerability found at: {full_url}")
        else:
            print(f"No SQL Injection vulnerability detected at: {full_url}")
    except requests.exceptions.RequestException as e:
        print(f"Error with the request: {e}")

url = input("Enter the URL of the target website (e.g., https://example.com): ").strip()

if not url.startswith("http://") and not url.startswith("https://"):
    print("Invalid URL format. Please start with 'http://' or 'https://'.")
else:
    check_sql_injection(url)
