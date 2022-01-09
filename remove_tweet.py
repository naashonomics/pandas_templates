import tweepy
import traceback
from datetime import datetime 
"""
Delete All Your Tweets - Github Gist by davej
Credit: https://gist.github.com/davej/113241
Ported to Python 3 by Python Marketer: pythonmarketer.com/2020/09/13/delete-all-your-tweets-with-tweepy-and-the-twitter-api/
"""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
 
def oauth_login(consumer_key, consumer_secret):
    """Authenticate with twitter using OAuth"""
     
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()
     
    verify_code = input("Authenticate at %s and then enter you verification code here > " % auth_url) 
    auth.get_access_token(verify_code)
     
    return tweepy.API(auth)
 
def batch_delete(api):
    print("You are about to delete all tweets from the account @%s." % api.verify_credentials().screen_name)
    print("Does this sound ok? There is no undo! Type yes to carry out this action.")
    do_delete = input("> ")

    if do_delete.lower() == 'yes':
        for status in tweepy.Cursor(api.user_timeline).items():
        #for status in tweepy.Cursor(api.user_timeline, screen_name="@naashonomics", since=start_date, until=end_date).items():
            try:
                api.destroy_status(status.id)
                print("Deleted:", status.id)
            except Exception:
                traceback.print_exc()
                print("Failed to delete:", status.id)
 
if __name__ == "__main__":
    api = oauth_login(CONSUMER_KEY, CONSUMER_SECRET)
    #print("Authenticated as: %s" % api.me().screen_name)
     
    batch_delete(api)
    
    

