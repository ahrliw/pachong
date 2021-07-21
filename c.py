import requests

url = "http://49.235.92.12:7005/xadmin/"

r = requests.get(url)
print(r.ok) # True
print(r.status_code)
print(r.text)      # html 格式
# print(r.json())    # JSONDecodeError