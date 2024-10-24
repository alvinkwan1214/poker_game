import random
import numpy as np

def deal(cards, deck):
    dealt_out = []
    i = 0
    while i < cards:
        num = random.randint(0, 51)
        
        if num in deck:
            deck = np.delete(deck, np.where(deck==num))
            dealt_out.append(num)
            i += 1
    return dealt_out, deck

def translate(cards):
    res = []
    for card in cards:
        suit = card // 13 
        value = card - 13 * suit
        out = str(quick_tranlate('value', value)) + ' of ' + quick_tranlate('suit', suit)
        res.append(out)
    return res

def check_hands(cards):
    value_map = {}
    suit_map = {}
    for card in cards: 
        suit = card // 13
        value = quick_tranlate('value', card - 13*suit)
        suit = quick_tranlate('suit', suit)
        value_map[value] = value_map.get(value, 0) + 1
        suit_map[suit] = suit_map.get(suit, 0) + 1
    return value_map, suit_map

def quick_tranlate(type, number):
    if type == 'suit':
        translate_suit = {0:'Spade',
                        1:'Heart',
                        2:'Clubs',
                        3: 'Diamonds'
        }
        return translate_suit[number]
    if type == 'value':
        translate_value = {0:'Ace',
                        10:'Jack',
                        11:'Queen',
                        12:'King'
        }
        return translate_value.get(number, number  + 1)

if __name__ == "__main__":
    deck = np.linspace(0, 51, 52, dtype=int)
    flop, deck = deal(3, deck)
    while len(flop) <= 5:
        print(translate(flop))
        #print(check_hands(flop))
        hand, deck = deal(2, deck)
        print(translate(hand))
        input('next?')
        next_card = deal(1, deck)
        flop.append(next_card[0][0])

        
    


