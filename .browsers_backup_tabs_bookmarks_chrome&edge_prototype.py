import os, sys, subprocess
from pathlib import Path
import re

base_dir = Path(os.getcwd())
base_dir

target_dir = "C:/Users/moham/Desktop/BrowsersData".replace("/", "\\")

provider_name = "Microsoft"
browser_name = "Edge"

path = rf"C:\Users\moham\AppData\Local\{provider_name}\{browser_name}\User Data".replace("\\", "//")
path
path = Path(rf"C:\Users\moham\AppData\Local\{provider_name}\{browser_name}\User Data")

os.chdir(path)

dir_files = os.listdir()

required_files = []
i = 0
for file in dir_files:
    if file.lower() == "default" or file.lower().startswith("profile"):
        required_files.append(file)
        print(f"added {file} to required_files")
        os.chdir(path / file)
        i += 1
        for name in os.listdir(): 
            if re.match(r"sessions|bookmarks", name.lower()):
                print(name)
                target_session_folder_name = f"script_copied_sessions_{browser_name}"
                filename_clean = file.replace(" ", "_")
                try:
                    subprocess.check_output(["powershell", f"mkdir {target_dir}\{target_session_folder_name}\{filename_clean}"], shell=True)
                except Exception as e:
                    print(e)
                try:
                    subprocess.check_output(["powershell", f"cp -r {name} {target_dir}\{target_session_folder_name}\{filename_clean}\\"], shell=True)
                except Exception as e:
                    print(e)

        os.chdir("..")
required_files