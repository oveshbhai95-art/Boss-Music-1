import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "ʙᴏss ᴍᴜsɪᴄ")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/6790864f5fe27471bdc8d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/e9a4d6655e5ddf51f9160.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/91034f175d41040d45b38.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c8a0e9c544c5ea689caf9.jpg")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "BossMusicSpotifyBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "OnlyBossManager")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "OnlyBossMoviesGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "OveshBossOfficial")
OWNER_NAME = getenv("OWNER_NAME", "Ovesh_Boss") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("1416433622")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("mongodb+srv://Ovesh:ovesh.boss@ovesh.95jpp8g.mongodb.net/?retryWrites=true&w=majority&appName=Ovesh") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("-1003166629808")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
