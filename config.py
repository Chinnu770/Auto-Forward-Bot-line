from os import getenv

class Config(object):
      API_HASH = getenv("4ed1b0d3f9394927baac66bcae1a4d53")
      API_ID = int(getenv("29219263", 0))      
      BOT_TOKEN = getenv("BOT_TOKEN", "6981391198:AAEGTS8rkYYmBdYolW1H2Z2AUDNTZ9_LY2Q")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001711858115:-1001894380790 -1001925306151 -1002101664566 -1001952248822 -1002034415698").replace("\n", " ").split(' '))
