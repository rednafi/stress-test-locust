<div align="center">

# Stress Testing w/ Locust

</div>


## Description

[Locust](https://locust.io/) is a distributed and scalable open-source library that helps you write effective load tests in pure Python. This repository demonstrates a modular architecture to establish a template for quickly building a scalable stress testing pipeline with Locust.

## Locust Terminology

If you're unfamiliar with the terminologies and the generic workflow of writing stress-tests with Locust, then you should go through the official [documentation](https://docs.locust.io/en/stable/) first. With that out of the way, let's go through a few terminologies that comes up in this context quite often:

**Task:** In Locust, a [Task](https://docs.locust.io/en/stable/writing-a-locustfile.html#tasks) is the smallest unit of a test suite. Usually, it means, any function or method that is decorated with the `@task` decorator.

**TaskSet:** A [TaskSet](https://docs.locust.io/en/stable/writing-a-locustfile.html#taskset-class) is a class that establishes a contextual boundary between different groups of Tasks. You can essentially group multiple similar Tasks inside a TaskSet. Then you use the TaskSets from your User class.

**User:** In Locust, a [User](https://docs.locust.io/en/stable/writing-a-locustfile.html#user-class) is a class that executes the tests either by directly calling the Task methods or via using TaskSets.

***In more complex cases, the tests can further be organized by arranging them in multiple test modules. This template groups the Tasks using TaskSets and places multiple TaskSets in separate test modules to ensure modularity and better scalability.***

## Target API

This template uses [Rapid API's](https://rapidapi.com/) currency-exchange [API](https://rapidapi.com/fyhao/api/currency-exchange) for showcasing the load testing procedure. The API converts one currency to another using the current exchange rate.

### API Anatomy

It takes three parameters in its query string:
```
1. q    : str - quantity
2. from : str - currency to convert from
3. to   : str - currency to convert to
```

And returns the converted value.


### Access the API

Sign up for a Rapid API [account](https://rapidapi.com/signup) and get your token. You can access the API via cURL like (You need to provide your API token in the header):

```bash
curl --request GET \
         --url 'https://currency-exchange.p.rapidapi.com/exchange?q=1.0&from=USD&to=BDT' \
         --header 'x-rapidapi-host: currency-exchange.p.rapidapi.com' \
         --header 'x-rapidapi-key: your-api-token'
```

The response will look like this:

```
84.91925⏎
```

Or, you might want to access it via Python. You can do so using the [HTTPx](https://github.com/encode/httpx) library like this:


```python
import httpx

url = "https://currency-exchange.p.rapidapi.com/exchange"

querystring = {"q": "1.0", "from": "USD", "to": "BDT"}

headers = {
    "x-rapidapi-host": "currency-exchange.p.rapidapi.com",
    "x-rapidapi-key": "your-api-token",
}

with httpx.Client(http2=True) as client:
    response = client.get(url, headers=headers, params=querystring)

print(response.text)
```

## Stress Testing Pipeline

Below, you can see the core architecture of the load testing pipeline. For brevity's sake—files regarding containerization, deployment, and dependency management have been omitted.


```
src/
├── locustfiles         # Directir where the load test modules live
│   ├── __init__.py
│   ├── bdt_convert.py  # Load test module 1
│   └── rs_convert.py   # Load test module 2
├── __init__.py
├── auth.py             # Auth, login, logout, etc
├── locust.conf         # Locust configurations
├── locustfile.py       # Locust entrypoint
└── settings.py         # Read the environment variables here
```

The test suite has three primary components—
`setup.py`, `locustfiles`, and the `locust.conf` file.

### [setup.py](src/setup.py)
The common elements required for testing, like `auth`, `login`, and `logout` functions reside in the `setup.py` file.

### [locustfiles](src/locustfiles/)
The load test modules reside in the **`locustfiles`** directory. Test modules import and use the functions in the `setup.py` file before executing each test.

In the `locustfiles` directory, currently, there are only two load test modules—`bdt_convert.py` and `rs_convert.py`. You can name your test modules whatever you want and the load testing classes and functions should reside here.

* [bdt_convert.py](src/locustfiles/bdt_convert.py): This module houses a single TaskSet named `BDTConvert` that has two Tasks—`usd_to_bdt` and `bdt_to_usd`. The first Task tests the exchange API when the request query asks for USD to BDT currency conversion and the second Task tests the API while requesting BDT to USD conversion.

* [rs_convert.py](src/locustfiles/rs_convert.py): The second test module does the same things as the first one; only it tests the APIs while the request query asks for USD to RS conversion and vice versa.

    The reason that there are two similar test modules is just to demonstrate how you can organize your Tasks, TaskSets, and test modules.

* [locustfile.py](src/locustfile.py): This file works as the entrypoint of the workflow. It imports the TaskSets from the `bdt_convert` and `usd_convert` modules and creates a [HttpUser](https://docs.locust.io/en/stable/writing-a-locustfile.html#making-http-requests) that will execute the tasks.

### [locust.conf](src/locust.conf)

The **`locust.conf`** file defines the configurations like *hostname*, *number* of *workers*, *number of simulated users*, *spawn rate*, etc.


## Run the Stress Tests Locally

* Make sure you have [docker](https://www.docker.com/) and [docker-compose v2](https://github.com/docker/compose) installed on your machine.

* Clone this repository and go to the root directory.

* Place your rapidAPI token in the `.env` file.

* Run:

    ```bash
    docker compose up -d
    ```

    This will spin up a master container and a single worker container that will do the testing. If you want to deploy more workers to do the load testing then run:

    ```bash
    docker compose up -d --scale worker 2
    ```

* To access the Locust GUI, go to [http://localhost:8089/](http://localhost:8089/) on your browser. You'll be prompted to provide a username and a password. Use `ubuntu` as the username and `debian` as the password. You'll be greeted by a screen like below. You should see that the fields of the form are already filled in since Locust pulls the values from the `locust.conf` file:

    ![locust signin](https://user-images.githubusercontent.com/30027932/92285103-51988580-ef25-11ea-9155-c9d3f5dcaf42.png)

* Once you've pressed the *start swarming* button, you'll be taken to the following page:

    ![Screenshot from 2020-09-05 03-12-25](https://user-images.githubusercontent.com/30027932/92285284-b94ed080-ef25-11ea-9f91-3f972fd844f1.png)

* You can start, stop and control your tests from there.


## Disclaimer
This dockerized application is production-ready. However, you shouldn't expose your environment file (.env) in production. Here, it was done only for demonstration purposes.
