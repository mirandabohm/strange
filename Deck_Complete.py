# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 19:26:59 2018
# Test shuttle 
@author: Mira
"""

from random import shuffle, randint
  
# Define the ranks and suits in the deck. 
rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suit = ["Spades", "Clubs", "Diamonds", "Hearts"]

LR = len(rank)
LS = len(suit)

class Card(object):
    def __init__(self, R, S):
        assert (R in rank), "That's not a real rank!"
        assert (S in suit), "That's not a real suit!"
        self.R = R        
        self.S = S
    def __str__(self):
        return str(self.R) + " of " + str(self.S)
    def __repr__(self):
        return str(self)

class Hand(object):
    def __init__(self):
        self.cards = []
        self.count = len(self.cards)
    
    def show_hand(self):
        print self.cards
        
    def return_hand(self, deck):
        print "Now returning your hand to the deck."
        deck.cards.append(self.cards)
        del self.cards[:]
        self.count = len(self.cards)

class Deck(object):
    def __init__(self, duplicates=False):
        self.cards = []
        self.duplicates = duplicates
        for i in range(0,LS):
            for j in range(0, LR):
                k = Card(rank[j],suit[i])
                self.cards.append(k)
                j += 1
            i += 1 
        self.count = len(self.cards)
    
    def draw_one(self, hand):
        """
        Draws card from top of the deck, places it in your hand, and returns hand. 
        """
        drawn = self.cards.pop(0)
        print drawn
        hand.cards.append(drawn)
        
        if len(hand.cards) == 1:
            print "There is currently " + str(len(hand.cards)) + " card in your hand:" + str(hand.cards)
        else:
            print "There are currently " + str(len(hand.cards)) + " cards in your hand:" + str(hand.cards)
                 
        self.count = len(self.cards)
        hand.count = len(hand.cards)
       
    def shuffle(self):
        """
        Self explanatory. Shuffles deck
        """
        shuffle(self.cards)
        print self.cards

    def add_cards(self, index, cards_list):
        """
        Method for adding cards to the deck from a source other than the hand
        """
        if index == "top":
            index = 0
        elif index == "bottom":
            index = 52
        elif index == "middle":
            index = 52/2
        elif index == "random": 
            index = randint(0, 52)
        
        if index < 0 or index > len(self.cards):
            print "The index needs to be between 0 (top of deck) and " + str(len(self.cards)) + " (bottom)."
        else:               
            for x in cards_list: 
                split = x.split(" of ")
                new_rank = split[0]
                new_suit = split[1]     
                new_card = Card(new_rank, new_suit)
                if (not self.duplicates) and (str(new_card) in str(self.cards)):
                    print "This card is already in the deck. " 
                else: 
                    self.cards.insert(index,new_card)  
                    count = "There are " + str(len(self.cards)) +" cards currently in the deck."
                    print "\nYou've added "+ str(len(cards_list)) + " cards to the deck. Now there are "+ str(len(self.cards)) + " cards total."
        self.count = len(self.cards)

    def print_cards(self, index, amount):
        """
        Method for printing a certain part of the deck. 
        Index is index of the first card printed. Amount is # cards printed
        """
        
        if index < 0:        
            print "Choose an index above 0."
        elif index > len(self.cards): 
            print "That index is too large. Choose an index below " + str(len(self.cards))+"."
        else: 
            if amount < 0:
                print "Can't choose a negative amount. Number of cards must be between 0 and " + str(len(self.cards))+ "."
            elif amount > len(self.cards)-index:
                print "ERROR. . . . . . . . .\nCannot print " + str(amount) + " cards from index " + str(index) + ". Please choose " + str(len(self.cards)-index) + " cards or fewer, or choose a smaller index."
            else: 
                print self.cards[index:index+amount]
     
class Game(object):
    def __init__(self):
        pass
    
mydeck = Deck()
myhand = Hand()
mygame = Game()
      
# testhand.draw(awesome_deck)
# testhand.take_a_card(awesome_deck)
    
"""Need to update this so that the DECK always is updated, such that printing
using awesome_deck.print_cards is correct if cards have been added/removed first."""

# awesome_deck.add_card("top", ["Queen of Hearts","Queen of Spades","Queen of Clubs"])
# print awesome_deck.count
# awesome_deck.print_cards(0,9)

# awesome_deck.shuffle_me()
# print awesome_deck.cards
   
"""
BACKUP
for i in range(0,len(suit)):
    for j in range(0, len(rank)):
        k = Card(rank[j],suit[i])
        Deck.append(k)
        j += 1
    i += 1 
"""

"""
BACKUP
    def return_card(self, index, new_rank, new_suit):
        if index == "top":
            index = 0
        elif index == "bottom":
            index = 52
        elif index == "middle":
            index = 52/2
        elif index == "random": 
            index = randint(0, 52)
        
        if index < 0 or index > len(self.cards):
            print "The index needs to be between 0 (top of deck) and " + str(len(self.cards)) + " (bottom)."
        else:               
            new_card = Card(new_rank,new_suit)
            self.cards.insert(index,new_card)
            print self.cards
"""