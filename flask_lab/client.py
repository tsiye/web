import requests

URL_GET1 = "http://127.0.0.1/hello"
URL_GET2 = "http://127.0.0.1/times"

def user_requests_hello(n):
    response = requests.get(URL_GET1)
    print(response.text)

def user_requests_times():
    response = requests.get(URL_GET2)
    print(response.text)

if __name__ == '__main__':
    n = int(input("Please input the times you want to send hello\n")) 
    for i in range (0, n):
        user_requests_hello(n)
    user_requests_times()
