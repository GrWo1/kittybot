import requests

from telegram import Bot

bot = Bot(token='5302624518:AAFcQB_LQkM7FLKBBbDojsNH-e71U7rjcA0')

URL = 'https://api.thecatapi.com/v1/images/search'

chat_id = 476835623

response = requests.get(URL).json()
random_cat_url = response[0].get('url')
bot.send_photo(chat_id, random_cat_url)
