import json
import requests
import webbrowser
import time, os

with open("assets\\updater\\version.json", "r", encoding="utf-8") as updater_json:
    data_updater = json.load(updater_json)

def updateCheck():

    INFO_UPDATER = json.loads(requests.get("https://raw.githubusercontent.com/ExtbhiteEAS/CopyrightPatcher/main/assets/updater/version.json").text)
    INFO_WHATSNEW = json.loads(requests.get("https://raw.githubusercontent.com/ExtbhiteEAS/CopyrightPatcher/main/assets/updater/whatsnew.json").text)

    version = INFO_UPDATER["application"]["version"]
    whatsnew = INFO_WHATSNEW["updaterDesc"]["whatsnew"]
    current_version = data_updater["application"]["version"]

    print("[INF] Checking update...")
    time.sleep(1.4)
    if version != current_version:
        print(f"[INF] Available new version of CopyrightPatcher: {version}\n{whatsnew}\n[INF] Taking you to github page..")
        time.sleep(2.06)
        webbrowser.open_new_tab("")
        os._exit(0)
    else:
        print("[INF] You have latest version of CopyrightPatcher.")