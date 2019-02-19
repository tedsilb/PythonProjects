# This program will play a game of blackjack

# Import dependencies
import random

# Define function
def playBlackjack():
  # Set up card class
  class Card(object):
    def __init__(self, number, suit, name, value):
      self.number = number
      self.suit = suit
      self.name = name
      self.value = value

  # Set up deck
  cardDeck = []
  def genCardDeck():
    sH = 'hearts'
    sD = 'diamonds'
    sS = 'spades'
    sC = 'clubs'
    cardDeck.clear()
    cardDeck.append(Card(1, sH, 'ace', 1))
    cardDeck.append(Card(2, sH, 'two', 2))
    cardDeck.append(Card(3, sH, 'three', 3))
    cardDeck.append(Card(4, sH, 'four', 4))
    cardDeck.append(Card(5, sH, 'five', 5))
    cardDeck.append(Card(6, sH, 'six', 6))
    cardDeck.append(Card(7, sH, 'seven', 7))
    cardDeck.append(Card(8, sH, 'eight', 8))
    cardDeck.append(Card(9, sH, 'nine', 9))
    cardDeck.append(Card(10, sH, 'ten', 10))
    cardDeck.append(Card(11, sH, 'jack', 10))
    cardDeck.append(Card(12, sH, 'queen', 10))
    cardDeck.append(Card(13, sH, 'king', 10))
    cardDeck.append(Card(14, sD, 'ace', 1))
    cardDeck.append(Card(15, sD, 'two', 2))
    cardDeck.append(Card(16, sD, 'three', 3))
    cardDeck.append(Card(17, sD, 'four', 4))
    cardDeck.append(Card(18, sD, 'five', 5))
    cardDeck.append(Card(19, sD, 'six', 6))
    cardDeck.append(Card(20, sD, 'seven', 7))
    cardDeck.append(Card(21, sD, 'eight', 8))
    cardDeck.append(Card(22, sD, 'nine', 9))
    cardDeck.append(Card(23, sD, 'ten', 10))
    cardDeck.append(Card(24, sD, 'jack', 10))
    cardDeck.append(Card(25, sD, 'queen', 10))
    cardDeck.append(Card(26, sD, 'king', 10))
    cardDeck.append(Card(27, sS, 'ace', 1))
    cardDeck.append(Card(28, sS, 'two', 2))
    cardDeck.append(Card(29, sS, 'three', 3))
    cardDeck.append(Card(30, sS, 'four', 4))
    cardDeck.append(Card(31, sS, 'five', 5))
    cardDeck.append(Card(32, sS, 'six', 6))
    cardDeck.append(Card(33, sS, 'seven', 7))
    cardDeck.append(Card(34, sS, 'eight', 8))
    cardDeck.append(Card(35, sS, 'nine', 9))
    cardDeck.append(Card(36, sS, 'ten', 10))
    cardDeck.append(Card(37, sS, 'jack', 10))
    cardDeck.append(Card(38, sS, 'queen', 10))
    cardDeck.append(Card(39, sS, 'king', 10))
    cardDeck.append(Card(40, sC, 'ace', 1))
    cardDeck.append(Card(41, sC, 'two', 2))
    cardDeck.append(Card(42, sC, 'three', 3))
    cardDeck.append(Card(43, sC, 'four', 4))
    cardDeck.append(Card(44, sC, 'five', 5))
    cardDeck.append(Card(45, sC, 'six', 6))
    cardDeck.append(Card(46, sC, 'seven', 7))
    cardDeck.append(Card(47, sC, 'eight', 8))
    cardDeck.append(Card(48, sC, 'nine', 9))
    cardDeck.append(Card(49, sC, 'ten', 10))
    cardDeck.append(Card(50, sC, 'jack', 10))
    cardDeck.append(Card(51, sC, 'queen', 10))
    cardDeck.append(Card(52, sC, 'king', 10))

  # Set up user's hand
  hand = []

  # Set up starting score
  global earnedScore
  earnedScore = 100

  # Define function to process a turn
  def hitOrStand():
    choice = input('Would you like to hit or stand? ')
    if (choice.lower() == 'hit') or (choice.lower() == 'h'):
      print('Dealing new card...')
      takeNewCard()
      bustReturn = calcHandValue()
      if bustReturn > 21:
        print('Bust! Subtracting 21 points.')
      elif bustReturn == 21:
        print('Perfect 21! Ending turn.')
      else:
        currentValue()
        hitOrStand()
    elif (choice.lower() == 'stand') or (choice.lower() == 's'):
      print('Ending turn...')
      endTurn(calcHandValue())

  # Define function to print current card value
  def currentValue():
    value = calcHandValue()
    print(f'The current value of your cards is {value}.')

  # Define function to calculate hand value
  def calcHandValue():
    handValue = 0
    for card in hand:
      handValue += card.value
    return handValue

  # Define function to take a new card
  def takeNewCard():
    currentCard = random.choice(cardDeck)
    # Insert card into hand
    hand.append(currentCard)
    # Remove card from deck
    cardDeck.remove(currentCard)
    # Get index of new card in hand (will be the last one)
    handCardIndex = len(hand) - 1
    print(f'You have taken a {hand[handCardIndex].name} of {hand[handCardIndex].suit}.')

  # Define function to start turn
  def startTurn(i, rounds):
    print(f'Starting round {i} of {rounds}.')
    print(f'Your score is currently {earnedScore}.')
    print('Drawing two cards...')
    hand.clear()
    takeNewCard()
    takeNewCard()
    currentValue()
    hitOrStand()

  # Define function to end turn
  def endTurn(handValue):
    roundScore = 21 - handValue
    print(f'Round score: {roundScore}')
    global earnedScore
    earnedScore -= roundScore
    return

  # Start the game, give direction to user
  print('Blackjack!')
  print('This program will play a game of blackjack.')

  # Run rounds a number of times
  rounds = 5
  for i in range(1, rounds + 1):
    genCardDeck()
    startTurn(i, rounds)
    if i < rounds:
      print(f'Score after round {i}: {earnedScore}')
    else:
      print(f'Final score: {earnedScore}')

# Call function
playBlackjack()