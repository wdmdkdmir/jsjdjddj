import random
import time
import telepot
from telepot.loop import MessageLoop

bot = telepot.Bot('5869707878:AAGSnac4xeme7HdSRZzElz0-CKp8nkrMlg8') # Telegram Bot Token'ını buraya girin

def action(msg):
    chat_id = msg['chat']['id']
    message = msg['text']
    if message.startswith('/tag'):
        tag_message = message[5:]
        members = bot.getChatMembersCount(chat_id)
        while True:
            time.sleep(30)
            member = random.randint(0, members - 1)
            bot.sendMessage(chat_id, f'@{member} {tag_message}', 'Markdown')

MessageLoop(bot, action).run_as_thread()
print('Bot çalışıyor...')