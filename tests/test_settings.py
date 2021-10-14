from unittest.mock import patch


@patch.dict(
    "src.settings.os.environ",
    {"HOST": "dummy_host", "API_TOKEN": "dummy_api_token"},
)
@patch("src.settings.load_dotenv", autospec=True)
def test_envvars(load_dotenv):
    from src import settings

    assert settings.os.environ["HOST"] == "dummy_host"
    assert settings.os.environ["API_TOKEN"] == "dummy_api_token"
