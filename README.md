<div align="center">

# Stress Testing w/ Locust

</div>

## Description

[Locust](https://locust.io/) is a distributed and scalable open-source library that lets you do effective load testing in pure Python. This repository demonstrates a modular architecture to establish a template for quickly architecting scalable load tests using Locust. It uses [Rapid API's](https://rapidapi.com/) currency-exchange [API](https://rapidapi.com/fyhao/api/currency-exchange) for showcasing the load testing procedure.


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

## Run the Load Tests Locally

* Make sure you've [docker](https://www.docker.com/) and [docker-compose](https://github.com/docker/compose) installed on your machine

* Clone this repository and go to the root directory

* Run:

    ```bash
    sudo chmod +x scripts/run.sh
    ./scripts/run.sh
    ```

    This will spin up a master container and a single worker container that will do the testing. If you want to deploy more workers to do the load testing then run:

    ```bash
    sudo chmod +x scripts/run.sh
    ./scripts/run.sh -n 4 # number of the workers
    ```
* To access the the Locust GUI, go to [http://localhost:8089/](http://localhost:8089/) on your browser. You'll be prompted to provide a username and a password. Use `ubuntu` as the `username` and `debian` as the password. You'll be greeted by a screen like this:

    ![locust signin](https://user-images.githubusercontent.com/30027932/92285103-51988580-ef25-11ea-9155-c9d3f5dcaf42.png)

* Once you've pressed the *start swarming* button, you'll be taken to the following page:

    ![Screenshot from 2020-09-05 03-12-25](https://user-images.githubusercontent.com/30027932/92285284-b94ed080-ef25-11ea-9f91-3f972fd844f1.png)

* You can start, stop and control your tests from there.
