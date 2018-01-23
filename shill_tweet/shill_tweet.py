import twitter
from twilio.rest import Client
from api_keys import *

client = Client(ACCOUNT_SID, AUTH_TOKEN)

api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                  consumer_secret=TWITTER_CONSUMER_SECRET,
                  access_token_key=TWITTER_ACCESS_TOKEN_KEY,
                  access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

t = api.GetUserTimeline(screen_name="officialmcafee", count=1)

tweets = [i.AsDict() for i in t]

# tweets = [{'created_at': 'Sat Dec 23 22:45:52 +0000 2017', 'favorite_count': 1093, 'hashtags': [], 'id': 944700613618782208, 'id_str': '944700613618782208', 'lang': 'en', 'retweet_count': 197, 'source': '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', 'text': 'Coin of the day: Junkycoins (DGB). Using a Blockchain which is 40 times faster than Bitcoin and having one of the most decentralized mining systems in the world - based on 5 different synergistic algorithms. DGB adherents call the coin', 'truncated': True, 'urls': [{'expanded_url': 'https://twitter.com/i/web/status/944700613618782208', 'url': 'https://t.co/fcWZtAClvW'}], 'user': {'created_at': 'Wed Nov 21 00:03:03 +0000 2012', 'description': 'Tech Pioneer, Chief Cybersecurity Visionary of MGT. Trustee - Keep This Bastard Alive fund.', 'favourites_count': 12425, 'followers_count': 345662, 'following': True, 'friends_count': 12105, 'id': 961445378, 'lang': 'en', 'listed_count': 3008, 'location': 'House McAfee', 'name': 'John McAfee', 'notifications': True, 'profile_background_color': 'FFFFFF', 'profile_background_image_url': 'http://pbs.twimg.com/profile_background_images/463138421511168000/3E83MZd8.png', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/961445378/1466659018', 'profile_image_url': 'http://pbs.twimg.com/profile_images/722878117967036416/2MOt13No_normal.jpg', 'profile_link_color': 'FAB81E', 'profile_sidebar_fill_color': 'C0DFEC', 'profile_text_color': '088253', 'screen_name': 'officialmcafee', 'statuses_count': 8072, 'time_zone': 'Pacific Time (US & Canada)', 'utc_offset': -28800, 'verified': True}, 'user_mentions': []}]

latest_tweet = tweets[0]["text"]

def shill_tweet():
    if 'Coin of the week' in latest_tweet:
        return True

def send_message():
    client.messages.create(
        to=TO_NUMBER, 
        from_=FROM_NUMBER,
        body=coin_name)

if shill_tweet():
    coin_name = latest_tweet.split(":")[1].strip().split(" ")[0].lower()
    file2write=open("tweet_data.txt",'r')
    file_coin = file2write.read()
    file2write.close()
    if coin_name != file_coin:
        send_message()    
        file2write=open("tweet_data.txt",'w')
        file2write.write(coin_name)
        file2write.close()

