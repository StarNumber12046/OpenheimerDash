import sys
import dotenv
import os
import time
from tqdm import tqdm
import sqlite3
import json

env_file = sys.argv[2]
db_folder = sys.argv[1]

dotenv.load_dotenv(env_file)

debug_mode = True if os.environ.get("DEBUG", "false").lower() == "true" else False

folder = os.listdir(db_folder)

db =sqlite3.connect(os.environ.get("DB_PATH"))
c = db.cursor()


if debug_mode:
    print(f"[DEBUG] --> Adding {len(folder)} servers")

for server in tqdm(folder):
    f = open(f"{db_folder}/{server}", "r")
    server_json = json.load(f)
    version = server_json["version"]["name"]
    max_players = server_json["players"]["max"]
    online_players = server_json["players"]["online"]
    motd = server_json["description"]["text"]
    favicon = server_json["favicon"]
    c.execute("INSERT INTO servers (IP, VER, max_players, online_players, motd, favicon, stat) VALUES (?,?,?,?,?,?,?)", (server, version, max_players, online_players, motd, favicon, "nc"))
    db.commit()
    if debug_mode:
        print(f"Added server! \n version: {version}\nmax players: {max_players}\nonline players; {online_players}\nMOTD: {motd}\nfavicon: [base64, ignored]\nIP: {server}")