import pytest 
from poker import PokerProb 

class Test_PokerProb(object):
    def test_royal_flush(self):
        p1 = PokerProb(['AH','KH','QH','JH','10H'])
        assert p1.royal_flush(['AH','KH','QH','JH','10H']) == True 
        assert p1.royal_flush(['AH','JH','QH','JH','10H']) == False , 'This is not r flush'
        assert p1.royal_flush(['AH','9H','QH','JH','10H']) == False

    def test_straight_flush(self):
        p1 = PokerProb(['5C','6C','7C','8C','9C'])
        assert p1.straight_flush(['5C','6C','7C','8C','9C']) == True , 'This is s flush'
        assert p1.straight_flush([str(x)+'H' for x in range(2,7)]) == True 
        assert p1.straight_flush([str(x)+'S' for x in range(5,10)]) == True 
        assert p1.straight_flush(['AH','9H','QH','JH','10H']) == False 
        assert p1.straight_flush(['AH','KH','QH','JH','10H']) == False , 'This is r flush'

    def test_four_of_a_kind(self):
        p1 = PokerProb(['5C','6C','7C','8C','9C'])
        assert p1.four_of_a_kind(['AD','AC','AH','AS','5D']) == True 
        assert p1.four_of_a_kind(['5D','5C','6C','5H','5S']) == True
        assert p1.four_of_a_kind(['AH','KH','QH','JH','10H']) == False , 'Royal'
        assert p1.four_of_a_kind(['5C','6C','7C','8C','9C']) == False, 'S Flush'
        assert p1.four_of_a_kind(['10S','10H','10C','9H','9C']) == False , 'This is full house'
    
    def test_full_house(self):
        p1 = PokerProb(['5C','6C','7C','8C','9C'])
        assert p1.full_house(['10S','10H','10C','9H','9C']) == True 
        assert p1.full_house(['AD','AC','AH','AS','5D']) == False , 'This si f of kind'
        assert p1.full_house(['AD','AC','AH','KD','KS']) == True
        assert p1.full_house(['AH','9H','QH','JH','10H']) == False ,  'S flush'
        assert p1.full_house(['2H','2S','2C','3C','3D']) == True 
        assert p1.full_house(['AH','9H','QH','JH','10H']) == False 

    def test_flush(self):
        p1 = PokerProb(['5C','6C','7C','8C','9C'])
        assert p1.flush(['AH','KH','QH','JH','10H']) == False, 'this si r s flush'
        assert p1.flush(['5C','6C','7C','8C','9C']) == False, 'this is s flush'
        assert p1.flush(['3C','6C','7C','2C','AC']) == True
        assert p1.flush(['4H','AH','QH','JH','2H']) == True 

    def test_straight(self):
        p1 = PokerProb(['5C','6C','7C','8C','9C'])
        assert p1.straight(['AH','KH','QH','JH','10H']) == False, 'this is r s flush'
        assert p1.straight(['5C','6C','7C','8C','9C']) == False, 'this is s flush'
        assert p1.straight(['4C','3H','5S','6D','7S']) == True
        assert p1.straight(['6C','7S','8S','9S','10S']) == True 
    