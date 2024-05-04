import os
import pyrebase 
#
from instabot import Bot

# Create an instance of the bot
bot = Bot()

# Login to your Instagram account
bot.login(username="your_username", password="your_password")

# Upload a photo with caption
bot.upload_photo("photo.jpg", caption="Check out this cool photo!")

# Logout from your Instagram account
bot.logout()
