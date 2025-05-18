import requests
from config import token


def get_updates(token):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url)
    return response.json()


# Пример использования
<<<<<<< HEAD
=======
token = ""
>>>>>>> 88c1b837883e02ac5b23c9ca7e0f08daaf3dac37
print(get_updates(token))
