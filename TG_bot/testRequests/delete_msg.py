import requests
from config import token, chat_id


def delete_message(token, chat_id, message_id):
    url = f"https://api.telegram.org/bot{token}/deleteMessage"
    payload = {
        'chat_id': chat_id,
        'message_id': message_id
    }
    response = requests.post(url, data=payload)
    return response.json()


# Пример использования
message_id = "12"
print(delete_message(token, chat_id, message_id))
