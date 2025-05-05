from hello import greet

def test_hello_world():
    assert "hello".upper() == "HELLO"

def test_greet():
    assert greet("QA") == "Hello, QA!"
    