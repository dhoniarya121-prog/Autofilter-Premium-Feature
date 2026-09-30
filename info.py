import re
import os
from os import environ, getenv
from Script import script

# Utility functions
id_pattern = re.compile(r'^-?\d+$')  # optional leading minus, then digits (Telegram IDs)

def is_enabled(value, default):
    value = str(value).strip().lower()
    if value in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

def env_bool(name, default):
    """Read a boolean env var. (bool("False") is True in Python, so never use bool() on env strings.)"""
    return is_enabled(environ.get(name, str(default)), default)

def env_str(name, default):
    """Read a string env var; a missing OR blank value falls back to the default."""
    value = environ.get(name, "").strip()
    return value if value else default

def env_int(name, default):
    """Read an int env var; empty/missing -> default, garbage -> clear error."""
    value = environ.get(name, "").strip()
    if not value:
        return int(default)
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Environment variable {name} must be an integer, got: {value!r}")

def parse_ids(value):
    """Turn 'id1 id2 username' into [int, int, 'username']."""
    return [int(v) if id_pattern.match(v) else v for v in value.split()]

# ============================
# Bot Information Configuration
# ============================
SESSION = env_str('SESSION', 'royal_search')   # Session name for the bot
API_ID = env_int('API_ID', 0) # API ID from my.telegram.org
API_HASH = environ.get('API_HASH', '')  # API Hash from my.telegram.org
BOT_TOKEN = environ.get('BOT_TOKEN', "")    # Bot token from @BotFather

# ============================
# Bot Settings Configuration
# ============================
CACHE_TIME = env_int('CACHE_TIME', 300)    # Cache time in seconds (default: 5 minutes)
USE_CAPTION_FILTER = env_bool('USE_CAPTION_FILTER', True)  # Use caption filter for search results (default: True)
INDEX_CAPTION = is_enabled(environ.get('INDEX_CAPTION', environ.get('SAVE_CAPTION', 'True')), True) # Save caption db when idexing make it False if you dont use USE_CAPTION_FILTER for search results (default: True)
#Making it false will not save caption in db SO you can save some storage space


