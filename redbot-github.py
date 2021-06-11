import praw
import pdb
import re
import os
import time
import random
import json

def rnumber():
    return random.randint(10000000,1000000000000)

def xtime():
    t = time.localtime()
    return time.strftime("%Y/%m/%d %H:%M:%S", t)

def dumpdict():
    return json.dumps(reddit.auth.limits)    

  

def checksub(subname):
    subreddit = reddit.subreddit(subname)   
    lg.write(xtime() + " " + subname + "\n")
    lg.write(xtime() + " " + dumpdict() + "\n")
    print(xtime() + " " + subname + "\n")
    print(xtime() + " " + dumpdict() + "\n")
    for submission in subreddit.new(limit=100):
        #lg.write(subname + "-->" + submission.title + "\n")
        if submission.id not in posts_replied_to:
            if re.search("search-tearm in post title", submission.title, re.IGNORECASE):
                submission.reply("This is comment you want to leave on posts." + str(rnumber()))
                lg.write(xtime() + " bot comment : " + submission.id + "," + submission.title + "" + dumpdict() + "\n")
                print(xtime() + " bot comment : " + submission.id + "," + submission.title + "" + dumpdict() + "\n")
                posts_replied_to.append(submission.id)
    
#list of subs you want to search
subs = ['BSCcryptoListings', 'CryptoCurrencyTrading', 'pancakeswapgems', 'CryptoMars', 'Cryptopumping', 'CryptoMoon', 'MarsWallStreet', 'CryptoMoonRocks', 'shitcoin', 'CryptoMarsShots', 'AllCryptoBets', 'shitcoinpotential', 'cryptomooncalls', 'cryptostreetbets', 'cryptomooncoins']


reddit = praw.Reddit('bot1')

      

while True:
    for sub in subs:
        if not os.path.isfile("posts_replied_to.txt"):
          posts_replied_to = []
        else:
          with open("posts_replied_to.txt", "r") as f:
              posts_replied_to = f.read()
              posts_replied_to = posts_replied_to.split("\n")
              posts_replied_to = list(filter(None, posts_replied_to))

        lg=open("redbot.log", "a")
        lg.write(xtime() + "Start " + sub + " Run at " + "\n") 
        print(xtime() + "Start " + sub + " Run at " + "\n") 

        checksub(sub)
        
    
        
        with open("posts_replied_to.txt", "w") as f:
            for post_id in posts_replied_to:
                f.write(post_id + "\n")
                print(post_id)
        lg.close()
        print("sleeping")
        time.sleep(550)

