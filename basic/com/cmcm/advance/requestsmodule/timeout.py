import requests
from retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
}


@retry(stop_max_attempt_number=7)
def get_url(url):
    print("*****************")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        assert response.status_code == 200
    except Exception as e:
        print("报错了", e)


if __name__ == '__main__':
    html = get_url("www.baidu.com")
