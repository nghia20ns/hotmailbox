import requests
import random
import string
import sys
import time

def generate_random_credentials(domain, provider):
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    email = f"{username}@{domain}"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    return email, password, provider

def send_credentials_to_api(email, password, provider):
    api_endpoint = "http://localhost:3005/api/products/create?api_key=dd4665fbc8a002b6d0dc9772964027e159fb4b66"  # Thay đổi URL của API của bạn ở đây
    data = {
        "email": email,
        "password": password,
        "provider": provider
    }
    response = requests.post(api_endpoint, json=data)
    if response.status_code == 200:
        print(f"{email}")
    else:
        print("Đã xảy ra lỗi khi thêm tài khoản mới.")

def main():
    domains = {
        'gmail.com': 'gmail',
        'hotmail.com': 'hotmail'
    }  # Các tên miền của dịch vụ email và provider tương ứng

    while True:
        domain = random.choice(list(domains.keys()))
        provider = domains[domain]
        email, password, provider = generate_random_credentials(domain, provider)
        send_credentials_to_api(email, password, provider)
        time.sleep(2)  # Đợi 3 giây trước khi thêm tài khoản mới

if __name__ == "__main__":
    main()
