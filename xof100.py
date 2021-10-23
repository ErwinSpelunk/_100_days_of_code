#%%
from modules import blackjack_logo
import random as rnd

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

#%%
def draw_cards(nn):
    """
    returns LIST, even with only one card
    """
    card_drawn = rnd.sample(deck,nn)
    for k in card_drawn:
        del deck[deck.index(k)]
    return card_drawn
#%%
def evaluate_cards(in_cards):
    out_cards = []
    aces = []
    for card in in_cards:
        if card in ["J", "Q", "K"]:
            out_cards += [10]
        elif card == "A":
            aces += ["A"]
        else:
            out_cards += [card]
    if aces is not []:
        if len(aces) == 1 and sum(out_cards)+11 <= 21:
            out_cards += [11]
        elif len(aces) == 1 and sum(out_cards)+11 > 21:
            out_cards += [1]
        elif len(aces) == 2 and sum(out_cards)+12 > 21:
            out_cards += [1, 1]
        elif len(aces) == 2 and sum(out_cards)+12 <= 21:
            out_cards += [11, 1]
    else:
        pass        
    return out_cards

#%%
def check_player(participant):
    """
    participant : "dealer" or "player" dictionary
    """
    if participant["total"] > 21:
        participant["status"] = "bust"
        return "BUST!"
    elif participant["total"] == 21:
        participant["status"] = "bj"
        return "BLACKJACK!"
    elif participant["total"] < 17:
        print("You have to draw another card!")
        participant["status"] = "draw"
    else:
        draw = bool("y" == input("Do you want to draw another card? y/n : "))
        if draw:
            participant["status"] = "draw"
        else:
            participant["status"] = "fold"
    return

def check_dealer(participant):
    """
    participant : "dealer" or "player" dictionary
    """
    if participant["total"] > 21:
        participant["status"] = "bust"
        return "BUST!"
    elif participant["total"] == 21:
        participant["status"] = "bj"
        return "BLACKJACK!"
    elif participant["total"] < 17:
        print("Dealer has to draw another card!")
        participant["status"] = "draw"
    else:
        draw = bool(1 == rnd.randint(0,1))
        if draw:
            print("Dealer chooses to draw another card.")
            participant["status"] = "draw"
        else:
            print("Dealer chooses to fold.")
            participant["status"] = "fold"
    return

#%%
def deck_check(deck):
    if len(deck)<10:
        deck = 4*cards
        print("Deck gets renewed.")
    else:
        pass
    return deck

def newgame():
    another = bool("y" == input("Want to play another game?"))
    if another:
        return blackjack(deck)
    else:
        return False
#        raise Exception("STOP THE COUNT!!!")
#%%
def blackjack(deck):
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    # check deck
    deck_check(deck)

    print(blackjack_logo)
    
    # deal first cards
    # rule is: player invisible, dealer invisible, player invisible, dealer visible
    dealer_cards = draw_cards(1)
    player_cards = draw_cards(1)
    second_dealer = draw_cards(1)
    print(f"dealer has {second_dealer}.")
    dealer_cards += second_dealer
    player_cards += draw_cards(1)
    print(f"you have {player_cards}")
    
    dealer_values = evaluate_cards(dealer_cards)
    player_values = evaluate_cards(player_cards)

    card_status = {
        "dealer" : {"cards" : dealer_cards, "values" : dealer_values, "total" : sum(dealer_values), "status" : "draw"},
        "player" : {"cards" : player_cards, "values" : player_values, "total" : sum(player_values), "status" : "draw"},
    }
    print(card_status)
    # evaluate first draw
    check_player(card_status["player"])

    # player goes on
    while card_status["player"]["status"] == "draw":
        deck_check(deck)
        next_card = draw_cards(1)
        card_status["player"]["cards"] += next_card
        card_status["player"]["values"] += next_card
        card_status["player"]["values"] = evaluate_cards(card_status["player"]["values"])
        card_status["player"]["total"] = sum(card_status["player"]["values"])
        print(f"you have {card_status['player']['cards']}")
        print(card_status)
        check_player(card_status["player"])

    if card_status["player"]["status"] == "bust":
        print("BUST! You LOSE!")
        newgame()
        return
    elif card_status["player"]["status"] == "bj":
        print("BLACKJACK! You WIN!")
        newgame()
        return
    elif card_status["player"]["status"] == "fold":
        print("Let's see, what the dealer has...")
    else:
        newgame()
        return
    # dealer goes on
    print(f"Dealer has {card_status['dealer']['cards']}.")
    check_dealer(card_status["dealer"])
    while card_status["dealer"]["status"] == "draw":
        deck_check(deck)
        next_card = draw_cards(1)
        card_status["dealer"]["cards"] += next_card
        card_status["dealer"]["values"] += next_card
        card_status["dealer"]["values"] = evaluate_cards(card_status["dealer"]["values"])
        card_status["dealer"]["total"] = sum(card_status["dealer"]["values"])
        print(f"Dealer has {card_status['dealer']['cards']}")
        print(card_status)
        check_dealer(card_status["dealer"])

    if card_status["dealer"]["status"] == "bust":
        print("Dealer BUST! You WIN!")
        newgame()
        return
    elif card_status["dealer"]["status"] == "bj":
        print("Dealer has BLACKJACK! You LOSE!")
        newgame()
        return
    elif card_status["dealer"]["status"] == "fold":
        if card_status["dealer"]["total"] > card_status["player"]["total"]:
            print(f"Dealer has {card_status['dealer']['cards']}.\n You have {card_status['player']['cards']}.\n You LOSE!")
            newgame()
            return
        elif card_status["dealer"]["total"] < card_status["player"]["total"]:
            print(f"Dealer has {card_status['dealer']['cards']}.\n You have {card_status['player']['cards']}.\n You WIN!")
            newgame()
            return
        elif card_status["dealer"]["total"] == card_status["player"]["total"]:
            print(f"Dealer has {card_status['dealer']['cards']}.\n You have {card_status['player']['cards']}.\n DRAW!")
            newgame()
            return
    else:
        return
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
deck = 4*cards
blackjack(deck)