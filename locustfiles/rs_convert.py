from locust import TaskSet, between, task

from common import settings
from common.auth import login, logout


class RSConvert(TaskSet):
    """Converting from Dollar to RS & vice versa."""

    # Time period between firing consecutive tasks is 1-3 seconds
    wait_time = between(1, 3)

    def on_start(self):
        """Logins and stuff before starting a user session."""
        login()

    @task
    def usd_to_rs(self):
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
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed! Http Code `{response.status_code}`")
        return

    @task
    def rs_to_usd(self):
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
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed! Http Code `{response.status_code}`")
        return

    @task
    def stop(self):
        """TaskSet objects don't know when to hand over control
        to the parent class. This method does exactly that."""

        self.interrupt()

    def on_stop(self):
        """Logout and stuff after ending a user session."""
        logout()
