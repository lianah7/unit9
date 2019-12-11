# created by Liana Hill
# last modified on December 5, 2019
# unit 9 option one - this program plays a game of Compare (a small game of War) between the user and dealer

import card
import deck


def deal_cards(my_deck):
    user_cards = []
    for x in range(5):
        user_card = my_deck.deal()
        user_cards.append(user_card)
    return user_cards


def compare_cards(user_card, dealer_card):
    if user_card > dealer_card:
        print("The user wins!")
        return True
    elif dealer_card > user_card:
        print("The dealer wins!")
        return False


def main():
    my_deck = deck.Deck()
    my_deck.shuffle()
    user_deal = deal_cards(my_deck)
    dealer_deal = deal_cards(my_deck)
    user_score = 0
    dealer_score = 0
    for x in range(5):
        print("The user has", user_deal[x])
        print("The dealer has", dealer_deal[x])
        if compare_cards(user_deal[x], dealer_deal[x]):
            user_score += 1
        else:
            dealer_score += 1
        print("")
        print("The user's final score is", user_score, "and the dealer's final score is", dealer_score)



main()
