#!/usr/bin/python3

import os

def setup_server():
    folder_name = 'Server_Backup'

    if os.path.exists(folder_name):
        print(f"{folder_name} folder already exists")

    else:
        os.mkdir(folder_name)
        print(f"Folder is created successfully: {folder_name}")

    current_path = os.getcwd()
    print(f"Your current working directory is: {current_path}")

if __name__ == "__main__":
    setup_server()