import requests
from config import token, chat_id


def get_chat_info(token, chat_id):
    url = f"https://api.telegram.org/bot{token}/getChat"
    params = {
        'chat_id': chat_id
    }
    response = requests.get(url, params=params)
    return response.json()


# Пример использования
print(get_chat_info(token, chat_id))
