import requests
from config import token, chat_id


def send_photo(token, chat_id, photo_url, caption=""):
    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    payload = {
        'chat_id': chat_id,
        'photo': photo_url,
        'caption': caption
    }
    response = requests.post(url, data=payload)
    return response.json()


# Пример использования
base_url = "https://unsplash.com/photos/"
img_name = "brown-and-white-owl-in-close-up-photography-2VsPnDt2SQs"
photo_url = base_url + img_name
caption = "Сова"
print(send_photo(token, chat_id, photo_url, caption))
