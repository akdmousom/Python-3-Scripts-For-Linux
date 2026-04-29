#!/usr/bin/python3


"""🛠 চ্যালেঞ্জ: "The Quick IP Logger"
একজন সার্ভার অ্যাডমিন হিসেবে আপনাকে প্রায়ই আইপি অ্যাড্রেস (IP Address) সেভ করে রাখতে হয়। আপনার কাজ হলো এমন একটি স্ক্রিপ্ট লেখা যা রান করার সময় একটি IP Address আর্গুমেন্ট হিসেবে নেবে এবং সেটি একটি ফাইলে সেভ করবে।

আপনার কোড যা করবে:
১. আর্গুমেন্ট হিসেবে একটি আইপি (sys.argv[1]) নেবে।
২. যদি ইউজার আইপি না দেয়, তবে স্ক্রিপ্টটি একটি মেসেজ দিয়ে বন্ধ হবে।
৩. যদি আইপি দেয়, তবে সেটি server_list.txt নামে একটি ফাইলে লিখে রাখবে।
৪. টার্মিনালের উইডথ অনুযায়ী একটি বর্ডার দিয়ে শেষ করবে।

আপনার জন্য ক্লু (Hints):
আর্গুমেন্ট চেক: if len(sys.argv) < 2:

ফাইল রাইটিং: with open("server_list.txt", "a") as f: (এখানে "a" মানে Append, এটি নতুন ডেটা আগের ডেটার নিচে যোগ করে, মুছে ফেলে না)।

লেখা: f.write(ip_address + "\n")

কেন এই চ্যালেঞ্জটি?
এই চ্যালেঞ্জটি করলে আপনি শিখবেন:

কীভাবে লিনাক্সের কমান্ড লাইন থেকে ডেটা নিয়ে সরাসরি ফাইলে স্টোর করতে হয়।

"w" (Write) এবং "a" (Append) এর মধ্যে পার্থক্য (সার্ভার লগের জন্য Append খুবই জরুরি)। """

import sys
import os
import shutil

columns = shutil.get_terminal_size().columns

def the_quick_ip_logger():
    print(f"*" * columns)
    print(f"\nWelcome to the quick ip logger script\n")
    print(f"*" * columns)

    if len(sys.argv) < 2:
        print("Enter Vail Ip Address")
        print(f"Usage: {sys.argv[0]} [127.0.0.1] ")
        return
    else:
        ip_addr = sys.argv[1]
        with open("server_ip_list.txt", "a") as f: #this line create a text file.
            f.write(ip_addr + "\n") #this line help us to write ip address in our server_ip_list.txt file.
            print("Ip is added successfully")
            print("_" * columns)
            return


if __name__ == "__main__":
    the_quick_ip_logger()