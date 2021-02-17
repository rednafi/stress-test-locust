import logging

import httpx

from commons import settings

logging.basicConfig(level=logging.INFO)


def test_integration():
    logging.info("Make sure your server is up!")

    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"q": "1.0", "from": "USD", "to": "BDT"}

    headers = {
        "x-rapidapi-host": "currency-exchange.p.rapidapi.com",
        "x-rapidapi-key": settings.API_TOKEN,
    }

    with httpx.Client() as client:
        response = client.get(url, headers=headers, params=querystring)

    assert response.status_code == 200
