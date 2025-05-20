from pyrogram import Client, filters
from utils import process_txt, process_url
import os

api_id = 1234567
api_hash = "your_api_hash"
bot_token = "your_bot_token"

app = Client("drm-bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.document & filters.private)
async def handle_file(client, message):
    if message.document.file_name.endswith(".txt"):
        path = await message.download()
        await message.reply("Processing your file...")
        await process_txt(path, message)

@app.on_message(filters.text & filters.private)
async def handle_text(client, message):
    if message.text.startswith("http"):
        await message.reply("Processing URL...")
        await process_url(message.text, message)
