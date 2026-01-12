import requests
from pyrogram import Client as Bot, filters
from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN, BG_IMAGE

# --- UNIVERSAL FIX FOR 'edited' ATTRIBUTE ERROR ---
if not hasattr(filters, "edited"):
    filters.edited = filters.create(lambda _, __, ___: False)
# --------------------------------------------------

# Aapka String Session yahan define kar diya hai
STRING_SESSION = "BQJBLZQAOy4ydKZNdb336ahf4V0P86NODeLnIq_oeGJdrBkkyQtxJZqMs_dfL2G182Q5fdt4umF-WOCqke0HVzBIb9igvqdjhKlQci5FnpS8kPIazGOSGIVYlULAttLyvFp0_fji4Xv43fC6HiKAonspmBLGQo1wQGOxkv-K8vGsbpPyEbnGjKTIUrzVyqmR5IuDFSLULLP4d0c5wsE4xL6seY9YxLTO88cbWbRV0mDRILhdJ8m6ZXve3dgS70HwxEYe9btcbYVDYFnhU_fz7dkz4M-VPivvfxIBwQRoWVeKVZTpOz0sCK5tzA3KducVy6GU6Zt3WTaU3-cDR7VUiDGa7d6iwgAAAAH_5sbSAA"

response = requests.get(BG_IMAGE)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers"),
)

print("[INFO]: CYBERMUSIC STARTED!")

# Bot start karne ka sahi tarika
if __name__ == "__main__":
    bot.start()
    # Yahan humne callsmusic ko run kiya hai jo aapke assistant ko handle karega
    run()
