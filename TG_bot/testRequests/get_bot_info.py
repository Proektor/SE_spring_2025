import requests
from config import token


def get_bot_info(token):
    url = f"https://api.telegram.org/bot{token}/getMe"
    response = requests.get(url)
    return response.json()


# Пример использования
print(get_bot_info(token))
