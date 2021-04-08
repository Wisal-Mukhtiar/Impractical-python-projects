""" Extra project in the first project with first one """
import random

def main():
    """The main function"""
    words = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
                'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
                'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
                'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
                'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
                'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
                'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
                'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
                'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
                'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
                'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
                'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
                'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
                'Woolysocks')
    vowels = ('a', 'e', 'i', 'o', 'u')
    word = random.choice(words)
    if word[0].lower() in vowels:
        print(word)
        print()
        word = word[1:] +word[0].lower()+ 'ay'
        print(word)
    else:
        print(word)

if __name__ == "__main__":
    main()
    