import os
import subprocess
from pyrogram.types import Message

async def process_txt(filepath, message: Message):
    with open(filepath, "r") as f:
        urls = f.read().splitlines()
    for url in urls:
        await process_url(url, message)

async def process_url(url, message: Message):
    if "mpd" in url:
        if "key=" in url:
            mpd, key = url.split("?key=")
            kid, k = key.split(":")
            cmd = f'yt-dlp -k --external-downloader ffmpeg --downloader-args "mpd:-headers User-Agent:Mozilla" "{mpd}" -o "output.mp4"'
        else:
            cmd = f'yt-dlp "{url}" -o "output.mp4"'
    elif "m3u8" in url:
        cmd = f'ffmpeg -i "{url}" -c copy output.mp4'
    else:
        cmd = f'yt-dlp "{url}" -o "output.mp4"'

    subprocess.run(cmd, shell=True)

    if os.path.exists("output.mp4"):
        size = os.path.getsize("output.mp4") / (1024 * 1024)
        if size <= 50:
            await message.reply_video("output.mp4")
        else:
            await message.reply_document("output.mp4", caption=f"File is {int(size)}MB")
        os.remove("output.mp4")
