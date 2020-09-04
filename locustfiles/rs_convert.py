from locust import TaskSet, between, task

from commons.auth import login, logout


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
            "x-rapidapi-host": "currency-exchange.p.rapidapi.com",
            "x-rapidapi-key": "d26533cbe8msh020600a07386d87p18a610jsn31d39f87f802",
        }

        self.client.get(url, headers=headers, params=querystring)

    @task
    def rs_to_usd(self):
        url = "exchange"

        querystring = {"q": "1.0", "from": "RS", "to": "USD"}

        headers = {
            "x-rapidapi-host": "currency-exchange.p.rapidapi.com",
            "x-rapidapi-key": "d26533cbe8msh020600a07386d87p18a610jsn31d39f87f802",
        }

        self.client.get(url, headers=headers, params=querystring)

    @task
    def stop(self):
        """TaskSet objects don't know when to hand over control
        to the parent class. This method does exactly that."""

        self.interrupt()

    @task
    def on_stop(self):
        """Logout and stuff after ending a user session."""
        logout()
