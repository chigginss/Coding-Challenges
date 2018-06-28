"""
Part 1

We will be implementing a modified version of the real card game Set.
Our version of Set involves a deck of 27 cards. Each Set card has a
shape, shading and count. Possible values for each attribute are:

shapes = ["oval", "squiggle", "diamond"]
shadings = ["solid", "striped", "open"]
counts = [1, 2, 3]

Create a class SetCard that models a Set card.
This class must include a means of printing a SetCard as a string.
Then print the string representation of a card.

Part 2

Create a SetGame class. On initialization, generate a deck of Set cards
that is stored within the class instance. The order of the deck does not
matter, as long as all 27 unique cards are present.

Part 3

In a game of Set, cards are dealt onto the table at a given time. Edit SetGame
to track the cards that are currently on the table using an instance
variable "table." Write a function deal(num_cards) in SetGame that deals
num_cards random cards onto the table from the deck.

Part 4

Write a function is_set() that accepts three cards and returns a boolean
indicating whether the three cards make up a valid set. A set is valid if all
three conditions hold:
1. Shape: all the same shape OR all different shapes
2. Shading: all the same shading OR all different shading
3. Count: all the same count OR all different count

Example set:
["oval", "solid", 1], ["oval", "solid", 2], ["oval", "solid", 3]

Example _not_ set:
["oval", "solid", 1], ["oval", "striped", 2], ["oval", "solid", 3]

Part 5

Write a function find_set() in class SetGame that finds one possible set
among the table cards and prints it out. The function should return a boolean
indicating whether or not a set was found. Handle the case where there are no
sets in a graceful manner.

"""

import random


class SetCard(object):
     
    def __init__(self, count, shape, shade):
        self.shape = shape
        self.shade = shade
        self.count = count
    
    def __repr__(self):
        return "{shape} {shade} {count}".format(
          shape=self.shape, shade=self.shade, count=self.count)


class SetGame(object):
    shapes = ["oval", "squiggle", "diamond"]
    shadings = ["solid", "striped", "open"]
    counts = [1, 2, 3]

    def __init__(self):
        self.deck = []
        self.table = []
        for num in SetGame.counts:
            for shape in SetGame.shapes:
                for shade in SetGame.shadings:
                    self.deck.append(SetCard(num, shape, shade))
                    
    def deal_cards(self, num_cards):
        
        if len(self.deck) < num_cards :
            raise ValueError("Not enough cards in deck")
        
        for i in range(num_cards):
            card = random.choice(self.deck)
            self.table.append(card)
            self.deck.remove(card)
    
    @staticmethod
    def is_set(cards):
        shapes = set()
        counts = set()
        shades = set()
        
        for card in cards:
            shapes.add(card.shape)
            counts.add(card.count)
            shades.add(card.shade)
        
        return ((len(shapes) == len(cards) or len(shapes) == 1) and
                (len(shades) == len(cards) or len(shades) == 1) and
                (len(counts) == len(cards) or len(counts) == 1))




testgame = SetGame()
assert len(testgame.deck) == 27, "Deck must instantiate with 27 cards"

testgame.deal_cards(5)
assert len(testgame.table) == 5, "deal_cards() failed to deal correct number of cards to the table"
assert len(testgame.deck) == 22, "deal_cards() failed to remove cards from the deck"

isset = [SetCard("oval", "solid", 1), SetCard("oval", "solid", 2), SetCard("oval", "solid", 3)]
assert SetGame.is_set(isset), "Known vaild set tested false"

notset = [SetCard("oval", "solid", 1), SetCard("oval", "striped", 2), SetCard("oval", "solid", 3)]
assert not SetGame.is_set(notset), "Known invalid set tested true"

testgame.table.extend(isset)
assert testgame.find_set(), "Known valid set was not found on the table"

testgame = SetGame()
testgame.table.extend(notset)
assert not testgame.find_set(), "Known invalid set was found as set on the table"

print "All tests passed!"





