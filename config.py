from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
app_id = 12297551
app_hash = "9d3fd6a2c52c6b01312e02a3abf9999b"
session = os.environ.get("teleson")
StrPython = TelegramClient(StringSession(session), app_id, app_hash)
StrPython.start()
