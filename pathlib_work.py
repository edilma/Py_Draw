from pathlib import Path

def print_directory_contents():
    entries = Path.cwd()
    #entries = Path("images/")
    #entries = Path.home()
    for entry in entries.iterdir():
        print (entry.name)
        print (entry.parent)
        print( entry.parent.parent)
        print(entry.stem)
        print (entry.suffix)
        print (entry.stat())
        
#this creates a directory.  It doesn't create a new one if it already exists
def make_output_dir():
    dir_path = Path("output/")
    dir_path.mkdir(exist_ok=True)


if __name__ == "__main__":
    #print_directory_contents()
    make_output_dir()
