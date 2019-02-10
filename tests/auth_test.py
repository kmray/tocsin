from tocsin.auth import Auth


def test_constructor():
    auth = Auth("example@example.com", "example")
    assert auth.email == "example@example.com"
    assert auth.password == "example"
