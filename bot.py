import telepot
from telepot.loop import MessageLoop

TOKEN = '5496954434:AAHcqE5uM4gCGZr-_3da7dV-Lb7vDvNO02w'
bot = telepot.Bot(TOKEN)


def handle(msg):
    """ Process request like '3+2' """
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg["text"]
    try:
        answer = eval(text)
    except:
        answer = "Can't calculate :("
    bot.sendMessage(chat_id, "answer: {}".format(answer))


MessageLoop(bot, handle).run_as_thread()

while True:
    n = input('To stop enter "stop":')
    if n.strip() == 'stop':
        break
