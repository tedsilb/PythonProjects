# Magic 8 ball.
# By Ted Silbernagel

import random
from typing import Text, Dict


def magic_8_ball(question: Text) -> Dict[Text, Text]:
  # Set up array to store responses and values
  # Answers from https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers
  responses = [
    ['It is certain.', 'positive'],
    ['It is decidedly so.', 'positive'],
    ['Without a doubt.', 'positive'],
    ['Yes - definitely.', 'positive'],
    ['You may rely on it.', 'positive'],
    ['As I see it, yes.', 'positive'],
    ['Most likely.', 'positive'],
    ['Outlook good.', 'positive'],
    ['Yes.', 'positive', 'positive'],
    ['Signs point to yes.', 'positive'],

    ['Reply hazy, try again.', 'non-committal'],
    ['Ask again later.', 'non-committal'],
    ['Better not tell you now.', 'non-committal'],
    ['Cannot predict now.', 'non-committal'],
    ['Concentrate and ask again.', 'non-committal'],

    ['Don\'t count on it.', 'negative'],
    ['My reply is no.', 'negative'],
    ['My sources say no.', 'negative'],
    ['Outlook not so good.', 'negative'],
    ['Very doubtful.', 'negative']
  ]

  # Choose a random response
  chosen_response = responses[random.randint(0, len(responses) - 1)]

  # Return data
  return {
    'question': question,
    'answer': chosen_response[0],
    'value': chosen_response[1],
  }


# Get user input, call function
print('Magic 8-ball...')
response = magic_8_ball(input('Please enter your question: '))

# Print response for user
print(f'Your question was: \"{response["question"]}\"')
print(f'The Magic 8-ball\'s answer: \"{response["answer"]}\" '
      f'({response["value"]})')
