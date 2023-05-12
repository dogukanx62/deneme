import requests
import webbrowser


print("1")
ğ = input(": ")
a = "test"+ ğ

response = requests.get(a)
data = response.content.decode("utf-8")
print(data)