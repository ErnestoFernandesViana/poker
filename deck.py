import random 

class Deck:
    figures = {'D' : u"\u2666", 'H': u"\u2665", 
                'C':u"\u2663", 'S':u"\u2660"} #Diamond, Heart, Club, Spade 
    deck_nipes = ['D','H','C','S']
    deck_numbers = [str(x) for x in range(2, 11)]
    deck_letters = ['A','J','Q','K']
    
    def __init__(self):
        self.deck = [x + y for x in (self.deck_numbers +  self.deck_letters) for y in self.deck_nipes]

    def shuffle(self):
        random.shuffle(self.deck)

    def pull_cards(self, number):
        if len(self.deck) >= number:
            return [self.deck.pop() for _ in range(number)]
        else: 
            print('Not enough cards in deck to pull {} cards!'.format(number))
            return False

    def take_off_cards(self, lista):
        self.deck =  list(set(self.deck).difference(set(lista)))

    def push_cards(self, number):
        pass 

    @classmethod
    def print_cards(cls, lista):
        cards = [str(x[:-1]) + cls.figures[x[-1]] for x in lista]
        return '  '.join(cards)

    def __len__(self):
        return len(self.deck)




        

if __name__ == '__main__':
    d1 = Deck()
    cards = d1.pull_cards(3)
    print(d1.print_cards(['AS','2C']))
    d2 = Deck()
    print(len(d2)) 
    d2.take_off_cards(['AS','KC'])
    print(len(d2))