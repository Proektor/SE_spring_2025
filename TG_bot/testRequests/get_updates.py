import requests
from config import token


def get_updates(token):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url)
    return response.json()


# Пример использования
print(get_updates(token))
