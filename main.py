import json
from assets import copyright, updater

def main():
    with open("settings.json", "r", encoding="utf-8") as settings:
        settings_config = json.load(settings)

    updater.updateCheck()

    choose = int(input("[1] Patching copyright. | [2] Help. | [3] Exit from programm. | (Default=None) :: "))

    if choose == 1:
        assets = copyright.CopyrightAttachement(language=settings_config["main"]["language"], debug=settings_config["main"]["debugger"])
        assets.create_copyright()

if __name__ == "__main__":
    main()