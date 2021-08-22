import telegram
from riotwatcher import LolWatcher
from telegram.ext import Updater, CommandHandler
from datetime import datetime, timedelta
import time

### Variable number
api_key = 'tele  api'
token = api_key

bot = telegram.Bot(token=token)
updates = bot.getUpdates()
chat_id = 'Your telegram id(number)'

updater = Updater(token=token)
dispatcher = updater.dispatcher

lol_watcher = LolWatcher('Your LOL API')

my_region = 'Your region'
nickname = 'Your nickname'

me = lol_watcher.summoner.by_name(my_region, nickname)


spectator = None

### Running program
bot.send_message(chat_id=chat_id, text='Program is running..')


# help
def help(update, context):
    context.bot.send_message(chat_id=chat_id, text='/help 도움 사항\n/사람 이름 플레이 상황\n(명령어:/me, /SY, /MS)')

# Searching me
def me(update, context):
    while True:
        bot.sendMessage(chat_id= chat_id, text=f"[*]Monitoring.. {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        try:
            spectator = lol_watcher.spectator.by_summoner(my_region, me['id'])

            start_time = datetime.fromtimestamp(spectator['gameStartTime'] / 1000)

            if datetime.now() - start_time < timedelta(minutes=5):
                bot.sendMessage(chat_id=chat_id,
                                text=f"HE IS PLAYING LOL! , {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

        except:
            pass

        time.sleep(5)




help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

me_handler = CommandHandler('me', me)
dispatcher.add_handler(me_handler)

updater.start_polling()
updater.idle()




