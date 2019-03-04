# A Tic Tac Toe program. Uses tkinter for GUI. This is my first program ever to use a GUI
# By Ted Silbernagel
#TODO: Check to see if the computer won. Cascade logic from cell A1 to the rest.

# Import dependencies
import tkinter as tk
import tkinter.font as font
from time import sleep
from random import choice

# Not sure what I'm doing yet, learning tkinter
class TicTacToe:
  def __init__(self, master):
    # Set up core
    self.master = master
    master.title("Tic Tac Toe")

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
    self.bottomButton = tk.Button(master, text = 'Reset Game', command = self.resetGame2)
    self.bottomButton.grid(row = 4, column = 3)

  # Set up button handlers
  def callA1(self):
    if self.btnA1['text'] == '':
      self.btnA1['text'] = 'X'
      try:
        self.availableCells.remove('A1')
      except ValueError:
        pass
      if (self.btnA1['text'] == 'X' and self.btnA2['text'] == 'X' and self.btnA3['text'] == 'X') \
        or (self.btnB1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnB3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnC2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB1['text'] == 'X' and self.btnC1['text'] == 'X') \
        or (self.btnA2['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC2['text'] == 'X') \
        or (self.btnA3['text'] == 'X' and self.btnB3['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnA3['text'] == 'X'):
        self.bottomLabel['text'] = 'You win!'
      else:
        self.bottomLabel['text'] = 'Computer\'s turn...'
        sleep(1)
        cpuChoice = choice(self.availableCells)
        print(cpuChoice)
        if cpuChoice == 'A1':
          self.btnA1['text'] = 'O'
          self.cpuChosenCells.append('A1')
        elif cpuChoice == 'A2':
          self.btnA2['text'] = 'O'
          self.cpuChosenCells.append('A2')
        elif cpuChoice == 'A3':
          self.btnA3['text'] = 'O'
          self.cpuChosenCells.append('A3')
        elif cpuChoice == 'B1':
          self.btnB1['text'] = 'O'
          self.cpuChosenCells.append('B1')
        elif cpuChoice == 'B2':
          self.btnB2['text'] = 'O'
          self.cpuChosenCells.append('B2')
        elif cpuChoice == 'B3':
          self.btnB3['text'] = 'O'
          self.cpuChosenCells.append('B3')
        elif cpuChoice == 'C1':
          self.btnC1['text'] = 'O'
          self.cpuChosenCells.append('C1')
        elif cpuChoice == 'C2':
          self.btnC2['text'] = 'O'
          self.cpuChosenCells.append('C2')
        elif cpuChoice == 'C3':
          self.btnC3['text'] = 'O'
          self.cpuChosenCells.append('C3')
        self.bottomLabel['text'] = 'Your turn.'
    else:
      self.bottomLabel['text'] = 'Spot already selected. Try again'
  def callA2(self):
    if self.btnA2['text'] == '':
      self.btnA2['text'] = 'X'
      if (self.btnA1['text'] == 'X' and self.btnA2['text'] == 'X' and self.btnA3['text'] == 'X') \
        or (self.btnB1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnB3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnC2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB1['text'] == 'X' and self.btnC1['text'] == 'X') \
        or (self.btnA2['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC2['text'] == 'X') \
        or (self.btnA3['text'] == 'X' and self.btnB3['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnA3['text'] == 'X'):
        self.bottomLabel['text'] = 'You win!'
    else:
      self.bottomLabel['text'] = 'Spot already selected. Try again'
  def callA3(self):
    if self.btnA3['text'] == '':
      self.btnA3['text'] = 'X'
      if (self.btnA1['text'] == 'X' and self.btnA2['text'] == 'X' and self.btnA3['text'] == 'X') \
        or (self.btnB1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnB3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnC2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB1['text'] == 'X' and self.btnC1['text'] == 'X') \
        or (self.btnA2['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC2['text'] == 'X') \
        or (self.btnA3['text'] == 'X' and self.btnB3['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnA3['text'] == 'X'):
        self.bottomLabel['text'] = 'You win!'
    else:
      self.bottomLabel['text'] = 'That spot\'s already selected. Try again'
  def callB1(self):
    if self.btnB1['text'] == '':
      self.btnB1['text'] = 'X'
      if (self.btnA1['text'] == 'X' and self.btnA2['text'] == 'X' and self.btnA3['text'] == 'X') \
        or (self.btnB1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnB3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnC2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB1['text'] == 'X' and self.btnC1['text'] == 'X') \
        or (self.btnA2['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC2['text'] == 'X') \
        or (self.btnA3['text'] == 'X' and self.btnB3['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnA3['text'] == 'X'):
        self.bottomLabel['text'] = 'You win!'
    else:
      self.bottomLabel['text'] = 'That spot\'s already selected. Try again'
  def callB2(self):
    if self.btnB2['text'] == '':
      self.btnB2['text'] = 'X'
      if (self.btnA1['text'] == 'X' and self.btnA2['text'] == 'X' and self.btnA3['text'] == 'X') \
        or (self.btnB1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnB3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnC2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB1['text'] == 'X' and self.btnC1['text'] == 'X') \
        or (self.btnA2['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC2['text'] == 'X') \
        or (self.btnA3['text'] == 'X' and self.btnB3['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnA3['text'] == 'X'):
        self.bottomLabel['text'] = 'You win!'
    else:
      self.bottomLabel['text'] = 'That spot\'s already selected. Try again'
  def callB3(self):
    if self.btnB3['text'] == '':
      self.btnB3['text'] = 'X'
      if (self.btnA1['text'] == 'X' and self.btnA2['text'] == 'X' and self.btnA3['text'] == 'X') \
        or (self.btnB1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnB3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnC2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB1['text'] == 'X' and self.btnC1['text'] == 'X') \
        or (self.btnA2['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC2['text'] == 'X') \
        or (self.btnA3['text'] == 'X' and self.btnB3['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnA3['text'] == 'X'):
        self.bottomLabel['text'] = 'You win!'
    else:
      self.bottomLabel['text'] = 'That spot\'s already selected. Try again'
  def callC1(self):
    if self.btnC1['text'] == '':
      self.btnC1['text'] = 'X'
      if (self.btnA1['text'] == 'X' and self.btnA2['text'] == 'X' and self.btnA3['text'] == 'X') \
        or (self.btnB1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnB3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnC2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB1['text'] == 'X' and self.btnC1['text'] == 'X') \
        or (self.btnA2['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC2['text'] == 'X') \
        or (self.btnA3['text'] == 'X' and self.btnB3['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnA3['text'] == 'X'):
        self.bottomLabel['text'] = 'You win!'
    else:
      self.bottomLabel['text'] = 'That spot\'s already selected. Try again'
  def callC2(self):
    if self.btnC2['text'] == '':
      self.btnC2['text'] = 'X'
      if (self.btnA1['text'] == 'X' and self.btnA2['text'] == 'X' and self.btnA3['text'] == 'X') \
        or (self.btnB1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnB3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnC2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB1['text'] == 'X' and self.btnC1['text'] == 'X') \
        or (self.btnA2['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC2['text'] == 'X') \
        or (self.btnA3['text'] == 'X' and self.btnB3['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnA3['text'] == 'X'):
        self.bottomLabel['text'] = 'You win!'
    else:
      self.bottomLabel['text'] = 'That spot\'s already selected. Try again'
  def callC3(self):
    if self.btnC3['text'] == '':
      self.btnC3['text'] = 'X'
      if (self.btnA1['text'] == 'X' and self.btnA2['text'] == 'X' and self.btnA3['text'] == 'X') \
        or (self.btnB1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnB3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnC2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB1['text'] == 'X' and self.btnC1['text'] == 'X') \
        or (self.btnA2['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC2['text'] == 'X') \
        or (self.btnA3['text'] == 'X' and self.btnB3['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnA1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnC3['text'] == 'X') \
        or (self.btnC1['text'] == 'X' and self.btnB2['text'] == 'X' and self.btnA3['text'] == 'X'):
        self.bottomLabel['text'] = 'You win!'
    else:
      self.bottomLabel['text'] = 'That spot\'s already selected. Try again'

  # Set up function to reset game
  def resetGame2(self):
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