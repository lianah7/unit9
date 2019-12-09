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
    elif dealer_card > user_card:
        print("The dealer wins!")


def main():
    my_deck = deck.Deck()
    my_deck.shuffle()
    user_deal = deal_cards(my_deck)
    dealer_deal = deal_cards(my_deck)
    for x in range:

    print("The user has the cards:")
    for y in user_deal:
        print(y)
    print("")

    print("The dealer has the cards:")
    for z in dealer_deal:
        print(z)
    for x in range(5):
        print("")
        compare_cards(user_deal, dealer_deal)


main()