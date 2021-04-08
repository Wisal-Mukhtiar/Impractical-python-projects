"""Bonus project in project one"""
from pprint import pprint
import string

def main():
    """main LOL"""
    text = '''like the castle in its corner in a medievel game, i foresee terrible trouble
     and i stay here just the same '''
    dictio = {}
    alphabets = list(string.ascii_lowercase)
    for word in text.rstrip():
        if word not in dictio and word in alphabets:
            dictio[f'{word}'] = [word]
        elif word in alphabets:
            dictio[f'{word}'].append(word)

    pprint(dictio)

if __name__ =='__main__':
    main()
