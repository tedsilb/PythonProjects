# A Tic Tac Toe program. Uses tkinter for GUI.

# Import dependencies
import tkinter as tk

# Not sure what I'm doing yet, learning tkinter
class TicTacToe:
  def __init__(self, master):
    self.master = master
    master.title("Tic Tac Toe")

    # Set up first row
    self.btnA1 = tk.Button(master, text = 'Cell A1', command = self.select)
    self.btnA1.grid(row = 1, column = 1)
    self.btnA2 = tk.Button(master, text = 'Cell A2', command = self.select)
    self.btnA2.grid(row = 1, column = 2)
    self.btnA3 = tk.Button(master, text = 'Cell A3', command = self.select)
    self.btnA3.grid(row = 1, column = 3)

    # Set up second row
    self.btnB1 = tk.Button(master, text = 'Cell B1', command = self.select)
    self.btnB1.grid(row = 2, column = 1)
    self.btnB2 = tk.Button(master, text = 'Cell B2', command = self.select)
    self.btnB2.grid(row = 2, column = 2)
    self.btnB3 = tk.Button(master, text = 'Cell B3', command = self.select)
    self.btnB3.grid(row = 2, column = 3)

    # Set up third row
    self.btnC1 = tk.Button(master, text = 'Cell C1', command = self.select)
    self.btnC1.grid(row = 3, column = 1)
    self.btnC2 = tk.Button(master, text = 'Cell C2', command = self.select)
    self.btnC2.grid(row = 3, column = 2)
    self.btnC3 = tk.Button(master, text = 'Cell C3', command = self.select)
    self.btnC3.grid(row = 3, column = 3)

    # Set up bottom label
    self.bottomLabel = tk.Label(master, text = 'This is the label')
    self.bottomLabel.grid(row = 4, columnspan = 3, rowspan = 2, sticky = tk.W + tk.E)

  def select(self):
    print('select placeholder')

root = tk.Tk()
gui = TicTacToe(root)
root.mainloop()