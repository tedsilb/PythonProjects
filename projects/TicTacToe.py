# A Tic Tac Toe program. Uses tkinter for GUI. This is my first program ever to use a GUI
# By Ted Silbernagel

# Import dependencies
import tkinter as tk
import tkinter.font as font
from time import sleep
from random import choice

# Set up class for GUI
class TicTacToe:
  def __init__(self, master):
    # Set up core
    self.master = master
    master.title("Tic Tac Toe")
    self.buttonsEnabled = True

    # Set up list for cpu to select from
    self.availableCells = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    self.cpuChosenCells = []

    # Set up first row
    self.btnA1 = tk.Button(master, text = '', height = 1, width = 2, command = self.callA1)
    self.btnA1.grid(row = 1, column = 1)
    self.btnA1['font'] = ('Helvetica', 90)
    self.btnA2 = tk.Button(master, text = '', height = 1, width = 2, command = self.callA2)
    self.btnA2.grid(row = 1, column = 2)
    self.btnA2['font'] = ('Helvetica', 90)
    self.btnA3 = tk.Button(master, text = '', height = 1, width = 2, command = self.callA3)
    self.btnA3.grid(row = 1, column = 3)
    self.btnA3['font'] = ('Helvetica', 90)

    # Set up second row
    self.btnB1 = tk.Button(master, text = '', height = 1, width = 2, command = self.callB1)
    self.btnB1.grid(row = 2, column = 1)
    self.btnB1['font'] = ('Helvetica', 90)
    self.btnB2 = tk.Button(master, text = '', height = 1, width = 2, command = self.callB2)
    self.btnB2.grid(row = 2, column = 2)
    self.btnB2['font'] = ('Helvetica', 90)
    self.btnB3 = tk.Button(master, text = '', height = 1, width = 2, command = self.callB3)
    self.btnB3.grid(row = 2, column = 3)
    self.btnB3['font'] = ('Helvetica', 90)

    # Set up third row
    self.btnC1 = tk.Button(master, text = '', height = 1, width = 2, command = self.callC1)
    self.btnC1.grid(row = 3, column = 1)
    self.btnC1['font'] = ('Helvetica', 90)
    self.btnC2 = tk.Button(master, text = '', height = 1, width = 2, command = self.callC2)
    self.btnC2.grid(row = 3, column = 2)
    self.btnC2['font'] = ('Helvetica', 90)
    self.btnC3 = tk.Button(master, text = '', height = 1, width = 2, command = self.callC3)
    self.btnC3.grid(row = 3, column = 3)
    self.btnC3['font'] = ('Helvetica', 90)

    # Set up bottom label
    self.bottomLabel = tk.Label(master, text = 'New game. Your turn.')
    self.bottomLabel.grid(row = 4, column = 1, columnspan = 2, rowspan = 2, sticky = tk.W + tk.E)
    self.bottomButton = tk.Button(master, text = 'Reset Game', command = self.resetGame)
    self.bottomButton.grid(row = 4, column = 3)

  # Set up button handlers
  def callA1(self):
    # Ensure buttons are enabled
    if self.buttonsEnabled == True:
      # Ensure cell isn't yet selected
      if self.btnA1['text'] == '':
        # Set the cell as checked
        self.btnA1['text'] = 'X'
        self.availableCells.remove('A1')
        # Check to see if you won
        if self.hasWon('X'):
          self.bottomLabel['text'] = 'You win!'
          self.buttonsEnabled = False
        # If you didn't win, take computer's turn
        else:
          self.takeCpuTurn()

      # If cell's selected, display error
      else:
        self.bottomLabel['text'] = 'Spot already selected. Try again'
  def callA2(self):
    # Ensure buttons are enabled
    if self.buttonsEnabled == True:
      # Ensure cell isn't yet selected
      if self.btnA2['text'] == '':
        # Set the cell as checked
        self.btnA2['text'] = 'X'
        self.availableCells.remove('A2')
        # Check to see if you won
        if self.hasWon('X'):
          self.bottomLabel['text'] = 'You win!'
          self.buttonsEnabled = False
        # If you didn't win, take computer's turn
        else:
          self.takeCpuTurn()

      # If cell's selected, display error
      else:
        self.bottomLabel['text'] = 'Spot already selected. Try again'
  def callA3(self):
    # Ensure buttons are enabled
    if self.buttonsEnabled == True:
      # Ensure cell isn't yet selected
      if self.btnA3['text'] == '':
        # Set the cell as checked
        self.btnA3['text'] = 'X'
        self.availableCells.remove('A3')
        # Check to see if you won
        if self.hasWon('X'):
          self.bottomLabel['text'] = 'You win!'
          self.buttonsEnabled = False
        # If you didn't win, take computer's turn
        else:
          self.takeCpuTurn()

      # If cell's selected, display error
      else:
        self.bottomLabel['text'] = 'Spot already selected. Try again'
  def callB1(self):
    # Ensure buttons are enabled
    if self.buttonsEnabled == True:
      # Ensure cell isn't yet selected
      if self.btnB1['text'] == '':
        # Set the cell as checked
        self.btnB1['text'] = 'X'
        self.availableCells.remove('B1')
        # Check to see if you won
        if self.hasWon('X'):
          self.bottomLabel['text'] = 'You win!'
          self.buttonsEnabled = False
        # If you didn't win, take computer's turn
        else:
          self.takeCpuTurn()

      # If cell's selected, display error
      else:
        self.bottomLabel['text'] = 'Spot already selected. Try again'
  def callB2(self):
    # Ensure buttons are enabled
    if self.buttonsEnabled == True:
      # Ensure cell isn't yet selected
      if self.btnB2['text'] == '':
        # Set the cell as checked
        self.btnB2['text'] = 'X'
        self.availableCells.remove('B2')
        # Check to see if you won
        if self.hasWon('X'):
          self.bottomLabel['text'] = 'You win!'
          self.buttonsEnabled = False
        # If you didn't win, take computer's turn
        else:
          self.takeCpuTurn()

      # If cell's selected, display error
      else:
        self.bottomLabel['text'] = 'Spot already selected. Try again'
  def callB3(self):
    # Ensure buttons are enabled
    if self.buttonsEnabled == True:
      # Ensure cell isn't yet selected
      if self.btnB3['text'] == '':
        # Set the cell as checked
        self.btnB3['text'] = 'X'
        self.availableCells.remove('B3')
        # Check to see if you won
        if self.hasWon('X'):
          self.bottomLabel['text'] = 'You win!'
          self.buttonsEnabled = False
        # If you didn't win, take computer's turn
        else:
          self.takeCpuTurn()

      # If cell's selected, display error
      else:
        self.bottomLabel['text'] = 'Spot already selected. Try again'
  def callC1(self):
    # Ensure buttons are enabled
    if self.buttonsEnabled == True:
      # Ensure cell isn't yet selected
      if self.btnC1['text'] == '':
        # Set the cell as checked
        self.btnC1['text'] = 'X'
        self.availableCells.remove('C1')
        # Check to see if you won
        if self.hasWon('X'):
          self.bottomLabel['text'] = 'You win!'
          self.buttonsEnabled = False
        # If you didn't win, take computer's turn
        else:
          self.takeCpuTurn()

      # If cell's selected, display error
      else:
        self.bottomLabel['text'] = 'Spot already selected. Try again'

  def callC2(self):
    # Ensure buttons are enabled
    if self.buttonsEnabled == True:
      # Ensure cell isn't yet selected
      if self.btnC2['text'] == '':
        # Set the cell as checked, remove from available
        self.btnC2['text'] = 'X'
        self.availableCells.remove('C2')
        # Check to see if you won
        if self.hasWon('X'):
          self.bottomLabel['text'] = 'You win!'
          self.buttonsEnabled = False
        # If you didn't win, take computer's turn
        else:
          self.takeCpuTurn()

      # If cell's selected, display error
      else:
        self.bottomLabel['text'] = 'Spot already selected. Try again'

  def callC3(self):
    # Ensure buttons are enabled
    if self.buttonsEnabled == True:
      # Ensure cell isn't yet selected
      if self.btnC3['text'] == '':
        # Set the cell as checked, remove from available
        self.btnC3['text'] = 'X'
        self.availableCells.remove('C3')
        # Check to see if you won
        if self.hasWon('X'):
          self.bottomLabel['text'] = 'You win!'
          self.buttonsEnabled = False
        # If you didn't win, take computer's turn
        else:
          self.takeCpuTurn()

      # If cell's selected, display error
      else:
        self.bottomLabel['text'] = 'Spot already selected. Try again'

  # Set up function to take CPU turn
  def takeCpuTurn(self):
    self.bottomLabel['text'] = 'Computer\'s turn...'
    # Ensure winning moves
    # A block
    if (('A2' in self.cpuChosenCells and 'A3' in self.cpuChosenCells) \
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
    elif (('C2' in self.cpuChosenCells and 'A3' in self.cpuChosenCells) \
      or ('A1' in self.cpuChosenCells and 'B1' in self.cpuChosenCells) \
      or ('B2' in self.cpuChosenCells and 'A3' in self.cpuChosenCells)) \
      and 'C1' in self.availableCells:
      self.cpuChoice = 'C1'
    elif (('C1' in self.cpuChosenCells and 'C3' in self.cpuChosenCells) \
      or ('A2' in self.cpuChosenCells and 'B2' in self.cpuChosenCells)) \
      and 'C2' in self.availableCells:
      self.cpuChoice = 'C2'
    elif (('A1' in self.cpuChosenCells and 'A2' in self.cpuChosenCells) \
      or ('B3' in self.cpuChosenCells and 'C3' in self.cpuChosenCells) \
      or ('C1' in self.cpuChosenCells and 'B2' in self.cpuChosenCells)) \
      and 'C3' in self.availableCells:
      self.cpuChoice = 'C3'
    else:
      self.cpuChoice = choice(self.availableCells)
    
    # Set cell as chosen based on logic
    if self.cpuChoice == 'A1':
      self.btnA1['text'] = 'O'
      self.cpuChosenCells.append('A1')
    elif self.cpuChoice == 'A2':
      self.btnA2['text'] = 'O'
      self.cpuChosenCells.append('A2')
    elif self.cpuChoice == 'A3':
      self.btnA3['text'] = 'O'
      self.cpuChosenCells.append('A3')
    elif self.cpuChoice == 'B1':
      self.btnB1['text'] = 'O'
      self.cpuChosenCells.append('B1')
    elif self.cpuChoice == 'B2':
      self.btnB2['text'] = 'O'
      self.cpuChosenCells.append('B2')
    elif self.cpuChoice == 'B3':
      self.btnB3['text'] = 'O'
      self.cpuChosenCells.append('B3')
    elif self.cpuChoice == 'C1':
      self.btnC1['text'] = 'O'
      self.cpuChosenCells.append('C1')
    elif self.cpuChoice == 'C2':
      self.btnC2['text'] = 'O'
      self.cpuChosenCells.append('C2')
    elif self.cpuChoice == 'C3':
      self.btnC3['text'] = 'O'
      self.cpuChosenCells.append('C3')
    
    # Remove chosen cells from available
    self.availableCells.remove(self.cpuChoice)
    
    # Check to see if computer has won
    if self.hasWon('O'):
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
    self.cpuChosenCells.clear()
    self.availableCells.clear()
    self.availableCells = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
  
# Initialise GUI
root = tk.Tk()
gui = TicTacToe(root)
root.mainloop()