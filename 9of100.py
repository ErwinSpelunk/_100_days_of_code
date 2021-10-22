from modules9of100 import logo
import os
clear = lambda: os.system('cls')
clear()
print(logo)
goon = True
#auction = {}
auction = {"A" : 1., "B" : 2., "C" : 3., "D" : 4., }
while goon:
    new_name = input("What is your Name? : ")
    new_bid = round(float(input("What is your bid? : € ")), 2)
    auction[new_name] = new_bid
    goon = bool("y" == input("Is there another bidder? y/n : ").lower())
    clear()

winner = max(auction, key = auction.get)
max_value = "{:.2f}".format(auction[winner])
auction.pop(winner)
second = max(auction)
second_value = "{:.2f}".format(auction[second])
payment = "{:.2f}".format(round(float(second_value) * 1.1, 2))
print(f"The highest bid was given by {winner} with {max_value},")
print(f"second was {second} with {second_value}.")
print(f"{winner} has to pay {payment}")