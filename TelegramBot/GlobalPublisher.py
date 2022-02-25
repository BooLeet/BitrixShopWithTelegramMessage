import telegram.ext
import telegram
import json
import sys

users = set()
try:
    with open('users.txt', 'r') as f:
        users = set(json.loads(f.read()).keys()) 
except IOError:
    print("No prior users found")

with open('token.txt', 'r') as f:
    TOKEN = f.read()

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

argumentCount = len(sys.argv)

def sendTextMessage():
    messageString = str()
    for i in range(2, argumentCount):
        messageString += str(sys.argv[i]) + " "

    for user in users: 
        updater.bot.send_message(chat_id = int(user),text = messageString)

def sendImageURL():
    for user in users: 
        for i in range(2, argumentCount):
            updater.bot.send_photo(chat_id = int(user),photo = sys.argv[i])

def sendImageFile():
    for user in users: 
        for i in range(2, argumentCount):
            updater.bot.send_photo(chat_id = int(user),photo = open(sys.argv[i], 'rb'))

def sendAudioFile():
    for user in users: 
        for i in range(2, argumentCount):
            updater.bot.send_audio(chat_id = int(user),audio = open(sys.argv[i], 'rb'))

if(sys.argv[1] == "txt"):
    sendTextMessage()
elif(sys.argv[1] == "imgURL"):
    sendImageURL()
elif(sys.argv[1] == "img"):
    sendImageFile()
elif(sys.argv[1] == "audio"):
    sendAudioFile()
else:
    print("Invalid format argument. Legal arguments: txt, img, imgURL, audio)")

