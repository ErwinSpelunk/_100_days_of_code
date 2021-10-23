#%%
from modules import blackjack_logo
import random as rnd


outcome = ["draw", "win", "lose"]
# remember 0, 1, -1 for draw, win, lose
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
def result(cards):
    card_total = sum(cards)
    if card_total >= 21:
        print("Bust!")
#%%
def blackjack(deck):
    # shuffle deck
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    if len(deck)<10:
        deck = 4*cards
    else:
        pass

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
        "dealer" : {"d_cards" : dealer_cards, "d_values" : dealer_values, "d_total" : sum(dealer_values), "d_status" : 0},
        "player" : {"p_cards" : player_cards, "p_values" : player_values, "p_total" : sum(player_values), "p_status" : 0},
    }
    print(card_status)
    # TODO 1: evaluate first draw

    # TODO 0: make BUST-check a function?
    dealer = card_status["dealer"]
    if dealer["d_total"] >= 21:
        dealer["d_status"] = -1
    # TODO 2: player draws

    # TODO 3: dealer draws

    another = bool("y" == input("Want to play another game?"))
    if another:
        blackjack(deck)
    else:
        raise Exception("STOP THE COUNT!!!")
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
deck = 4*cards
blackjack(deck)
# %%
