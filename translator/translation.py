import http.client

conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

payload = "q=Hello%2C%20I'm%20pearl%2C%20a%20junior%20software%20developer!%20Nice%20to%20meet%20you!&target=ja&source=en"
# target=(the language code you're gonna translate to)
# source=(the language code you're gonna put)

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'Accept-Encoding': "application/gzip",
    'X-RapidAPI-Key': "YOUR_API_KEY",
    'X-RapidAPI-Host': "google-translate1.p.rapidapi.com"
}

conn.request("POST", "/language/translate/v2", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
