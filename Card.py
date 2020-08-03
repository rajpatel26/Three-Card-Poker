#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import copy

class Card(object):
    """
    A generic Card class
    """
    
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 
             'Jack', 'Queen', 'King', 'Ace']
    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def get_rank(self):
        return self.rank
    
    
    def get_suit(self):
        """
        Returns the value of the
        suit attribute
        """
        return self.suit


    def __str__(self):
        return Card.ranks[self.rank] + ' of ' + Card.suits[self.suit]
    
class Deck(object):
    """
    A standard deck of 52 cards
    """
    
    def __init__(self):
        self.cards = []
        for rank in range(len(Card.ranks)):
            for suit in range(len(Card.suits)):
                self.cards.append(Card(rank, suit))

         
    def shuffle(self):
        """
        Use the random.shuffle method
        to randomly shuffle the list of cards.
        """
        random.shuffle(self.cards)
        
    
    def pop_cards(self, n):
        """
        n, positive integer.
        Returns a list of n Card objects 
        at the end of self.cards, and 
        removes the returned cards from 
        self.cards.
        """
        pop_cards = []
        for i in range (n):
            l = self.cards.pop()
            pop_cards.append(l)
        return pop_cards
    
  
    def add_cards(self, cards):
        """
        cards, a list of Card objects.
        Extends self.cards with a
        deep copy of the cards parameter.
        Use the copy.deepcopy() method of 
        the Python's copy library.
        """
        self.cards.extend(copy.deepcopy(cards))
        
    
    def clear_cards(self):
        """
        Clears the content of self.cards. Be
        careful to NOT remove the entire attribute!
        """
        self.cards.clear()
        
     
    def move_cards(self, hand, n):
        """
        hand, a Hand object
        n, a positive integer
        Uses add_cards and pop_cards to 
        move n cards from self to hand
        """   
        hand.add_cards(self.pop_cards(n))
        
        
    def __str__(self):
        lst = [str(card) for card in self.cards]
        return '\n'.join(lst)
    
class Hand(Deck):
    """
    A generic Hand class
    """

    def __init__(self, name=""):
        self.cards = []
        self.name = name
        
    #   Question 1 
    def get_name(self):
        """
        Return the value of the 
        name attribute
        """
        return self.name
        
    def __str__(self):
        return self.name + "'s Hand:\n" + Deck.__str__(self)

if __name__ == '__main__':    

    d = Deck()
    print(d)
    print()
    h = Hand()
    d.move_cards(h, 5)
    print(d)
    print()
    print(h)
    d.add_cards([Card(0, 0), Card(1, 1)])
    print(d) 
    print()
    d = Deck()
    h = Hand('Dealer')
    print(h)
    print()
    d.shuffle()
    d.move_cards(h, 3);
