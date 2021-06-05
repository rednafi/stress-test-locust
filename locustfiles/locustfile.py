from __future__ import annotations

import logging
from typing import Any

from locust import HttpUser, events

from locustfiles.bdt_convert import BDTConvert
from locustfiles.rs_convert import RSConvert


class PrimaryUser(HttpUser):
    tasks = (BDTConvert, RSConvert)


@events.quitting.add_listener
def _(environment, **kwargs: Any) -> None:
    print(type(environment))
    if environment.stats.total.fail_ratio > 0:
        logging.error("Test failed due to failure ratio > 1%")
        environment.process_exit_code = 1
