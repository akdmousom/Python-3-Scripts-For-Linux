#!/usr/bin/python3

import os
import sys

def create_dir():
    # ১. চেক করা হচ্ছে আর্গুমেন্ট দেওয়া হয়েছে কি না
    if len(sys.argv) < 2:
        print(f"Please Enter The Right Command: ./user_argb.py [Folder Name]")
        return

    # ২. এই লাইনটি অবশ্যই if ব্লকের বাইরে থাকতে হবে
    folder_name = sys.argv[1]

    # ৩. ফোল্ডার তৈরির লজিক
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully")
    else:
        print(f"Folder '{folder_name}' already exists")

if __name__ == "__main__":
    create_dir()