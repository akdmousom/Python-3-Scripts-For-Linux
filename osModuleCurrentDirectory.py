#!/usr/share/python3

#This is a simple script. The script shows your current path

import os #here I import the os module, which is a Python module

path = os.listdir('.')

print("=" * 30)
print(f"Your Current Path Is: {path}")
