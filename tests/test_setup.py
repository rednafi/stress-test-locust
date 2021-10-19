from src import setup


def test_login(capsys):
    setup.login()
    out, err = capsys.readouterr()

    assert err == ""
    assert "logging in..." in out.lower()


def test_logout(capsys):
    setup.logout()
    out, err = capsys.readouterr()

    assert err == ""
    assert "logging out..." in out.lower()
