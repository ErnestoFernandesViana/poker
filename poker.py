from deck import Deck
import copy 

""" Class that takes in cards and measure probability of poker hands. """
class PokerProb:
    card_order = ['A','2','3','4','5','6','7','8','9','10','J','Q','K','A']
    def __init__(self, cards_list):
        self.full_deck = Deck()
        self.full_deck.take_off_cards(cards_list)
        self.cards = cards_list
        self.set_combinations = self._group_by_five(self.card_order)

    @staticmethod
    def give_cards(deck, hand):
        cards = [deck.pop() for x in range(7 - len(hand))]
        for x in cards: hand.append(x)

    @staticmethod
    def _group_by_five(lista):
        lista_len = len(lista)
        return [set([lista[y] for y in range(i, i+5)]) for i, x in enumerate(lista) if i < lista_len - 4]

    def calc_probs(self, n = 10000):
        royal_flush = 0 
        straight_flush = 0 
        four = 0
        full_house = 0
        flush = 0
        straight = 0 
        three = 0  
        for x in range(n):
            hand_list= copy.deepcopy(self.cards)
            self.full_deck.shuffle()
            deck_list = copy.deepcopy(self.full_deck.deck)
            self.give_cards(deck_list, hand_list)
            if self.royal_flush(hand_list):
                royal_flush += 1
                continue
            if self.straight_flush(hand_list):
                straight_flush += 1
                continue
            if self.four_of_a_kind(hand_list):
                four += 1 
                continue
            if self.full_house(hand_list):
                full_house += 1
                continue
            if self.flush(hand_list):
                flush += 1
                continue
            if self.straight(hand_list):
                straight += 1
                continue
            if self.three(hand_list):
                three += 1
                continue
          
        return ((royal_flush/n)*100 , (straight_flush/n)*100, (four/n)*100, full_house*100/n , 
                flush*100/n, straight*100/n, three*100/n)


    @staticmethod
    def royal_flush(lista):
        rf = {'AH','KH','QH','JH','10H'}
        if rf.issubset(set(lista)):
            return True 
        else: 
            return False 
        
    def straight_flush(self, lista):
        values = {x[:-1] for x in lista}
        naipes = self.naipe_dict(lista)
        if any([x.issubset(values) for x in self.set_combinations]):
            if 5 in naipes.values():
                if not self.royal_flush(lista):
                    return True 
                else:
                    return False
            else: return False 
        else: return False 

    def four_of_a_kind(self, lista):
        d = self.number_dict(lista)
        if 4 in d.values():
            return True 
        else: 
            return False 

    def full_house(self, lista):
        d = self.number_dict(lista)
        if {2,3}.issubset(set(d.values())):
            return True 
        else:
            return False 

    def flush(self, lista):
        d = self.naipe_dict(lista)
        if 5 in d.values():
            if not self.straight_flush(lista):
                if not self.royal_flush(lista):
                    return True 
                else:
                    return False 
            else:
                return False 
        else:
            return False 

    def straight(self, lista):
        values = {x[:-1] for x in lista}
        if any([values.issuperset(x) for x in self.set_combinations]):
            if not self.royal_flush(lista):
                if not self.straight_flush(lista):
                    return True 
                else: 
                    return False 
            else:
                return False 
        else: 
            return False 

    def three(self, lista):
        d = self.number_dict(lista)
        if 3 in d.values():
            return True 
        else:
            return False 

    @staticmethod
    def number_dict(lista):
        d = {}
        for x in lista:
            if x[:-1] in d:
                d[x[:-1]] += 1
            else:
                d[x[:-1]] = 1 
        return d

    @staticmethod
    def naipe_dict(lista):
        d = {}
        for x in lista:
            if x[-1] in d:
                d[x[-1]] += 1
            else:
                d[x[-1]] = 1 
        return d


if __name__ == '__main__':
    """ pb = PokerProb(['AH','KH','QH','JH','10H']) """
    pb = PokerProb(['AH','KH','10H'])
    print(pb.calc_probs())
    p1 = PokerProb(['5C','6C','7C'])
    print(p1.calc_probs())
    p1 = PokerProb(['AD','AC','AH'])
    print(p1.calc_probs())
    p1 = PokerProb(['AD','AC'])
    print(p1.calc_probs())
