# This program will play a game of blackjack

# Define function
def playBlackjack():
  # Set up card class
  class Card:
    def __init__(self, number, suit, name, value):
      self.number = number
      self.suit = suit
      self.name = name
      self.value = value

  # Set up deck
  cardDeck = {}
  def genCardDeck():
    cardDeck = {
      1: Card(1, 'Hearts', 'ace', 1),
      2: Card(2, 'Hearts', 'two', 2),
      3: Card(3, 'Hearts', 'three', 3),
      4: Card(4, 'Hearts', 'four', 4),
      5: Card(5, 'Hearts', 'five', 5),
      6: Card(6, 'Hearts', 'six', 6),
      7: Card(7, 'Hearts', 'seven', 7),
      8: Card(8, 'Hearts', 'eight', 8),
      9: Card(9, 'Hearts', 'nine', 9),
      1: Card(10, 'Hearts', 'ten', 10),
      11: Card(11, 'Hearts', 'jack', 10),
      12: Card(12, 'Hearts', 'queen', 10),
      13: Card(13, 'Hearts', 'king', 10),
      14: Card(14, 'Diamonds', 'ace', 1),
      15: Card(15, 'Diamonds', 'two', 2),
      16: Card(16, 'Diamonds', 'three', 3),
      17: Card(17, 'Diamonds', 'four', 4),
      18: Card(18, 'Diamonds', 'five', 5),
      19: Card(19, 'Diamonds', 'six', 6),
      20: Card(20, 'Diamonds', 'seven', 7),
      21: Card(21, 'Diamonds', 'eight', 8),
      22: Card(22, 'Diamonds', 'nine', 9),
      23: Card(23, 'Diamonds', 'ten', 10),
      24: Card(24, 'Diamonds', 'jack', 10),
      25: Card(25, 'Diamonds', 'queen', 10),
      26: Card(26, 'Diamonds', 'king', 10),
      27: Card(27, 'Spades', 'ace', 1),
      28: Card(28, 'Spades', 'two', 2),
      29: Card(29, 'Spades', 'three', 3),
      30: Card(30, 'Spades', 'four', 4),
      31: Card(31, 'Spades', 'five', 5),
      32: Card(32, 'Spades', 'six', 6),
      33: Card(33, 'Spades', 'seven', 7),
      34: Card(34, 'Spades', 'eight', 8),
      35: Card(35, 'Spades', 'nine', 9),
      36: Card(36, 'Spades', 'ten', 10),
      37: Card(37, 'Spades', 'jack', 10),
      38: Card(38, 'Spades', 'queen', 10),
      39: Card(39, 'Spades', 'king', 10),
      40: Card(40, 'Clubs', 'ace', 1),
      41: Card(41, 'Clubs', 'two', 2),
      42: Card(42, 'Clubs', 'three', 3),
      43: Card(43, 'Clubs', 'four', 4),
      44: Card(44, 'Clubs', 'five', 5),
      45: Card(45, 'Clubs', 'six', 6),
      46: Card(46, 'Clubs', 'seven', 7),
      47: Card(47, 'Clubs', 'eight', 8),
      48: Card(48, 'Clubs', 'nine', 9),
      49: Card(49, 'Clubs', 'ten', 10),
      50: Card(50, 'Clubs', 'jack', 10),
      51: Card(51, 'Clubs', 'queen', 10),
      52: Card(52, 'Clubs', 'king', 10)
    }

  # Define function to process a turn
  def takeTurn():
    choice = input('Would you like to hit or stand?')
    if (choice.lower() == 'hit') or (choice.lower() == 'h'):
      print('Dealing new card...')
      takeNewCard()
    elif (choice.lower() == 'stand') or (choice.lower() == 's'):
      print('Ending turn...')
      return

  # Define function to take a new card
  def takeNewCard():
    1 == 1  # placeholder

  # Set up user's hand
  hand = {}

  # Set up starting score
  score = 100

  # Start the game, give direction to user
  print('Blackjack!')
  print('This game will play a game of blackjack.')

# Call function
playBlackjack()