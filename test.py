import httpx

url = "https://currency-exchange.p.rapidapi.com/exchange"

querystring = {"q": "1.0", "from": "USD", "to": "BDT"}

headers = {
    "x-rapidapi-host": "currency-exchange.p.rapidapi.com",
    "x-rapidapi-key": "d26533cbe8msh020600a07386d87p18a610jsn31d39f87f802",
}

with httpx.Client() as client:
    response = client.get(url, headers=headers, params=querystring)

print(response.text)
