import os

class Config:
    API_ID = int( os.getenv("api_id","16612056") )
    API_HASH = os.getenv("api_hash","ae32caf162207865ff93b9b931b2ba54")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1001792892962") )
    CHANNEL_USERNAME = os.getenv("channel_username","forjoim777888")
    TOKEN = os.getenv("token","5305336110:AAHyDsa9_exGaOTyv8qDxaw_U0Z1BOO-zYM")
    DOMAIN  = os.getenv("domain","http://d4.kimo.vip")
