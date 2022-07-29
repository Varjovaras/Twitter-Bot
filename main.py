import time
import schedule
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()


def bot():
    private_key = os.getenv("CONSUMER_KEY")
    private_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_secret = os.getenv("ACCESS_SECRET")

    auth = tweepy.OAuthHandler(
        private_key, private_secret)

    auth.set_access_token(
        access_token, access_secret)
    api = tweepy.API(auth)

    # Upload image
    media = api.media_upload("perstai.jpg")
    # Post tweet with image
    tweet = "Perstai"
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])
    print(post_result)


schedule.every().friday.at("9:30").do(bot)
while True:
    schedule.run_pending()
    time.sleep(1)
    print("\nGMT: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
