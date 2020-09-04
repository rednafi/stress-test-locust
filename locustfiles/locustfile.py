from locust import HttpUser

from locustfiles.bdt_convert import BDTConvert
from locustfiles.rs_convert import RSConvert


class PrimaryUser(HttpUser):
    tasks = [BDTConvert, RSConvert]
