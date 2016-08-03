import threading
from twitter_follow_bot import auto_follow_followers_for_user
from twitter_follow_bot import auto_fav
from twitter_follow_bot import auto_unfollow_nonfollowers

def ball():
  threading.Timer(3600.0, ball).start()
  auto_follow_followers_for_user("streamernews", count=20)
  auto_follow_followers_for_user("gamewisp", count=20)
  #auto_unfollow_nonfollowers()
  print "Vape is life"

ball()


