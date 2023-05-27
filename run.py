import os, sys, subprocess
from pathlib import Path
import re

starting_dir = Path(os.getcwd())
# current_user = os.environ.get('USERNAME')
current_user = os.getlogin()
target_dir_name = "Browser_Backup"
target_path = f"C:/Users/{current_user}/Desktop/{target_dir_name}".replace("/", "\\")
browsers_info = {"Microsoft": "Edge", "Google": "Chrome"}

for provider, browser in browsers_info.items():
    print(f"Backing up {browser}...")
    path = rf"C:\Users\{current_user}\AppData\Local\{provider}\{browser}\User Data".replace("\\", "//")
    path
    path = Path(rf"C:\Users\{current_user}\AppData\Local\{provider}\{browser}\User Data")

    os.chdir(path)

    dir_files = os.listdir()

    i = 0
    for file in dir_files:
        if file.lower() == "default" or file.lower().startswith("profile"):
            print(f"Adding {file}...")
            os.chdir(path / file)
            i += 1
            for name in ["Sessions", "Bookmarks"]: 
                if re.match(r"sessions|bookmarks", name.lower()):
                    print(name)
                    target_session_folder_name = browser
                    filename_clean = file.replace(" ", "_")
                    try:
                        subprocess.check_output(["powershell", f"mkdir {target_path}\{target_session_folder_name}\{filename_clean}"], shell=True)
                    except Exception as e:
                        # print(f"Can't create dir {file}")
                        # print("Directory already exists.")
                        # print(f"{target_path}\{target_session_folder_name}\{filename_clean}")
                        pass
                    try:
                        subprocess.check_output(["powershell", f"cp -r {name} {target_path}\{target_session_folder_name}\{filename_clean}\\"], shell=True)
                    except Exception as e:
                        print(f"Couldn't copy {name}.")

            os.chdir("..")
    print(f"{browser} is backed up successfully.")
    print()