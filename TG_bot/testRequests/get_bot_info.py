import requests


def get_bot_info(token):
    url = f"https://api.telegram.org/bot{token}/getMe"
    response = requests.get(url)
    return response.json()


# Пример использования
token = "7709538685:AAH3nikbdFya1SUGi16SkWoocf7aFLsnIj8"
print(get_bot_info(token))
