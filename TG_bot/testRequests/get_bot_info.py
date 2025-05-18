import requests
from config import token


def get_bot_info(token):
    url = f"https://api.telegram.org/bot{token}/getMe"
    response = requests.get(url)
    return response.json()


# Пример использования
<<<<<<< HEAD
=======
token = ""
>>>>>>> 88c1b837883e02ac5b23c9ca7e0f08daaf3dac37
print(get_bot_info(token))
