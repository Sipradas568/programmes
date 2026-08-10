import requests
data = "deutschland"
res = requests.get("https://restcountries.com/v3.1/name/",params = data)
print(res.url)
prirent(res.status_code)