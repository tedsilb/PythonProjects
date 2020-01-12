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
def calc_hand_value(hand):
  return sum([card.value for card in hand])


# Define function to print current card value
def print_current_value(current_value):
  print(f'The current value of your cards is {current_value}.')


# Define main function
def play_blackjack():
  # Set up deck
  card_deck = []
  def gen_card_deck():
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    faces = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven',
             'eight', 'nine', 'ten', 'jack', 'queen', 'king']
    card_deck.clear()

    # Card number must be unique. Keep track of it here
    unique_card_number = 1
    for i in range(len(suits)):
      for j in range(1, len(faces) + 1):
        # Jack, queen, and king are all ten
        suit_card_no = 10 if (j > 10) else j
        card_deck.append(Card(unique_card_number, suits[i],
                             faces[j - 1], suit_card_no))
        unique_card_number += 1

  # Set up user's hand
  hand = []

  # Set up starting score
  global earned_score
  earned_score = 100

  # Define function to process a turn
  def hit_or_stand():
    choice = input('Would you like to hit or stand? ')
    if choice.lower() in ['hit', 'h']:
      print('Dealing new card...')
      take_new_card()
      bust_return = calc_hand_value(hand)
      if bust_return > 21:
        print('Bust! Subtracting 21 points.')
        global earned_score
        earned_score -= 21
      elif bust_return == 21:
        print('Perfect 21! Ending turn.')
      else:
        print_current_value(calc_hand_value(hand))
        hit_or_stand()
    elif choice.lower() in ['stand', 's']:
      print('Ending turn...')
      end_turn(calc_hand_value(hand))

  # Define function to take a new card
  def take_new_card():
    current_card = random.choice(card_deck)
    # Insert card into hand
    hand.append(current_card)
    # Remove card from deck
    card_deck.remove(current_card)
    # Get index of new card in hand (will be the last one)
    hand_card_index = len(hand) - 1
    print(f'You have taken a {hand[hand_card_index].name} of '
          f'{hand[hand_card_index].suit}.')

  # Define function to start turn
  def start_turn(i, rounds):
    print(f'Starting round {i} of {rounds}.')
    print(f'Your score is currently {earned_score}.')
    print('Drawing two cards...')
    hand.clear()
    take_new_card()
    take_new_card()
    print_current_value(calc_hand_value(hand))
    hit_or_stand()

  # Define function to end turn
  def end_turn(hand_value):
    round_score = 21 - hand_value
    print(f'Round score: {round_score}')
    global earned_score
    earned_score -= round_score
    return

  # Start the game, give direction to user
  print('Blackjack!')
  print('This program will play a game of blackjack.')

  # Run rounds a number of times
  rounds = 5
  for i in range(1, rounds + 1):
    gen_card_deck()
    start_turn(i, rounds)
    if i < rounds:
      print(f'Score after round {i}: {earned_score}')
    else:
      start = f'Final score: {earned_score}. Grade: '
      if earned_score >= 90:
        print(start + 'A')
      elif earned_score >= 80:
        print(start + 'B')
      elif earned_score >= 70:
        print(start + 'C')
      elif earned_score >= 60:
        print(start + 'D')
      else:
        print(start + 'F')

# Call function
play_blackjack()
