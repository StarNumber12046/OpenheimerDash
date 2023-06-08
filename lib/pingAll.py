import sys
import dotenv
import os
import sqlite3
import requests
from typing import List
from tqdm import tqdm

env_file = sys.argv[1]

dotenv.load_dotenv(env_file)

debug_mode = True if os.environ.get("DEBUG", "false").lower() == "true" else False
if debug_mode:
    print("Debug Mode enabled")
db =sqlite3.connect(os.environ.get("DB_PATH"))

if debug_mode:
    print("[DEBUG] --> Connected to database on " + os.environ.get("DB_PATH"))

c = db.cursor()
servers: List[List[str]] = c.execute("SELECT * FROM servers").fetchall()
for a in tqdm(servers):
    if debug_mode:
        print("[DEBUG] --> Running on " + a[0])
    server_request = requests.get(f"http://{os.environ.get('SERVERS_API')}/status/java/{a[0]}")
    if debug_mode:
        print("[DEBUG] --> Server request succeded.")
    server = server_request.json()
    if server['online']:
        if debug_mode:
            print("[DEBUG] --> Executing query " +"UPDATE servers SET stat = 'online' WHERE IP = '" + a[0] + "' LIMIT 1")
        c.execute("UPDATE servers SET stat = 'online' WHERE IP = '" + a[0] + "' LIMIT 1")
        if debug_mode:
            print(f"[DEBUG] --> Server {a[0]} has been updated to online status")
    else:
        if debug_mode:
            print("[DEBUG] --> Executing query " +"UPDATE servers SET stat = 'offline' WHERE IP = '" + a[0] + "' LIMIT 1")
        c.execute("UPDATE servers SET stat = 'offline' WHERE IP = '" + a[0] + "' LIMIT 1")
        if debug_mode:
            print(f"[DEBUG] --> Server {a[0]} has been updated to offline status")