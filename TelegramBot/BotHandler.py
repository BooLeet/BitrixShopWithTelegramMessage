import telegram.ext
import telegram
import json

users = set()
try:
    with open('users.txt', 'r') as f:
        if(len(f.read()) > 0):
            users = set(json.loads(f.read()).keys()) 
except IOError:
    print("No prior users found")

def addUser(user):
    users.add(str(user.id))
    print(f"New user: id: {str(user.id)} {user.first_name} {user.last_name}")
    with open('users.txt', 'w+')  as usersFile:
        usersFile.write(json.dumps(dict.fromkeys(users, 0)))

def start(update, context):
    update.message.reply_text("Добро пожаловать")
    update.message.reply_text("Список комманд: /help")
    addUser(update.message.from_user)

def help(update, context):
    update.message.reply_text("""
/start -> Запустить бота заново
/anecdote -> Запросить анекдот
    """)

def anecdote(update, context):
    update.message.reply_text("Идет медведь по лесу, видит машина горит. Сел в неё и сгорел")

def handle_message(update, context):
    update.message.reply_text(f"Эхо: {update.message.text}")

def picture(update, context):
    update.message.reply_pic

with open('token.txt', 'r') as f:
    TOKEN = f.read()

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("anecdote", anecdote))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()