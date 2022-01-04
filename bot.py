import tweepy 

API_KEY = ''
API_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_SECRET_TOKEN = ''

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY0)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
api = tweepy.API(auth)

FILE = "id.text"

def retrieve_id(file):
    f_read = open(file, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

    def store_id(id, file):
        f_write = open(file, "w")
        f_write.write(str(id))
        f_write.close()
        return
    
    last_seen_id = retrieve_id(FILE)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode = "extended")

for mentions in api.mentions_timeline(mentions):
    if "solidity":"ETHDEV","Reactjs" in mentio.full_text:
        store_id(last_seen_id, FILE)
        api.update_status('@'+mention.user.screen_name + 'The future is here, learning is important', mentions)
        print('replied to @' + mention.user.screen_name)

for mention in mentions:
    print(mention.id)
