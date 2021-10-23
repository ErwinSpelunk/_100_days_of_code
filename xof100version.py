#%%
from modules import blackjack_logo
import random as rnd

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
deck = 4*cards

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
        if len(aces) == 1 and sum(out_cards) <= 21:
            out_cards += [11]
        if len(aces) == 1 and sum(out_cards) > 21:
            out_cards += [1]
    else:
        pass        
    return out_cards
#%%
def compare_cards(player, dealer):
    
    player_total = sum(player)
    dealer_total = sum(dealer)

    if player_total > 21:
        return [-1, "end"]
    elif dealer_total > 21:
        return [1, "end"]
    elif player_total < 17:
        return [1, "another"]
    elif player_total <= 21:
        return [1, "choice"]
    else:
        return "Why did nothing happen?"
#%%
def blackjack():
    
    # shuffle cards
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
    
    # initialize result
    result = [1,""]

    while result[0] == 1 and result[1] != "end":
        # assign card values
        dealer_values = evaluate_cards(dealer_cards)
        player_values = evaluate_cards(player_cards)
        
        # evaluate result
        result = compare_cards(player_values, dealer_values)

        if result[1] == "another":
            print("You have to draw another.")
            newcard = draw_cards(1)
            print("Your next card is: {newcard}")
            player_cards += newcard

        elif result[1] == "choice":
            if "y" == input("Do you want to draw another? y/n : "):
                newcard = draw_cards(1)
                print("Your next card is: {newcard}")
                player_cards += newcard

        another = bool("y" == input("Want to play another game?"))
        if another:
            blackjack()
        else:
            raise Exception("STOP THE COUNT!!!")

blackjack()