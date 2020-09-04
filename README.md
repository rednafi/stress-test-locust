# Stress Testing w/ Locust

## Description

This repository aims to demonstrate API stress testing with Python Locust. It employs factory pattern architecture to organize and orchestrate the tests. It uses RapidAPI's currency exchange [API] for demonstration purpose.

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
