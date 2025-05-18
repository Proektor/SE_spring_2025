import requests


def get_bot_info(token):
    url = f"https://api.telegram.org/bot{token}/getMe"
    response = requests.get(url)
    return response.json()


# Пример использования
token = ""
print(get_bot_info(token))
