counterURL = "URL"
import time
from random import randint
import datetime
import urllib.request
count = 13
deviation = 2
totalDeviation = 2*deviation
period = count*60 # 13 for 15 minutes average

def downloader(url,name):
    urllib.request.urlretrieve(url,name)

# CREATE A LOOP THAT RUNS AROPUND EVERY 15 MINUTES WITH A RANDOM COMPONENT OF 2 OR 3 MINUTES
i = 0
while True:
    time.sleep(period) # RUNS AN AMOUNT OF TIME DETERMINED ABOVE
    amountMinutes = randint(0,totalDeviation-1) # CREATES A RANDOM INTEGER FOR MINUTES TO AVOID IDENTIFICATION
    amountSeconds = randint(0,60) # CREATES A RANDOM INTEGER FOR SECONDS TO AVOID IDENTIFICATION
    pseudorandom = amountMinutes*60+amountSeconds # PUTS TOGETHER THE TIME
    time.sleep(pseudorandom) # SLEEPS FOR ADDITIONAL TIME WITH RANDOM FACTOR WITH AN AVERGE OF 2 MINUTES, 120 SECONDS
# EVERY RUN DOWNLOAD THE IMAGE FROM THE URL GIVING IT THE NAME OF THE TIME STAMP
    name = str(datetime.datetime.now())+".png"
    downloader(counterURL,name)
    i += 1
    if i >= 96:
    	False
    else:
    	continue