PICS = (environ.get('PICS', 'https://graph.org/file/56b5deb73f3b132e2bb73.jpg https://graph.org/file/5303692652d91d52180c2.jpg https://graph.org/file/425b6f46efc7c6d64105f.jpg https://graph.org/file/876867e761c6c7a29855b.jpg')).split()  # Sample pic
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_PHOTO = environ.get("MELCOW_PHOTO", "https://graph.org/file/56b5deb73f3b132e2bb73.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/13702ae26fb05df52667c.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4perL5EzFCCsObZALcw3osNqiNn1DbuKTjNRvc8K46IYEEKL-a_sZs9J8-g6hV8h_HfCO8_WnUIzMJ8u3s4iOmLhDWIht2xZE2CLWtywZwY8y7ZDf9llddATYPEhGSXBe8tKvfiehGnIUSPqf8wgEFPraAUIdUt6PmA-E_HLmzCmdYU987YgH3FuVtos/s1280/1e194cc0-24d1-4bef-93bd-ea7a75d632d8.png'))
FSUB_PICS = (environ.get('FSUB_PICS', 'https://graph.org/file/7478ff3eac37f4329c3d8.jpg https://graph.org/file/56b5deb73f3b132e2bb73.jpg')).split()  # Fsub pic

# ============================
# Admin, Channels & Users Configuration
# ============================
ADMINS = parse_ids(environ.get('ADMINS', '')) # Replace with the actual admin ID(s) to add
CHANNELS = parse_ids(environ.get('CHANNELS', '-1004398129971'))  # Channel id for auto indexing (make sure bot is admin)

LOG_CHANNEL = env_int('LOG_CHANNEL', -100)  # Log channel id (make sure bot is admin)
BIN_CHANNEL = env_int('BIN_CHANNEL', -100)  # Bin channel id (make sure bot is admin)
PREMIUM_LOGS = env_int('PREMIUM_LOGS', -1004379059015)  # Premium logs channel id
DELETE_CHANNELS = parse_ids(environ.get('DELETE_CHANNELS', '-100')) #(make sure bot is admin)
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-100')  # Support group id (make sure bot is admin)
reqst_channel = environ.get('REQST_CHANNEL_ID', '-100')  # Request channel id (make sure bot is admin)
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/')  # Support group link (make sure bot is admin)

# FORCE_SUB 
auth_req_channels = environ.get("AUTH_REQ_CHANNELS", "-100")# requst to join Channel for force sub (make sure bot is admin) only for bot ADMINS  
auth_channels     = environ.get("AUTH_CHANNELS", "-100")# Channels for force sub (make sure bot is admin)

# ============================
# Payment Configuration
# ============================
QR_CODE = environ.get('QR_CODE', 'Your_Qr_Code')    # QR code image for payments
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', 'ɴᴏ ᴀᴠᴀɪʟᴀʙʟᴇ ʀɪɢʜᴛ ɴᴏᴡ')    # Owner UPI ID for payments

STAR_PREMIUM_PLANS = {
    10: "7day",
    20: "15day",    
    40: "1month", 
    55: "45day",
    75: "60day",
}  # Premium plans with their respective durations in days

# ============================
# MongoDB Configuration
# ============================
DATABASE_URI = environ.get('DATABASE_URI', "")  # MongoDB URI for the database
DATABASE_NAME = env_str('DATABASE_NAME', "Cluster0") # Database name (default: cluster)
COLLECTION_NAME = env_str('COLLECTION_NAME', 'SERIAL PRODCAST...') # Collection name (default: dreamcinezone_files)

# If MULTIPLE_DB Is True Then Fill DATABASE_URI2 Value Else You Will Get Error.
MULTIPLE_DB = env_bool('MULTIPLE_DB', False) # Type True For Turn On MULTIPLE DB FUNTION 
DATABASE_URI2 = environ.get('DATABASE_URI2', "")  # MongoDB URI for the second database (if MULTIPLE_DB is True)
# ============================
# Movie Notification & Update Settings
# ============================
MOVIE_UPDATE_NOTIFICATION = env_bool('MOVIE_UPDATE_NOTIFICATION', True)  # Notification On (True) / Off (False)
MOVIE_UPDATE_CHANNEL = env_int('MOVIE_UPDATE_CHANNEL', -1003900854538)  # Notification of sent to your channel
DREAMXBOTZ_IMAGE_FETCH = env_bool('DREAMXBOTZ_IMAGE_FETCH', True)  # On (True) / Off (False)
LINK_PREVIEW = env_bool('LINK_PREVIEW', False) # Shows link preview in notification msg instead of image
ABOVE_PREVIEW = env_bool('ABOVE_PREVIEW', False) # Shows link preview above the text in notification msg if True else below the msg
TMDB_API_KEY = environ.get('TMDB_API_KEY', '') # preffer to use your own tmdb API Key get it from https://www.themoviedb.org/settings/api
TMDB_POSTER = env_bool('TMDB_POSTER', False) # Shows TMDB poster in notification msg
LANDSCAPE_POSTER = env_bool('LANDSCAPE_POSTER', True) # Shows landscape poster in notification msg

# ============================
# Verification Settings
# ============================
IS_VERIFY = is_enabled(environ.get('IS_VERIFY', 'False'), False)  # Verification On (True) / Off (False)
LOG_VR_CHANNEL = env_int('LOG_VR_CHANNEL', -100) #Verification Channel Id 
LOG_API_CHANNEL = env_int('LOG_API_CHANNEL', -100) #If Anyone Set Your Bot In Any Group And Set Shortner In That Group Then In This Channel The All Details Come
VERIFY_IMG = environ.get("VERIFY_IMG", "https://telegra.ph/file/9ecc5d6e4df5b83424896.jpg")

TUTORIAL = environ.get("TUTORIAL", "https://t.me/roaroicgroup")   # Tutorial link for verification
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/kingo_serial")   # Second tutorial link for verification
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/kingo_serial")   # Third tutorial link for verification

# Verification (Must Fill All Veriables. Else You Got Error
SHORTENER_API = environ.get("SHORTENER_API", "") # Shortener API key
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "") # Shortener website

SHORTENER_API2 = environ.get("SHORTENER_API2", "")  # Shortener API key for second website
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "") # Shortener website for second website

