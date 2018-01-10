import random
from copy import deepcopy

def deal(deck, hand, n):
    hand += deck[:n]
    return hand

def bust(hand):
    if sum(hand) > 21:
        if 11 in hand:
            for i, val in enumerate(hand):
                if val == 11:
                    hand[i] = 1
            if sum(hand) > 21:
                return True
            return False
        return True
    return False

def play_game(players, seed=0):
    
    # Initial dealing of cards
    random.seed(seed)
    deck = [x for x in range(2, 12) for i in range(4)]
    random.shuffle(deck)
    
    hands = {name: [] for name in players}
    
    for i in range(2):
        for name, hand in hands.items():
            deal(deck, hand, 2)
            deck = deck[1:]

    hands['Dealer'] = deal(deck, [], 1)
    deck = deck[1:]
    
    curr_hands = deepcopy(hands)
    iter_hands = deepcopy(hands)
    stuck = {}

    for name in iter_hands:
        if len(curr_hands) == 1:
            return name
        hand = iter_hands[name]
        while not bust(hand) and name not in stuck:
            if sum(hand) < 16:
                hand = deal(deck, hand, 1)
                deck = deck[1:]
            elif sum(hand) < 19:
                r = random.random()
                if r > 0.75:
                    hand = deal(deck, hand, 1)
                    deck = deck[1:]
                else:
                    stuck[name] = hand
            elif sum(hand) < 21:
                r = random.random()
                if r > 0.999:
                    hand = deal(deck, hand, 1)
                    deck = deck[1:]
                else:
                    stuck[name] = hand
            else:
                stuck[name] = hand
        if bust(hand):
            del curr_hands[name]                
            
    rankings = sorted(stuck.items(), key=lambda item: sum(item[1]))
    name_rankings = [player[0] for player in rankings]
    return name_rankings[-1]
for seed in range(10):
    print(play_game(['Henry', 'Vince', 'Nikoleta', 'Geraint'], seed))
