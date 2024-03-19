import telebot
import os
from urllib.parse import urlparse
from insta_loader import download_media
from config import TELEGRAM_BOT_TOKEN

# Initialize the Telegram bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.text == '/start':
        bot.reply_to(message, "Welcome! Send me the Instagram reel or post link to download.")
    elif message.text == '/help':
        help_text = (
            "To use this bot, simply send me the link of the Instagram reel or post you want to download.\n\n"
            "Here's an example:\n"
            "1. Go to Instagram and copy the link of the reel or post you want to download.\n"
            "2. Send me the copied link by pasting it here.\n\n"
            "Note: Only Instagram reel and post links are supported."
        )
        bot.reply_to(message, help_text)

@bot.message_handler(func=lambda message: True)
def download_and_send_media(message):
    try:
        media_url = message.text

        # Check if the URL is a valid Instagram reel, reels, or post link
        parsed_url = urlparse(media_url)
        if not (parsed_url.scheme and parsed_url.netloc and ("/reel/" in media_url or "/reels/" in media_url or "/p/" in media_url)):
            bot.reply_to(message, "Please provide a valid Instagram reel or post link. Type /help for assistance.")
            return

        filename, ext = download_media(media_url)

        if filename and ext:
            if ext == '.jpg':
                # If the downloaded media is an image, send it as a photo
                with open(filename, 'rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            elif ext == '.mp4':
                # If the downloaded media is a video, send it as a video
                with open(filename, 'rb') as video:
                    bot.send_video(message.chat.id, video)

            # Delete the downloaded media file after sending
            os.remove(filename)
        else:
            bot.reply_to(message, "Failed to download the media.")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")


# Start the bot
bot.polling()
