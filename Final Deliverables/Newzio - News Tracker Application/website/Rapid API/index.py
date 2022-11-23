import http.client

conn = http.client.HTTPSConnection("crypto-news-live3.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "0010abfcf0mshe5d026c3f36953ep12b225jsn24bd5390cd38",
    'X-RapidAPI-Host': "crypto-news-live3.p.rapidapi.com"
    }

conn.request("GET", "/news", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
