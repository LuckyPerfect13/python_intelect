# import pyttsx3

# engine = pyttsx3.init()

# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[2].id)

# engine.say("Привет! Я Ваш голосовой помощник")
# engine.say("Чем я могу вам помочь?")
# engine.runAndWait()



# import datetime

# time = datetime.datetime.now()
# time = time.strftime("%I:%M")
# print(time)

# month = [
#     "Января", "Февраля", "Марта", "Апреля", 
#     "Мая", "Июня", "Июля", "Августа", "Сентября", 
#     "Октября", "Ноября", "Декабря"
# ]

# date = datetime.datetime.now()
# day = int(date.strftime("%d"))
# mon = int(date.strftime("%m"))
# year = int(date.strftime("%Y"))

# date = f"{day} {month[mon - 1]} {year}"
# print(date)



# import pywhatkit
# pywhatkit.playonyt("Let it snow Sinatra")    
# def play_on_youtube(song):
#     pywhatkit.playonyt(song)

import pywhatkit
pywhatkit.search("PyWhatKit")




# import requests
# import bs4
# import random

# joke = requests.get("https://www.anekdot.ru/random/anekdot/")
# joke = requests.get("http://anekdotme.ru/random")

# soup = bs4.BeautifulSoup(joke.text, 'html.parser')

# # jokes = soup.select('.topicbox')
# jokes = soup.select('.anekdot_text')
# index = random.randrange(len(jokes))
# joke_text = jokes[index].get_text().strip()

# print(joke_text)

#from email import message
#from itertools import count
#import profile
# import vk_api

# def vk_init():
#     token = 'access_token=6bbf684dc9cae82ad7322dce9a190dfd8142f862286fcc70fb59cb8c8d0ee9165a4f95bdeaee2cce7dcdc'

#     vk_session = vk_api.VkApi(token=token)
#     return vk_session.get_api()

# vk = vk_init()
# conversations = vk.messages.getConversations(offset = 0, count = 20)
# print()
# for item in conversations['items']:
#     try:
#         unread_count = item['conversation']['unread_count'] 
#         print(unread_count)
#         dialog_id = item['conversation']['peer']['local_id']
#         conversation = vk.messages.getHistory(
#             peer_id = dialog_id,
#             count = unread_count,
#             extended = True
#         )

#         profile = conversation['profiles']['0']
#         user = f"{profile['first_name']} {profile['last_name']}"

#         messages = conversation['items']
#         messages.reverse()

#         text = ''
#         for message in messages:
#             text += message['text'] + '\n'

#         print(f"{unread_count}  сообщение от пользователя {user}:\n{text}")    
#     except:
#         pass    



# import vk_api

# def vk_init():

#     token = 'access_token=8318ad8ca9d08360149d8d18fcb30bf549315219197cf4dedc1bb9bd311ddd24f7e070bbc457b3bcad063&expires_in'

#     vk_session = vk_api.VkApi(token=token)
#     return vk_session.get_api()

# vk = vk_init()

# name = "Moonlight Silence"
# friends = vk.friends.search(user_id = 279262184, q = name)
# friend_id = friends['itens'][0]['id']
# vk.messages.send(user_id = friend_id, message = "Привет, это сообщение отправлено через Python", random_id = 0)

# import pyowm

# token = 'dd0a9aad5414296dd99d7ec573326996'

# owm = pyowm.OWM(token)
# mgr = owm.weather_manager()
# observation = mgr.weather_at_place('Yaroslavl')

# weather = observation.weather
# print(f"На улице {round(weather.temperature('celsius') ['temp'])} градусов, ветер {weather.wind()['speed']} метров в секунду")


# import os

# os.system('top_radio_folk.m3u')
# os.execl