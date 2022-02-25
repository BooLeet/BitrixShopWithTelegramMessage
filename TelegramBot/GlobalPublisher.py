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

messageString = str()
argumentCount = len(sys.argv)
for i in range(1, argumentCount):
    messageString += str(sys.argv[i]) + " "

for user in users: 
    updater.bot.send_message(chat_id = int(user),text = messageString)