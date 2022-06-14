from email import message
from winreg import EnableReflectionKey
import speech_recognition as sr
import pyttsx3
import datetime
# import pywhatkit
import requests
import bs4
import random
# import vk_api
import pyowm
import os
import config

listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

print(os.getcwd())
talk("Чем я могу вам помочь?")
print(os.getcwd())

# def vk_init():

#     token = config.vk_token

#     vk_session = vk_api.VkApi(token=token)
#     return vk_session.get_api()


def talk_weather():
    token = config.weather_token

    owm = pyowm.OWM(token)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(config.weather_city)

    weather = observation.weather
    talk(f"На улице {round(weather.temperature('celsius') ['temp'])} градусов, ветер {weather.wind()['speed']} метров в секунду")

# def get_new_messages():
#     answer = []
#     vk = vk_init()
#     conversations = vk.messages.getConversations(offset = 0, count = 20)
#     for item in conversations['items']:
#         try:
#             unread_count = item['conversation']['unread_count'] 
#             dialog_id = item['conversation']['peer']['local_id']
#             conversation = vk.messages.getHistory(
#                 peer_id = dialog_id,
#                 count = unread_count,
#                 extended = True
#             )

#             profile = conversation['profiles']['0']
#             user = f"{profile['first_name']} {profile['last_name']}"

#             messages = conversation['items']
#             messages.reverse()

#             text = ''
#             for message in messages:
#                 text += message['text'] + '\n'

#             answer.append(f"{unread_count}  сообщение от пользователя {user}:\n{text}")    
#         except:
#             pass    
#     return answer    

# def check_vk():
#     messages = get_new_messages()
#     if len(messages) > 0:
#         for message in messages:
#             talk(message)
#     else:
#         talk(f'Нет новых сообщений, {config.user_name}!')        

# def write_message_vk(user, msg):
#     vk = vk_init()

#     try:
#         friends = vk.friends.search(user_id = config.vk_id, q = user)
#         friend_id = friends['itens'][0]['id']
#         vk.messages.send(user_id = friend_id, message = msg, random_id = 0)
#     except IndexError:
#         talk('Извините, я не смог найти такого пользователя')

def tell_time():
    time = datetime.datetime.now()
    time = time.strftime("%I:%M")
    talk(time)

def tell_date():

    date = datetime.datetime.now()
    day = int(date.strftime("%d"))
    mon = int(date.strftime("%m"))
    year = int(date.strftime("%Y"))

    date = f"{day} {config.month[mon - 1]} {year}"
    talk(date)    

# def play_on_youtube(song):
#     talk(f"Включаю {song}")
#     pywhatkit.playonyt(song) 

def get_anekdot():
    joke = requests.get(config.jokes_url)
    soup = bs4.BeautifulSoup(joke.text, 'html.parser')

    jokes = soup.select('.anekdot_text')
    index = random.randrange(len(jokes))
    joke_text = jokes[index].get_text().strip()
    return joke_text

def tell_joke():
    talk("Внимание, анекдот!")
    joke_text = get_anekdot()
    talk(joke_text)

def turn_radio():
    talk("Включаю радио")

#    path = os.path.abspath(os.path.dirname(__file__))
#    os.cndir(path)

    os.system('top_radio_folk.m3u')
    

with sr.Microphone() as source:
    listener.adjust_for_ambient_noise(source)

def take_command():
    try:
        with sr.Microphone() as source:
            print('Слушаем...')
            voice = listener.listen(source, timeout=1, phrase_time_limit=2)
            command = listener.recognize_google(voice, language='ru-RU').lower()
            for name in config.names:
                if name in command:
                    talk(f'Чем могу быть полезен, {config.user_name}')
                    return take_voice()
    except:
        pass
    return ''   


def take_voice():
    try:
        with sr.Microphone() as source:
            print('Слушаем...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='ru-RU').lower()
            return command
    except:
        pass
    return '' 

def run():
    command = take_command()
    if "привет" in command:
        talk(f"Приветствую вас, {config.user_name}")
    elif "время" in command:
        tell_time()
    elif "число" in command:       
        tell_date()
    # elif "включи" in command:
    #     song = command.replace("включи", "")
    #     play_on_youtube(song)
    elif "анекдот" in command:
         tell_joke()
    # elif "проверь вконтакте" in command:
    #     check_vk()
    # elif "Напиши вконтакте" in command:
    #     talk('Кому вы хотите написать сообщение?')
    #     user = take_voice()
    #     talk('Что вы хотите написать?')
    #     message = take_voice()
    #     write_message_vk(user, message)   
    elif "погода" in command:
        talk_weather()
    elif "запусти радио" in command:
        turn_radio()
while True:
    run()
