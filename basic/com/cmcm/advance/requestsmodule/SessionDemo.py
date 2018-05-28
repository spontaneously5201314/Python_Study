import requests


def test_session():
    session = requests.session()
    session.get("http://www.renren.com/PLogin.do")
    session.post()


assert 1 == 3
