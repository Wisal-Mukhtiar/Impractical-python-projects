"""this module will open and read the file

ARGUMENTS:
-text file name (and path if not in same directory)

Exceptions:
-IO Error if filename or path not found 

Imports
-sys module

Returns list of dictionary words    

"""
import sys

def load(file_name):
    """Main function to open, read and return list of words"""
    try:
        with open(file_name, 'r') as filee:
            words = filee.read().split('\n')
            return [word.lower() for word in words]
    
    except IOError as error_name:
        print(f"{error_name} Error opening file {file_name}  , Terminating program")
        sys.exit(1)

if __name__ == '__main__':
    print(load('dictionary.txt'))