SHORTENER_API3 = environ.get("SHORTENER_API3", "")  
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "") # Shortener website for third website

TWO_VERIFY_GAP = env_int('TWO_VERIFY_GAP', 1200) # Time gap for two-step verification in seconds (default: 20 minutes)
THREE_VERIFY_GAP = env_int('THREE_VERIFY_GAP', 54000)    

# ============================
# Channel & Group Links Configuration
# ============================
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/roaroicgroup') # Group link for the bot
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/roaroic0') # Owner link for the bot
UPDATE_CHNL_LNK = environ.get('UPDATE_CHNL_LNK', 'https://t.me/kingo_serial') # Update channel link for the bot

# ============================
# User Configuration
# ============================
auth_users = parse_ids(environ.get('AUTH_USERS', ''))
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = parse_ids(environ.get('PREMIUM_USER', ''))

# ============================
# Miscellaneous Configuration
# ============================
ULTRA_FAST_MODE = is_enabled(environ.get('ULTRA_FAST_MODE', "True"), True) # Set to True for fast search, False for original search

MAX_B_TN = environ.get("MAX_B_TN", "5") # Maximum number of buttons in a row (default: 5)
PORT = env_int('PORT', 8080)  # Port for the web server (default: 8080)
MSG_ALRT = environ.get('MSG_ALRT', 'Share & Support Us ♥️') # Alert message for users
DELETE_TIME = env_int('DELETE_TIME', 300)  #  deletion time in seconds (default: 5 minutes). Adjust as per your needs.
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")   # Custom caption for files
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION) # Custom caption for batch files
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")     # Custom IMDB template 
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None) # Maximum number of elements in a list (default: None, no limit)
INDEX_REQ_CHANNEL = env_int('INDEX_REQ_CHANNEL', LOG_CHANNEL)  # Index Request Channel ID (make sure bot is admin)
NO_RESULTS_MSG = env_bool('NO_RESULTS_MSG', True)  # True if you want no results messages in Log Channel
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)    # Max Button On (True) / Off (False)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)    # P_TTI_SHOW_OFF On (True) / Off (False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)    # IMDB Results On (True) / Off (False)
TMDB_ON_SEARCH = is_enabled((environ.get('TMDB_ON_SEARCH', "False")), False)    # Use TMDB Poster On Search Results
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True) # Auto Filter On (True) / Off (False)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True) # Auto Delete On (True) / Off (False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False) # Long IMDB Description On (True) / Off (False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True) # Spell Check Mode On (True) / Off (False)
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False) # Melcow New Users On (True) / Off (False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False) # Protect Content On (True) / Off (False)
PM_SEARCH = env_bool('PM_SEARCH', True)  # PM Search On (True) / Off (False)
EMOJI_MODE = env_bool('EMOJI_MODE', False)  # Emoji status On (True) / Off (False)
BUTTON_MODE = is_enabled((environ.get('BUTTON_MODE', "False")), False) # pm & Group button or link mode (True) / Off (False)
STREAM_MODE = env_bool('STREAM_MODE', True) # Set Stream mode True or False
PREMIUM_STREAM_MODE = env_bool('PREMIUM_STREAM_MODE', True) # Set Stream mode True or False only for premium users


# ============================
# Bot Configuration
# ============================

AUTH_REQ_CHANNELS = [int(ch) for ch in auth_req_channels.split() if ch and id_pattern.match(ch)] 
AUTH_CHANNELS = [int(ch) for ch in auth_channels.split() if ch and id_pattern.match(ch)]
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
LANGUAGES = {"ᴍᴀʟᴀʏᴀʟᴀᴍ":"mal","ᴛᴀᴍɪʟ":"tam","ᴇɴɢʟɪsʜ":"eng","ʜɪɴᴅɪ":"hin","ᴛᴇʟᴜɢᴜ":"tel","ᴋᴀɴɴᴀᴅᴀ":"kan","ɢᴜᴊᴀʀᴀᴛɪ":"guj","ᴍᴀʀᴀᴛʜɪ":"mar","ᴘᴜɴᴊᴀʙɪ":"pun"}
QUALITIES = ["360P", "480P", "720P", "1080P", "1440P", "2160P", "4K"]

