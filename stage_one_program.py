#!/usr/bin/python3

import os 
import subprocess 
import shutil 
import sys 

def user_input():
    columns = shutil.get_terminal_size().columns
    print("*" * columns)

    # আর্গুমেন্ট চেক করা
    if len(sys.argv) < 2:
        print("Error: Please provide a folder name: ")
        print(f"Usage: {sys.argv[0]} [Folder Name]")
        print("*" * columns)
        return
    
    # আর্গুমেন্ট থেকে ফোল্ডারের নাম নেওয়া
    folder_name = sys.argv[1]

    # ফোল্ডার তৈরি করার লজিক
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' Successfully Created")
    else:
        print(f"Folder '{folder_name}' already exists")

    print("*" * columns)

# এটি অবশ্যই ফাংশনের বাইরে থাকবে
if __name__ == "__main__":
    user_input()