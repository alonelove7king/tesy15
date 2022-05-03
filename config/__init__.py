import os

class Config:
    API_ID = int( os.getenv("api_id","392800") )
    API_HASH = os.getenv("api_hash","f7f4316dac3b4959687b46860b44c265")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1001631982458") )
    CHANNEL_USERNAME = os.getenv("channel_username","King_network7")
    TOKEN = os.getenv("token","2045343811:AAH2YutndTCYokHpkk_rn83CeAivJSMIOa0")
    DOMAIN  = os.getenv("domain","https://d4.kimo.vip")
