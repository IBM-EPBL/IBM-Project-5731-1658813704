import http.client

conn = http.client.HTTPSConnection("extract-news.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "50926b7c60mshe9177c6f3f8e9e9p1b755cjsn6e9ad935b336",
    'X-RapidAPI-Host': "extract-news.p.rapidapi.com"
    }

conn.request("GET", "/v0/article?url=https%3A%2F%2Fwww.theverge.com%2F2020%2F4%2F17%2F21224728%2Fbill-gates-coronavirus-lies-5g-covid-19", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
