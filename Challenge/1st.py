#!/usr/bin/python3

import os
import sys
import shutil

# ১. টার্মিনাল উইডথ সেট করা
columns = shutil.get_terminal_size().columns

def user_input():
    # ২. হেডার প্রিন্ট করা
    print("=" * columns)
    print("The Smart Welcome Kit")
    print("=" * columns)

    # ৩. আর্গুমেন্ট চেক (আগে চেক করতে হবে)
    if len(sys.argv) < 2:
        print("Error: Enter Your Name!")
        print(f"Usage: {sys.argv[0]} [User Name]")
        print("=" * columns)
        return

    # ৪. চেক পাস করার পর ভেরিয়েবল সেট করা
    folder_name = sys.argv[1]

    # ৫. ফোল্ডার ও ফাইল তৈরির লজিক
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Success: Folder '{folder_name}' created!")
        
        # ফাইলের ভেতরে কিছু লিখতেও পারেন
        with open(f"{folder_name}/welcome.txt", "w") as f:
            f.write(f"Welcome {folder_name} to the server automation world!")
            
        print(f"Success: welcome.txt file created inside {folder_name}")
    else:
        print(f"Notice: Folder '{folder_name}' already exists.")

    # ৬. ফুটার বর্ডার
    print("=" * columns)

# ৭. মেইন ব্লক (এটি একদম বাম দিক থেকে শুরু হবে)
if __name__ == "__main__":
    user_input()