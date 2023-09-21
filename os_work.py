
from datetime import datetime 
import os
# Working with the OS Module.  Count the files in the desktop directory

def display_cwd():
    cdw = os.getcwd()
    print (cdw)

def up_one_directory_level():
    os.chdir("../")

def format_datetime(timestamp):
    utc_timestramp = datetime.utcfromtimestamp(timestamp)
    formated_date = utc_timestramp.strftime("%d %b %Y %H %M %S")
    return formated_date

def display_entries_in_directory(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            print("Name: " , entry.name)
            info = entry.stat()
            print ("Creation time: ", format_datetime(info.st_ctime))
            print ("Files size time: ", info.st_size)

def display_directories(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir():
                print ("Directory Name: " , entry.name )

def display_directories(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                print ("File Name: " , entry.name )
    # desktop_path= "C:/Users/edilm/OneDrive/Desktop"
    # listNames = os.listdir(desktop_path)
    # files_count = len(listNames)
    # print (files_count)

# os.walk(directory) returns a tuple of dirpath, dirname and filename
def top_down_walk():
    for dirpath, dirnames , files in os.walk("../py_draw"):
        print ("Directory: ", dirpath)
        print ("Include this directories: ")
        for dirname in dirnames:
            print ( dirname )
        print ("Include this files")
        for filename in files:
            print (filename)
        print()

def top_down_walk():
    for dirpath, dirnames , files in os.walk("../py_draw"):
        print ("Directory: ", dirpath)
        print ("Include this directories: ")
        for dirname in dirnames:
            print ( dirname )
        print ("Include this files")
        for filename in files:
            print (filename)
        print()


def bottom_up_walk():
    for dirpath, dirnames , files in os.walk("../py_draw", topdown=False):
        print ("Directory: ", dirpath)
        print ("Include this directories: ")
        for dirname in dirnames:
            print ( dirname )
        print ("Include this files")
        for filename in files:
            print (filename)
        print()

#this creates a directory.  
def make_logs_dir():
    try:
        os.mkdir("logs/")
    except FileExistsError as ex:
        print("Logs directory already exists")


if __name__ == "__main__" :
    # display_cwd()
    # up_one_directory_level()
    #display_cwd()
   #display_entries_in_directory("C:/Users/edilm/OneDrive/Desktop/Programming/")
    #display_directories("../py_draw")
    #top_down_walk()
    #bottom_up_walk()
    make_logs_dir()
