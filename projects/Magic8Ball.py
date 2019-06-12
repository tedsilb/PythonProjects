# Magic 8 ball.
# By Ted Silbernagel

# Import dependencies
from random import randint

# Define main function
def magic8Ball(question):
  # Set up array to store responses and values
  # Answers taken from https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers
  responses = [ ['It is certain.', 'positive'],
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
  chosenResponse = responses[randint(0, len(responses) - 1)]

  # Compile data into dict for returning
  returnValues = {}
  returnValues['question'] = question
  returnValues['answer'] = chosenResponse[0]
  returnValues['value'] = chosenResponse[1]

  # Return data
  return returnValues

# Get user input
print('Magic 8-ball...')
userQuestion = input('Please enter your question: ')

# Call function
response = magic8Ball(userQuestion)

# Print response for user
print(f'Your question is: \"{response["question"]}\"')
print(f'The Magic 8-ball\'s answer: \"{response["answer"]}\" ({response["value"]})')
