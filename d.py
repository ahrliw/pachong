import requests

url = "https://www.baidu.com"

r = requests.get(url)
print(r.text)
# 猜测响应的编码
print(r.encoding)  # ISO-8859-1

# 从响应正文里面获取编码  utf-8
print(r.apparent_encoding)
print(r.content)  # byte类型
print(r.content.decode(r.apparent_encoding))
