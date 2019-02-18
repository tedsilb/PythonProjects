# This program will play a game of blackjack

# Import dependencies
import random

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
    cardDeck[1] = Card(1, 'Hearts', 'ace', 1),
    cardDeck[2] = Card(2, 'Hearts', 'two', 2),
    cardDeck[3] = Card(3, 'Hearts', 'three', 3),
    cardDeck[4] = Card(4, 'Hearts', 'four', 4),
    cardDeck[5] = Card(5, 'Hearts', 'five', 5),
    cardDeck[6] = Card(6, 'Hearts', 'six', 6),
    cardDeck[7] = Card(7, 'Hearts', 'seven', 7),
    cardDeck[8] = Card(8, 'Hearts', 'eight', 8),
    cardDeck[9] = Card(9, 'Hearts', 'nine', 9),
    cardDeck[10] = Card(10, 'Hearts', 'ten', 10),
    cardDeck[11] = Card(11, 'Hearts', 'jack', 10),
    cardDeck[12] = Card(12, 'Hearts', 'queen', 10),
    cardDeck[13] = Card(13, 'Hearts', 'king', 10),
    cardDeck[14] = Card(14, 'Diamonds', 'ace', 1),
    cardDeck[15] = Card(15, 'Diamonds', 'two', 2),
    cardDeck[16] = Card(16, 'Diamonds', 'three', 3),
    cardDeck[17] = Card(17, 'Diamonds', 'four', 4),
    cardDeck[18] = Card(18, 'Diamonds', 'five', 5),
    cardDeck[19] = Card(19, 'Diamonds', 'six', 6),
    cardDeck[20] = Card(20, 'Diamonds', 'seven', 7),
    cardDeck[21] = Card(21, 'Diamonds', 'eight', 8),
    cardDeck[22] = Card(22, 'Diamonds', 'nine', 9),
    cardDeck[23] = Card(23, 'Diamonds', 'ten', 10),
    cardDeck[24] = Card(24, 'Diamonds', 'jack', 10),
    cardDeck[25] = Card(25, 'Diamonds', 'queen', 10),
    cardDeck[26] = Card(26, 'Diamonds', 'king', 10),
    cardDeck[27] = Card(27, 'Spades', 'ace', 1),
    cardDeck[28] = Card(28, 'Spades', 'two', 2),
    cardDeck[29] = Card(29, 'Spades', 'three', 3),
    cardDeck[30] = Card(30, 'Spades', 'four', 4),
    cardDeck[31] = Card(31, 'Spades', 'five', 5),
    cardDeck[32] = Card(32, 'Spades', 'six', 6),
    cardDeck[33] = Card(33, 'Spades', 'seven', 7),
    cardDeck[34] = Card(34, 'Spades', 'eight', 8),
    cardDeck[35] = Card(35, 'Spades', 'nine', 9),
    cardDeck[36] = Card(36, 'Spades', 'ten', 10),
    cardDeck[37] = Card(37, 'Spades', 'jack', 10),
    cardDeck[38] = Card(38, 'Spades', 'queen', 10),
    cardDeck[39] = Card(39, 'Spades', 'king', 10),
    cardDeck[40] = Card(40, 'Clubs', 'ace', 1),
    cardDeck[41] = Card(41, 'Clubs', 'two', 2),
    cardDeck[42] = Card(42, 'Clubs', 'three', 3),
    cardDeck[43] = Card(43, 'Clubs', 'four', 4),
    cardDeck[44] = Card(44, 'Clubs', 'five', 5),
    cardDeck[45] = Card(45, 'Clubs', 'six', 6),
    cardDeck[46] = Card(46, 'Clubs', 'seven', 7),
    cardDeck[47] = Card(47, 'Clubs', 'eight', 8),
    cardDeck[48] = Card(48, 'Clubs', 'nine', 9),
    cardDeck[49] = Card(49, 'Clubs', 'ten', 10),
    cardDeck[50] = Card(50, 'Clubs', 'jack', 10),
    cardDeck[51] = Card(51, 'Clubs', 'queen', 10),
    cardDeck[52] = Card(52, 'Clubs', 'king', 10)

  # Define function to process a turn
  def takeTurn():
    choice = input('Would you like to hit or stand?')
    if (choice.lower() == 'hit') or (choice.lower() == 'h'):
      print('Dealing new card...')
      takeNewCard()
    elif (choice.lower() == 'stand') or (choice.lower() == 's'):
      print('Ending turn...')
      endTurn()
      return

  # Define function to calculate hand value
  def calcHandValue():
    handValue = 0
    for card in hand:
      handValue += card['value']

  # Define function to take a new card
  def takeNewCard():
    currentCardIndex = random.choice(list(cardDeck.keys()))
    # Insert card into hand
    hand[currentCardIndex] = cardDeck[currentCardIndex]

  # Define function to end turn
  def endTurn():
    1 == 1  # placeholder

  # Generate card deck, initially
  genCardDeck()

  # Set up user's hand
  hand = {}
  handValue = 0

  # Set up starting score
  score = 100

  # Start the game, give direction to user
  print('Blackjack!')
  print('This game will play a game of blackjack.')

  # temp
  takeNewCard()

# Call function
playBlackjack()