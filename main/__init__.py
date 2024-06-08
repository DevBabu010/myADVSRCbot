
#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

# variables
API_ID = "18532876" #config("API_ID", default=None, cast=int)
API_HASH = "c8be256015a242035196e801108af49f"#config("API_HASH", default=None)
BOT_TOKEN = "7309599729:AAHbypsWgcon-sBbYKIPmhswhm9upMPenro"#config("BOT_TOKEN", default=None)
SESSION = "BQEaygwAEs1mguh-oniSkeUb7sjRk6-AiquYaVsNadEWRknvRUJ0H9QUDCTy7RuFINBknbUPqU7pgmp1AXYMUhzHwbfHLpB909TfB2jcgs7sk2z-cIli20Wk9Bq-2IUSD-fB9NrwMulOhTsWJDXIDUZd6K9zcUoyr1Mc0_Svo0EXCTefsJ8l9SM1hHq9CieuS93w_k0_QKBmVbqPJPliqgJuvcbdmjCHtD4XzGsgU8orMMh56Zjpih7LZ6q6GEBgfU-UE73meU7gWSrDrhawRMKx1HnllXepu77RNf2MqzQLRqlRQexj1Hwf83bNOvuhlQz_srUhwp19LxPjVC2-Gf463yYmzgAAAAGzr6PxAQ"#config("SESSION", default=None)
FORCESUB = "premium_books_pdfs" #config("FORCESUB", default=None)
AUTH = "1466653662" #config("AUTH", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    # print(e)
    # logger.info(e)
    sys.exit(1)
