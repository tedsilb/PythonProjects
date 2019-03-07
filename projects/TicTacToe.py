# A Tic Tac Toe program. Uses tkinter for GUI. This is my first program ever to use a GUI
# By Ted Silbernagel

# TODO: Make who starts (user/cpu) random. Teach cpu how to start the game smartly

# Import dependencies
import tkinter as tk
from random import choice
from functools import partial

# Set up class for GUI
class TicTacToe:
  def __init__(self, master):
    # Set up core
    self.master = master
    master.title('Tic Tac Toe')

    # Set up base variables
    self.availableCells = []
    self.userChosenCells = []
    self.cpuChosenCells = []
    self.userIcon = 'X'
    self.cpuIcon = 'O'
    self.buttonFont = ('Helvetica', 90)

    # Define buttons
    self.btnA1 = tk.Button(master, height = 1, width = 2)
    self.btnA2 = tk.Button(master, height = 1, width = 2)
    self.btnA3 = tk.Button(master, height = 1, width = 2)
    self.btnB1 = tk.Button(master, height = 1, width = 2)
    self.btnB2 = tk.Button(master, height = 1, width = 2)
    self.btnB3 = tk.Button(master, height = 1, width = 2)
    self.btnC1 = tk.Button(master, height = 1, width = 2)
    self.btnC2 = tk.Button(master, height = 1, width = 2)
    self.btnC3 = tk.Button(master, height = 1, width = 2)

    # Set grid locations
    self.btnA1.grid(row = 1, column = 1)
    self.btnA2.grid(row = 1, column = 2)
    self.btnA3.grid(row = 1, column = 3)
    self.btnB1.grid(row = 2, column = 1)
    self.btnB2.grid(row = 2, column = 2)
    self.btnB3.grid(row = 2, column = 3)
    self.btnC1.grid(row = 3, column = 1)
    self.btnC2.grid(row = 3, column = 2)
    self.btnC3.grid(row = 3, column = 3)

    # Define button commands
    self.btnA1['command'] = partial(self.buttonPress, self.btnA1, 'A1')
    self.btnA2['command'] = partial(self.buttonPress, self.btnA2, 'A2')
    self.btnA3['command'] = partial(self.buttonPress, self.btnA3, 'A3')
    self.btnB1['command'] = partial(self.buttonPress, self.btnB1, 'B1')
    self.btnB2['command'] = partial(self.buttonPress, self.btnB2, 'B2')
    self.btnB3['command'] = partial(self.buttonPress, self.btnB3, 'B3')
    self.btnC1['command'] = partial(self.buttonPress, self.btnC1, 'C1')
    self.btnC2['command'] = partial(self.buttonPress, self.btnC2, 'C2')
    self.btnC3['command'] = partial(self.buttonPress, self.btnC3, 'C3')

    # Set button fonts
    self.btnA1['font'] = self.buttonFont
    self.btnA2['font'] = self.buttonFont
    self.btnA3['font'] = self.buttonFont
    self.btnB1['font'] = self.buttonFont
    self.btnB2['font'] = self.buttonFont
    self.btnB3['font'] = self.buttonFont
    self.btnC1['font'] = self.buttonFont
    self.btnC2['font'] = self.buttonFont
    self.btnC3['font'] = self.buttonFont

    # Set up bottom label
    self.bottomLabel = tk.Label(master)
    self.bottomLabel.grid(row = 4, column = 1, columnspan = 2, rowspan = 2, sticky = tk.N + tk.S + tk.W + tk.E)
    self.bottomLabel['font'] = ('Helvetica', 12, 'bold')

    # Set up reset game button
    self.bottomButton = tk.Button(master, text = 'Reset Game', command = self.resetGame)
    self.bottomButton.grid(row = 4, column = 3, columnspan = 2, pady = (15, 15))

    # Reset game, initially
    self.resetGame()

  # Set up function to handle button presses
  def buttonPress(self, button, gridLoc):
    # Ensure buttons are enabled
    if self.buttonsEnabled == True:
      # Ensure cell isn't yet selected
      if button['text'] == '':
        # Set the cell as checked and chosen, remove from available
        button['text'] = self.userIcon
        # Set cell as chosen, remove from available
        self.userChosenCells.append(gridLoc)
        self.availableCells.remove(gridLoc)
        # Check to see if you won
        if self.hasWon(self.userIcon):
          self.bottomLabel['text'] = 'You win!'
          self.buttonsEnabled = False
        # If you didn't win, take computer's turn
        else:
          self.takeCpuTurn()

      # If cell's selected, display error
      else:
        self.bottomLabel['text'] = 'Spot already selected. Try again.'

  # Set up function to take CPU turn
  def takeCpuTurn(self):
    self.bottomLabel['text'] = 'Computer\'s turn...'
    # Block winning moves by user
    # A block
    if (('A2' in self.userChosenCells and 'A3' in self.userChosenCells) \
      or ('B1' in self.userChosenCells and 'C1' in self.userChosenCells) \
      or ('B2' in self.userChosenCells and 'C3' in self.userChosenCells)) \
      and 'A1' in self.availableCells:
      self.cpuChoice = 'A1'
    elif (('A1' in self.userChosenCells and 'A3' in self.userChosenCells) \
      or ('B2' in self.userChosenCells and 'C2' in self.userChosenCells)) \
      and 'A2' in self.availableCells:
      self.cpuChoice = 'A2'
    elif (('A1' in self.userChosenCells and 'A2' in self.userChosenCells) \
      or ('B3' in self.userChosenCells and 'C3' in self.userChosenCells) \
      or ('C1' in self.userChosenCells and 'B2' in self.userChosenCells)) \
      and 'A3' in self.availableCells:
      self.cpuChoice = 'A3'
    # B block
    elif (('B2' in self.userChosenCells and 'B3' in self.userChosenCells) \
      or ('A1' in self.userChosenCells and 'C1' in self.userChosenCells)) \
      and 'B1' in self.availableCells:
      self.cpuChoice = 'B1'
    elif (('B1' in self.userChosenCells and 'B3' in self.userChosenCells) \
      or ('A2' in self.userChosenCells and 'C2' in self.userChosenCells) \
      or ('A1' in self.userChosenCells and 'C3' in self.userChosenCells)) \
      and 'B2' in self.availableCells:
      self.cpuChoice = 'B2'
    elif (('B1' in self.userChosenCells and 'B2' in self.userChosenCells) \
      or ('A3' in self.userChosenCells and 'C3' in self.userChosenCells)) \
      and 'B3' in self.availableCells:
      self.cpuChoice = 'B3'
    # C block
    elif (('C2' in self.userChosenCells and 'C3' in self.userChosenCells) \
      or ('A1' in self.userChosenCells and 'B1' in self.userChosenCells) \
      or ('B2' in self.userChosenCells and 'A3' in self.userChosenCells)) \
      and 'C1' in self.availableCells:
      self.cpuChoice = 'C1'
    elif (('C1' in self.userChosenCells and 'C3' in self.userChosenCells) \
      or ('A2' in self.userChosenCells and 'B2' in self.userChosenCells)) \
      and 'C2' in self.availableCells:
      self.cpuChoice = 'C2'
    elif (('C1' in self.cpuChosenCells and 'C2' in self.userChosenCells) \
      or ('B3' in self.userChosenCells and 'C3' in self.userChosenCells) \
      or ('C1' in self.userChosenCells and 'B2' in self.userChosenCells)) \
      and 'C3' in self.availableCells:
      self.cpuChoice = 'C3'

    # Take winning moves for cpu
    # A block
    elif (('A2' in self.cpuChosenCells and 'A3' in self.cpuChosenCells) \
      or ('B1' in self.cpuChosenCells and 'C1' in self.cpuChosenCells) \
      or ('B2' in self.cpuChosenCells and 'C3' in self.cpuChosenCells)) \
      and 'A1' in self.availableCells:
      self.cpuChoice = 'A1'
    elif (('A1' in self.cpuChosenCells and 'A3' in self.cpuChosenCells) \
      or ('B2' in self.cpuChosenCells and 'C2' in self.cpuChosenCells)) \
      and 'A2' in self.availableCells:
      self.cpuChoice = 'A2'
    elif (('A1' in self.cpuChosenCells and 'A2' in self.cpuChosenCells) \
      or ('B3' in self.cpuChosenCells and 'C3' in self.cpuChosenCells) \
      or ('C1' in self.cpuChosenCells and 'B2' in self.cpuChosenCells)) \
      and 'A3' in self.availableCells:
      self.cpuChoice = 'A3'
    # B block
    elif (('B2' in self.cpuChosenCells and 'B3' in self.cpuChosenCells) \
      or ('A1' in self.cpuChosenCells and 'C1' in self.cpuChosenCells)) \
      and 'B1' in self.availableCells:
      self.cpuChoice = 'B1'
    elif (('B1' in self.cpuChosenCells and 'B3' in self.cpuChosenCells) \
      or ('A2' in self.cpuChosenCells and 'C2' in self.cpuChosenCells) \
      or ('A1' in self.cpuChosenCells and 'C3' in self.cpuChosenCells)) \
      and 'B2' in self.availableCells:
      self.cpuChoice = 'B2'
    elif (('B1' in self.cpuChosenCells and 'B2' in self.cpuChosenCells) \
      or ('A3' in self.cpuChosenCells and 'C3' in self.cpuChosenCells)) \
      and 'B3' in self.availableCells:
      self.cpuChoice = 'B3'
    # C block
    elif (('C2' in self.cpuChosenCells and 'C3' in self.cpuChosenCells) \
      or ('A1' in self.cpuChosenCells and 'B1' in self.cpuChosenCells) \
      or ('B2' in self.cpuChosenCells and 'A3' in self.cpuChosenCells)) \
      and 'C1' in self.availableCells:
      self.cpuChoice = 'C1'
    elif (('C1' in self.cpuChosenCells and 'C3' in self.cpuChosenCells) \
      or ('A2' in self.cpuChosenCells and 'B2' in self.cpuChosenCells)) \
      and 'C2' in self.availableCells:
      self.cpuChoice = 'C2'
    elif (('C1' in self.cpuChosenCells and 'C2' in self.cpuChosenCells) \
      or ('B3' in self.cpuChosenCells and 'C3' in self.cpuChosenCells) \
      or ('C1' in self.cpuChosenCells and 'B2' in self.cpuChosenCells)) \
      and 'C3' in self.availableCells:
      self.cpuChoice = 'C3'

    # Take smart starts
    elif len(self.userChosenCells) == 1 and 'B2' in self.userChosenCells:
      self.cpuChoice = choice(['A1', 'A3', 'C1', 'C3'])
    elif len(self.userChosenCells) == 1 and self.userChosenCells[0] in ['A2', 'B1', 'B3', 'C2']:
      self.cpuChoice = 'B2'

    # If no winning moves for user or cpu, choose at random
    else:
      # First make sure it's not a tie
      if len(self.availableCells) != 0:
        self.cpuChoice = choice(self.availableCells)
      # If it's a tie, end the game
      else:
        self.bottomLabel['text'] = 'Tie.'
        self.buttonsEnabled = False
        return

    # Set cell as chosen based on previous logic
    if self.cpuChoice == 'A1':
      self.btnA1['text'] = self.cpuIcon
    elif self.cpuChoice == 'A2':
      self.btnA2['text'] = self.cpuIcon
    elif self.cpuChoice == 'A3':
      self.btnA3['text'] = self.cpuIcon
    elif self.cpuChoice == 'B1':
      self.btnB1['text'] = self.cpuIcon
    elif self.cpuChoice == 'B2':
      self.btnB2['text'] = self.cpuIcon
    elif self.cpuChoice == 'B3':
      self.btnB3['text'] = self.cpuIcon
    elif self.cpuChoice == 'C1':
      self.btnC1['text'] = self.cpuIcon
    elif self.cpuChoice == 'C2':
      self.btnC2['text'] = self.cpuIcon
    elif self.cpuChoice == 'C3':
      self.btnC3['text'] = self.cpuIcon

    # Set cell as chosen, remove from available
    self.cpuChosenCells.append(self.cpuChoice)
    self.availableCells.remove(self.cpuChoice)

    # Check to see if computer has won
    if self.hasWon(self.cpuIcon):
      self.bottomLabel['text'] = 'Computer wins :('
      self.buttonsEnabled = False
    else:
      self.bottomLabel['text'] = 'Your turn.'

  # Set up function to check if user/cpu won
  def hasWon(self, icon):
    if (self.btnA1['text'] == icon and self.btnA2['text'] == icon and self.btnA3['text'] == icon) \
      or (self.btnB1['text'] == icon and self.btnB2['text'] == icon and self.btnB3['text'] == icon) \
      or (self.btnC1['text'] == icon and self.btnC2['text'] == icon and self.btnC3['text'] == icon) \
      or (self.btnA1['text'] == icon and self.btnB1['text'] == icon and self.btnC1['text'] == icon) \
      or (self.btnA2['text'] == icon and self.btnB2['text'] == icon and self.btnC2['text'] == icon) \
      or (self.btnA3['text'] == icon and self.btnB3['text'] == icon and self.btnC3['text'] == icon) \
      or (self.btnA1['text'] == icon and self.btnB2['text'] == icon and self.btnC3['text'] == icon) \
      or (self.btnC1['text'] == icon and self.btnB2['text'] == icon and self.btnA3['text'] == icon):
      return True
    else:
      return False

  # Set up function to reset game
  def resetGame(self):
    self.buttonsEnabled = True
    self.btnA1['text'] = ''
    self.btnA2['text'] = ''
    self.btnA3['text'] = ''
    self.btnB1['text'] = ''
    self.btnB2['text'] = ''
    self.btnB3['text'] = ''
    self.btnC1['text'] = ''
    self.btnC2['text'] = ''
    self.btnC3['text'] = ''
    self.bottomLabel['text'] = 'New game. Your turn.'
    self.userChosenCells.clear()
    self.cpuChosenCells.clear()
    self.availableCells.clear()
    self.availableCells = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

# Initialise GUI
root = tk.Tk()
gui = TicTacToe(root)
root.mainloop()