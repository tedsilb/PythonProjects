# This program will play a game of blackjack
# By Ted Silbernagel

# Import dependencies
import random


# Set up card class
class Card(object):
  def __init__(self, number, suit, name, value):
    self.number = number
    self.suit = suit
    self.name = name
    self.value = value


# Define function to calculate hand value
def calcHandValue(hand):
  return sum([card.value for card in hand])


# Define function to print current card value
def printCurrentValue(currentValue):
  print(f'The current value of your cards is {currentValue}.')


# Define main function
def playBlackjack():
  # Set up deck
  cardDeck = []
  def genCardDeck():
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    faces = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven',
             'eight', 'nine', 'ten', 'jack', 'queen', 'king']
    cardDeck.clear()

    # Card number must be unique. Keep track of it here
    uniqueCardNumber = 1
    for i in range(len(suits)):
      for j in range(1, len(faces) + 1):
        # Jack, queen, and king are all ten
        suitCardNo = 10 if (j > 10) else j
        cardDeck.append(Card(uniqueCardNumber, suits[i], faces[j - 1], suitCardNo))
        uniqueCardNumber += 1

  # Set up user's hand
  hand = []

  # Set up starting score
  global earnedScore
  earnedScore = 100

  # Define function to process a turn
  def hitOrStand():
    choice = input('Would you like to hit or stand? ')
    if (choice.lower() in ['hit', 'h']):
      print('Dealing new card...')
      takeNewCard()
      bustReturn = calcHandValue(hand)
      if bustReturn > 21:
        print('Bust! Subtracting 21 points.')
        global earnedScore
        earnedScore -= 21
      elif bustReturn == 21:
        print('Perfect 21! Ending turn.')
      else:
        printCurrentValue(calcHandValue(hand))
        hitOrStand()
    elif (choice.lower() in ['stand', 's']):
      print('Ending turn...')
      endTurn(calcHandValue(hand))

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
    printCurrentValue(calcHandValue(hand))
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
      start = f'Final score: {earnedScore}. Grade: '
      if earnedScore >= 90:
        print(start + 'A')
      elif earnedScore >= 80:
        print(start + 'B')
      elif earnedScore >= 70:
        print(start + 'C')
      elif earnedScore >= 60:
        print(start + 'D')
      else:
        print(start + 'F')

# Call function
playBlackjack()
