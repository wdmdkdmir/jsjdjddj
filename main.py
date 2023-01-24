import random

import time

import telepot

bot = telepot.Bot('5869707878:AAGSnac4xeme7HdSRZzElz0-CKp8nkrMlg8') # Telegram Bot Token'ını buraya girin

def action(msg):

    chat_id = msg['chat']['id']

    message = msg['text']

    if message.startswith('/tag'):

        tag_message = message[5:]

        members = bot.getChatMembersCount(f'-{chat_id}')

        while True:

            time.sleep(30)

            member = random.randint(0, members - 2)

            bot.sendMessage(chat_id, f'@{member} {tag_message}', 'Markdown')

            if message and message["text"] == "/stop":

                bot.sendMessage(chat_id, "Etiket atma işlemi durduruldu.")

                break

bot.message_loop(action)

print('Bot çalışıyor...')
