#!/usr/bin/python3

import os # os module import here

directory_name = "log" # here i assign the folder name

def simple_log_or(): 
    """
    This is the main function. This function helps us to check if the log directory exists or not. 
    If not, then this function creates a folder, and then this function creates 3 different log files and store on log folder
    """
    
    if os.path.exists(directory_name):
        print(f"Folder already exsist")

    else:
        os.mkdir(directory_name)
        print(f'Folder is created successfully :)')
        
        open(f"{directory_name}/error.log", "w").close()
        open(f"{directory_name}/access.log", "w").close()
        open(f"{directory_name}/system.log", "w").close()

        print("Log setup complete! Total Files: 3")

if __name__ == "__main__":
    simple_log_or()


