import os
import sys
import shutil # With this library, you can measure the actual size of a terminal


colums = shutil.get_terminal_size().columns
print("*" * colums)

