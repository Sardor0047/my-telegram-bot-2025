# Get toke from the environment variable
import os
from telegram import Bot
token = os.getenv("TOKEN")

CHAT_ID = "1992257967"
bot = Bot(token)

video_url = 'https://www.sample-videos.com/video/mp4/720/big_buck_bunny_720p_10mb.mp4'
#response = bot.send_video(CHAT_ID,video_url,caption='Bunny ')

#audio = bot.send_audio(CHAT_ID, 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')

#message = bot.send_message(CHAT_ID,'Salom')

#photo = bot.send_photo(CHAT_ID,"https://ih1.redbubble.net/image.2464906586.5278/raf,360x360,075,t,fafafa:ca443f4786.jpg")

#document = bot.send_document(CHAT_ID, "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf")

#voice = bot.send_voice(CHAT_ID,'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')

update = bot.get_updates()
