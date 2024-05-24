
import random
mains = ['cauliflower','tilapia fillet','pork loin','green beans','rainbow carrots','potatoes','three color squash','eggplant','eye round of beef',]
flairs  = ['with balsamico', 'with garlic and olive oil', 'with minted yogurt', 'soup', 'chutney', 'salad', 'with salsa', 'over sticky rice', 'au jus', 'with basmati rice']
price_mains = [4, 9, 12, 4, 4, 5, 5.50, 1.25, 14]
price_flairs = [1, 3, 4, 5, 2, 5.25, 3.25, 3.50, 4, 4]
while True:
    try:
        number_items = int(input('How many menu items do you need? '))
        for i in range(number_items):
            main = random.choice(mains)
            flair = random.choice(flairs)
            print(f"\n {main} {flair} ${price_mains[mains.index(main)]+price_flairs[flairs.index(flair)]}\n")
        break
    except ValueError:
        print('Please input an integer! ')


while True:
        askinsult = str.lower(input('Would you like to hear a beautiful insult? '))
        if 'y' in askinsult:
            nouns = ['pig','toe','pidgeon',' bucket','potato','loser','weirdo']
            adjs  = ['big', 'lousy', 'dust', 'crummy', 'discusting', 'spiteful', 'slimey']
            while True: 
                try:
                    number_insults = int(input('How many insults do you want? '))
                    for i in range(number_insults):
                        rand_noun = random.choice(nouns)
                        rand_adj = random.choice(adjs)
                        print(f"\n {rand_adj} {rand_noun} \n")
                    break
                except ValueError:
                    print('Please input an integer! ')
        else:
            print('Bye!')
            break


    

