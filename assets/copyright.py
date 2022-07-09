# Copyright [2022-2023] [Extbhite]
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import json
from local import configs
from typing import Literal

class Localisation:

    # // This class using for localisation.
    # // If you want adding your national language here(if not exist here) - just
    # // write here like this and add case for your language, then copy functions but rename
    # // localisation value in print function.

    # Russian language.
    with open("assets/localisation/russian/ru_RU.json", "r", encoding="utf-8") as russian:
        russian_lang = json.load(russian)
    
    check_special_folder_successfully = russian_lang["lang_russian"]["check_special_folder_successfully"]
    check_special_folder_not_successfully = russian_lang["lang_russian"]["check_special_folder_not_successfully"]
    create_license_file_info = russian_lang["lang_russian"]["create_license_file_info"]
    create_license_file_successfully = russian_lang["lang_russian"]["create_license_file_successfully"]
    create_license_file_not_successfully = russian_lang["lang_russian"]["create_license_file_not_successfully"]

class CopyrightAttachement:

    def __init__(self, language: str = None, debug: Literal = False):
        self.language = language
        self.debug = debug
        self.local_language = Localisation()

    def create_copyright(self):

        # // Matching if language have value like this "lang_english" - script starting function.
        # // But if language have value like None - script can't starting function.
        match self.language:
            case None:
                print(configs.info_terminal_text + "Please set language in settings.json file.")
            case "lang_russian":

                # // Checking copyright folder and "import" file.
                with open("copyright/copyright.import", "r", encoding="utf-8") as check_debug_files:
                    try:
                        print(configs.info_terminal_text + self.local_language.check_special_folder_successfully)
                    except Exception as ERROR_DEBUG:
                        if self.debug == True:
                            print(configs.debug_terminal_text + ERROR_DEBUG)
                        print(configs.info_terminal_text + self.local_language.check_special_folder_not_successfully)
                        os._exit(0)

                # // Building copyright patcher.
                path = "build"
                with open("copyright\copyright.import", "w", encoding="utf-8") as copy_def:
                    copy_def.write(configs.copy_def_txt)
                    print(configs.info_terminal_text + "Writed data in copyright import file.")

                os.system("copy copyright\* build")
                os.system(f"mkdir {path}\copyright_assets && move {path}\copyright.import {path}\copyright_assets")

                with open(f"{path}\copyright.txt", "w", encoding="utf-8") as copyright_file:
                    copyright_file.write(configs.copyright_text)
                print(configs.info_terminal_text + self.local_language.create_license_file_info)

                with open(f"{path}/LICENSE", "w", encoding="utf-8") as copyright_license:
                    try:
                        copyright_license.write(configs.license_apache)
                        print(configs.info_terminal_text + self.local_language.create_license_file_successfully)
                    except Exception as ERROR_DEBUG:
                        if self.debug == True:
                            print(configs.debug_terminal_text + ERROR_DEBUG)
                        print(configs.info_terminal_text + self.local_language.create_license_file_not_successfully)
                        os._exit(0)