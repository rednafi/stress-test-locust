<div align="center">

# Stress Testing w/ Locust

</div>

## Description

Locust is a distributed and scalable open source library that let's you write effective load-tests in pure Python. This repository demonstrates a modular architecture to establish a template for quickly architecting scalable load tests via Locust.

It uses [Rapid API's](https://rapidapi.com/) currency-exchange [API](https://rapidapi.com/fyhao/api/currency-exchange) for doing the load testing.


### Access the API

Sign up for a Rapid API account and get your token. You can access the API via Python's [HTTPx](https://github.com/encode/httpx) library like this:

```python
import httpx

url = "https://currency-exchange.p.rapidapi.com/exchange"

querystring = {"q": "1.0", "from": "USD", "to": "BDT"}

headers = {
    "x-rapidapi-host": "currency-exchange.p.rapidapi.com",
    "x-rapidapi-key": "your-api-token",
}

with httpx.Client() as client:
    response = client.get(url, headers=headers, params=querystring)

print(response.text)
```

## Architecture

```
.
├── commons               [Common functions required by the test modules]
│   └── auth.py
├── locust.conf           [Locust config file]
├── locustfiles           [Primary folder where the tests live]
│   ├── __init__.py
│   ├── bdt_convert.py    [TaskSet 1]
│   ├── rs_convert.py     [TaskSet 2]
│   └── locustfile.py     [Locust entrypoint]
└── scripts               [Scripts required for deployment and linting]
    └── run.sh
```

## Run

* Make sure you've `docker` and `docker-compose` installed on your machine
* Clone this repository and go to the root directory
* Run:
    ```
    sudo chmod +x scripts/run.sh
    ./scripts/run.sh
    ```