SEASON_COUNT = 12
SEASONS = [f"S{str(i).zfill(2)}" for i in range(1, SEASON_COUNT + 1)]

BAD_WORDS = {
    "PrivateMovieZ",
    "toonworld4all",
    "themoviesboss",
    "1tamilmv",
    "tamilblasters",
    "1tamilblasters",
    "skymovieshd",
    "extraflix",
    "hdm2",
    "moviesmod",
    "hdhub4u",
    "mkvcinemas",
    "primefix",
    "join",
    "www",
    "villa",
    "tg",
    "original"
} # Set of bad words to filter out
   

# ============================
# Server & Web Configuration
# ============================

NO_PORT = env_bool('NO_PORT', False)
ON_HEROKU = 'DYNO' in environ
APP_NAME = environ.get('APP_NAME') if ON_HEROKU else None
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', 'kingo-q8hw.onrender.com'))
if ON_HEROKU and not getenv('FQDN'):
    if not APP_NAME:
        raise ValueError("APP_NAME must be set when running on Heroku (or set FQDN).")
    FQDN = APP_NAME + '.herokuapp.com'
else:
    FQDN = str(getenv('FQDN', BIND_ADRESS))
HAS_SSL = env_bool('HAS_SSL', True)
URL = "{}://{}/".format("https" if HAS_SSL else "http", FQDN)
SLEEP_THRESHOLD = env_int('SLEEP_THRESHOLD', 60)
WORKERS = env_int('WORKERS', 4)
SESSION_NAME = env_str('SESSION_NAME', 'dreamXBotz')
MULTI_CLIENT = False
name = str(environ.get('name', 'DREAMXBOTZ'))
PING_INTERVAL = env_int('PING_INTERVAL', 1200)  # 20 minutes

# ============================
# Reactions Configuration
# ============================
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]

# ============================
# Commands Bot
# ============================
Bot_cmds = {
    "start": "Sᴛᴀʀᴛ Mᴇ Bᴀʙʏ",
    "stats": "Gᴇᴛ Bᴏᴛ Sᴛᴀᴛs",
    "alive": "Cʜᴇᴄᴋ Bᴏᴛ Aʟɪᴠᴇ ᴏʀ Nᴏᴛ",
    "settings": "ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs",
    "id": "ɢᴇᴛ ɪᴅ ᴛᴇʟᴇɢʀᴀᴍ",
    "info": "Gᴇᴛ Usᴇʀ ɪɴғᴏ",
    "del_msg": "ʀᴇᴍᴏᴠᴇ ғɪʟᴇ ɴᴀᴍᴇ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ...",
    "movie_update": "ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "pm_search": "ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "trendlist": "Gᴇᴛ Tᴏᴘ Tʀᴀɴᴅɪɴɢ Sᴇᴀʀᴄʜ Lɪsᴛ",
    "broadcast": "ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ.",
    "grp_broadcast": "ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs",
    "send": "ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴜꜱᴇʀ.",
    "add_premium": "ᴀᴅᴅ ᴀɴʏ ᴜꜱᴇʀ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ.",
    "remove_premium": "ʀᴇᴍᴏᴠᴇ ᴀɴʏ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴘʀᴇᴍɪᴜᴍ.",
    "premium_users": "ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ.",
    "restart": "ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.",
    "group_cmd": "ɢʀᴏᴜᴘ ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ",
    "admin_cmd": "ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs ʟɪsᴛ.",
    "reset_group": "Group Setting Default",
    "trial_reset": "User Trial Reset"
}


#Don't Change Anything Here
if not MULTIPLE_DB:
    DATABASE_URI2 = DATABASE_URI

# ============================
# Logs Configuration
# ============================
LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for your queries.\n" if IMDB else "IMDB Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found, Users will be redirected to send /start to Bot PM instead of sending file directly.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled, files will be sent in PM instead of starting the bot.\n")
LOG_STR += ("BUTTON_MODE is found, filename and file size will be shown in a single button instead of two separate buttons.\n" if BUTTON_MODE else "BUTTON_MODE is disabled, filename and file size will be shown as different buttons.\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be sent along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled.\n" if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled, Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode is enabled, bot will be suggesting related movies if movie name is misspelled.\n" if SPELL_CHECK_REPLY else "Spell Check Mode is disabled.\n")