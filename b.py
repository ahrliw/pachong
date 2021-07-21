import requests
# post
# url上的参数
payload = {
    "key": "8dbee1fcd8627fb6699bce7b986adc45",
    "qq": "1111"
}
# url地址
url = "http://japi.juhe.cn/qqevaluate/qq"

r = requests.post(url, params=payload)
print(r.url)
print(r.text)
print(type(r.text))
print(r.json())
print(r.json()["error_code"])