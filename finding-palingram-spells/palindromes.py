""" Find palindromes from the dictionary file"""
import load_dictionary
import sys

def main(file_path):     #file path or file_name for current dir
    """The main function to find palindromes"""
    words = load_dictionary.load(file_path)
    palindromes_list = []

    for word in words:
        if len(word)>1 and word == word[::-1]:
            palindromes_list.append(word)

    print(f"No of palindromes found {len(palindromes_list)} ")
    print(palindromes_list, sep='\n')


if __name__ == "__main__":
    main(sys.argv[1])