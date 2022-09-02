import time
import schedule
import tweepy
import os
from dotenv import load_dotenv


def bot():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(
        consumer_key, consumer_secret)
    auth.set_access_token(
        access_token, access_secret)
    api = tweepy.API(auth)

    print("Tweeting perstai")
    # Upload image
    media = api.media_upload("perstai.jpg")
    # Post tweet with image
    tweet = "Perstai"
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])
    print(post_result)


def schedule_testprint(text):
    print(text)
    print(time.localtime(time.time()))
    print(time.asctime(time.localtime(time.time())))
    print(":)")


print("Deployed")

load_dotenv()


schedule.every().friday.at("12:16").do(bot)


while True:
    schedule.run_pending()
    time.sleep(1)
    print("\nGMT: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
