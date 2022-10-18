import http.client

conn = http.client.HTTPSConnection("cricbuzz-cricket.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "50926b7c60mshe9177c6f3f8e9e9p1b755cjsn6e9ad935b336",
    'X-RapidAPI-Host': "cricbuzz-cricket.p.rapidapi.com"
    }

conn.request("GET", "/matches/v1/recent", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
