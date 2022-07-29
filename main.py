import time
import schedule
import tweepy


def bot():
    twitter_auth_keys = {
        "consumer_key": "85vgIXBt6Wie3chd7A8UoMeH7",
        "consumer_secret": "YqZZoqqWHFTrsBESQpD0sf1WVdN5X748F36hkRHGnhv5lwcvXj",
        "access_token": "1519627575051669504-IrYi0bKZjvtL7XoE2C8K1iLhZqk4gm",
        "access_token_secret": "GWAzL1AXOPoHCxR9tgYdhtvQU1P9snPUY3pdL5GAbp7ZZ"
    }

    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )
    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )
    api = tweepy.API(auth)

    # Upload image
    media = api.media_upload("perstai.jpg")
    # Post tweet with image
    tweet = "Perstai"
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])


def testbot():
    print(";:D")


schedule.every().friday.at("10:48").do(bot)
while True:
    schedule.run_pending()
    time.sleep(1)
    print("\nGMT: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
