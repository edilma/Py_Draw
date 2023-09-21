import glob

def  display_pngs():
    py_files = glob.glob("*.py") # return a list
    print (py_files)

def find_filesCount():
    filtered_items = glob.glob('fi*')
    print (filtered_items)

def find_filesCount_in_subdir():
    for file in glob.iglob("**/*fi", recursive=True):
        print(file)
    

if __name__ == "__main__":
    #display_pngs()
    #find_filesCount()
    #find_filesCount_in_subdir()
    find_filesCount_in_subdir()

