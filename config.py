# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29538829"))
API_HASH = getenv("API_HASH", "0098baaaa11b512a0a8b8eaf33a4d91a")
BOT_TOKEN = getenv("BOT_TOKEN", "7884852517:AAFCJx89DDD9awSkK6rnaBy9R4IAjxSKIww")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1118716436").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://kingrajashish43211:rOYviMdPMPfCvSlR@cluster0.j3o3sbf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002552274394"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
