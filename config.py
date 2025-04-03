# Don't Remove Credit
# TitanXBots
# Dev - Yash



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7383779126:AAF2kIhS2tquCHUeRmYyPtpgs8lcnz-VHGQ")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "15671595"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "bb8f36f9c39a24c7f8b2acbc7ea8c60a")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002515386092"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "8075224687"))

#Port
PORT = os.environ.get("PORT", "8080")

#File Auto Delete
FILE_AUTO_DELETE = int(os.environ.get("FILE_AUTO_DELETE", "2700")) # auto delete in seconds


#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://anikush8310:RCB@cluster0.ig7xtt0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Titanxbot") # Don't Change Database Name

#force sub channel id, if you want to enable force sub (Use different ForceSub Channel ID)
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1002250501843"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1001966939371"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "-1002040318000"))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "-1002698579732"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/_k7.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/jI7.jpg") 

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀɴ ꜰɪʟᴇꜱᴛᴏʀᴇ ʙᴏᴛ ᴛᴏ ꜱᴛᴏʀᴇ ᴀɴᴅ ꜱʜᴀʀᴇ - ꜰɪʟᴇꜱ, ᴅᴏᴄᴜᴍᴇɴᴛꜱ, ᴇᴛᴄ..... \n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ 𝟦 ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!</b>"
ABOUT_TXT = "<b>✯ Creator : <a href='https://t.me/HK_Kushal'>This Person</a>\n✯ Language : <code>Python3</code>\n✯ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio</a>\n✯ Source Code : <a href='https://t.me/+ymTUr8GqUZZlZmJl'>Click Here</a>\n✯ Channel : @Hari_Backup\n✯ Request Group : @Hari_Searchx</b>"
START_MSG = os.environ.get("START_MESSAGE", "ʜᴇʏ ʜɪɪ ᴅᴇᴀʀ {first}\n\nI ᴄᴀɴ ꜱᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇꜱ ɪɴ ꜱᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜꜱᴇʀꜱ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ɪᴛ ғʀᴏᴍ ꜱᴘᴇᴄɪᴀʟ ʟɪɴᴋ./n/n𝗜𝗙 𝗬𝗢𝗨 𝗡𝗘𝗘𝗗 𝗧𝗢 𝗨𝗦𝗘 𝗙𝗢𝗥 𝗣𝗘𝗥𝗦𝗢𝗡𝗔𝗟 𝗖𝗢𝗡𝗧𝗔𝗖𝗧 𝗢𝗪𝗡𝗘𝗥 𝗛𝗘𝗥𝗘 😜 @Harikushal")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "8075224687").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʏ ʜɪɪ ᴅᴇᴀʀ {first}\n\n<b>ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ɪᴏɪɴ ɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ ᴛᴏ ᴜꜱᴇ ᴍᴇ\n\nKindly ᴘʟᴇᴀꜱᴇ ɪᴏɪɴ ᴄʜᴀɴɴᴇʟ</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "👋 ʜᴇʏ ғʀɪᴇɴᴅ, 🚫 ᴅᴏɴ'ᴛ ꜱᴇɴᴅ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇꜱ ᴛᴏ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ'ᴍ ᴏɴʟʏ ғɪʟᴇ ꜱʜᴀʀᴇ ʙᴏᴛ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(8075224687)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
