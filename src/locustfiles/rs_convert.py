from __future__ import annotations

from http import HTTPStatus

from locust import TaskSet, between, task

import settings
import setup


class RSConvert(TaskSet):
    """Converting from Dollar to RS & vice versa."""

    # Time period between firing consecutive tasks is 1-3 seconds
    wait_time = between(1, 3)

    def on_start(self) -> None:
        """Logins and stuff before starting a user session."""
        setup.login()

    @task
    def usd_to_rs(self) -> None:
        url = "exchange"

        querystring = {"q": "1.0", "from": "USD", "to": "RS"}

        headers = {
            "x-rapidapi-host": settings.HOST,
            "x-rapidapi-key": settings.API_TOKEN,
        }

        with self.client.get(
            url,
            headers=headers,
            params=querystring,
            catch_response=True,
        ) as response:
            if response.status_code == HTTPStatus.OK:
                response.success()
            else:
                response.failure(f"Failed! Http Code `{response.status_code}`")

    @task
    def rs_to_usd(self) -> None:
        url = "exchange"

        querystring = {"q": "1.0", "from": "RS", "to": "USD"}

        headers = {
            "x-rapidapi-host": settings.HOST,
            "x-rapidapi-key": settings.API_TOKEN,
        }

        with self.client.get(
            url,
            headers=headers,
            params=querystring,
            catch_response=True,
        ) as response:
            if response.status_code == HTTPStatus.OK:
                response.success()
            else:
                response.failure(f"Failed! Http Code `{response.status_code}`")

    @task
    def stop(self) -> None:
        """TaskSet objects don't know when to hand over control
        to the parent class. This method does exactly that."""

        self.interrupt()

    def on_stop(self) -> None:
        """Logout and stuff after ending a user session."""
        setup.logout()
