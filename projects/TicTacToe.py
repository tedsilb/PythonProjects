"""A Tic Tac Toe program.
Uses tkinter for GUI.
By Ted Silbernagel
"""

from functools import partial
import random
import tkinter as tk


class TicTacToe:
  """Class for the GUI."""

  def __init__(self, master):
    # Set up core
    self.master = master
    master.title('Tic Tac Toe')

    # Constants
    self.user_icon = 'X'
    self.cpu_icon = 'O'
    self.cpu_win_msg = 'Computer wins :('
    self.user_win_msg = 'You win!'
    self.tie_msg = 'Tie.'
    self.new_game_msg = 'New game. Your turn.'
    self.already_selected_msg = 'Spot already selected. Try again.'
    self.cpu_turn_msg = 'Computer\'s turn...'
    self.user_turn_msg = 'Your turn.'
    self.reset_game_txt = 'Reset Game'
    self.button_font = ('Helvetica', 90)
    self.bottom_label_font = ('Helvetica', 12, 'bold')
    self.button_height = 1
    self.button_width = 2

    # Base variables
    self.available_cells = []
    self.user_chosen_cells = []
    self.cpu_chosen_cells = []
    self.cpu_choice = ''
    self.cpu_started = False
    self.buttons_enabled = True

    # Define buttons
    self.btn_a1 = tk.Button(master,
                            font=self.button_font,
                            height=self.button_height,
                            width=self.button_width)
    self.btn_a2 = tk.Button(master,
                            font=self.button_font,
                            height=self.button_height,
                            width=self.button_width)
    self.btn_a3 = tk.Button(master,
                            font=self.button_font,
                            height=self.button_height,
                            width=self.button_width)
    self.btn_b1 = tk.Button(master,
                            font=self.button_font,
                            height=self.button_height,
                            width=self.button_width)
    self.btn_b2 = tk.Button(master,
                            font=self.button_font,
                            height=self.button_height,
                            width=self.button_width)
    self.btn_b3 = tk.Button(master,
                            font=self.button_font,
                            height=self.button_height,
                            width=self.button_width)
    self.btn_c1 = tk.Button(master,
                            font=self.button_font,
                            height=self.button_height,
                            width=self.button_width)
    self.btn_c2 = tk.Button(master,
                            font=self.button_font,
                            height=self.button_height,
                            width=self.button_width)
    self.btn_c3 = tk.Button(master,
                            font=self.button_font,
                            height=self.button_height,
                            width=self.button_width)

    # Set grid locations
    self.btn_a1.grid(row=1, column=1)
    self.btn_a2.grid(row=1, column=2)
    self.btn_a3.grid(row=1, column=3)
    self.btn_b1.grid(row=2, column=1)
    self.btn_b2.grid(row=2, column=2)
    self.btn_b3.grid(row=2, column=3)
    self.btn_c1.grid(row=3, column=1)
    self.btn_c2.grid(row=3, column=2)
    self.btn_c3.grid(row=3, column=3)

    # Define button commands
    self.btn_a1['command'] = partial(self.button_press, self.btn_a1, 'A1')
    self.btn_a2['command'] = partial(self.button_press, self.btn_a2, 'A2')
    self.btn_a3['command'] = partial(self.button_press, self.btn_a3, 'A3')
    self.btn_b1['command'] = partial(self.button_press, self.btn_b1, 'B1')
    self.btn_b2['command'] = partial(self.button_press, self.btn_b2, 'B2')
    self.btn_b3['command'] = partial(self.button_press, self.btn_b3, 'B3')
    self.btn_c1['command'] = partial(self.button_press, self.btn_c1, 'C1')
    self.btn_c2['command'] = partial(self.button_press, self.btn_c2, 'C2')
    self.btn_c3['command'] = partial(self.button_press, self.btn_c3, 'C3')

    # Set up bottom label
    self.bottom_label = tk.Label(master, font=self.bottom_label_font)
    self.bottom_label.grid(row=4,
                           column=1,
                           columnspan=2,
                           rowspan=2,
                           sticky=(tk.N + tk.S + tk.W + tk.E))

    # Set up reset game button
    self.bottom_button = tk.Button(master,
                                   text=self.reset_game_txt,
                                   command=self.reset_game)
    self.bottom_button.grid(row=4, column=3, columnspan=2, pady=(15, 15))

    # Reset game, initially
    self.reset_game()

  def button_press(self, button: tk.Button, grid_loc: str) -> None:
    """Handle button presses."""
    # Ensure that buttons are enabled
    if self.buttons_enabled:
      # Ensure the cell isn't yet selected
      if not button['text']:
        # Set the cell as checked and chosen, remove from available
        button['text'] = self.user_icon
        # Set cell as chosen, remove from available
        self.user_chosen_cells.append(grid_loc)
        self.available_cells.remove(grid_loc)
        # Check to see if you won
        if self.has_won(self.user_icon):
          self.bottom_label['text'] = self.user_win_msg
          self.buttons_enabled = False
        # If you didn't win, take the computer's turn
        else:
          self.take_cpu_turn()

      # If cell's selected, display error
      else:
        self.bottom_label['text'] = self.already_selected_msg

  def take_cpu_turn(self) -> None:
    """Take CPU turn."""
    self.bottom_label['text'] = self.cpu_turn_msg
    # Some winning strategies
    if self.cpu_started:
      if (self.cpu_chosen_cells == ['A1', 'A3'] and
          len(self.user_chosen_cells) == 2):
        if self.user_chosen_cells in [['B1', 'A2'], ['C1', 'A2']]:
          self.cpu_choice = 'C3'
        elif self.user_chosen_cells == ['B3', 'A2']:
          self.cpu_choice = 'C1'
        elif self.user_chosen_cells == ['A2', 'C2']:
          self.cpu_choice = 'B2'
      elif (self.user_chosen_cells == ['B2', 'C3'] and
            self.cpu_chosen_cells == ['A1', 'C1']):
        self.cpu_choice = 'A3'

    # Block winning moves by user
    # A block
    elif (
        (('A2' in self.user_chosen_cells and 'A3' in self.user_chosen_cells) or
         ('B1' in self.user_chosen_cells and 'C1' in self.user_chosen_cells) or
         ('B2' in self.user_chosen_cells and 'C3' in self.user_chosen_cells))
        and 'A1' in self.available_cells):
      self.cpu_choice = 'A1'
    elif (
        (('A1' in self.user_chosen_cells and 'A3' in self.user_chosen_cells) or
         ('B2' in self.user_chosen_cells and 'C2' in self.user_chosen_cells))
        and 'A2' in self.available_cells):
      self.cpu_choice = 'A2'
    elif (
        (('A1' in self.user_chosen_cells and 'A2' in self.user_chosen_cells) or
         ('B3' in self.user_chosen_cells and 'C3' in self.user_chosen_cells) or
         ('C1' in self.user_chosen_cells and 'B2' in self.user_chosen_cells))
        and 'A3' in self.available_cells):
      self.cpu_choice = 'A3'
    # B block
    elif (
        (('B2' in self.user_chosen_cells and 'B3' in self.user_chosen_cells) or
         ('A1' in self.user_chosen_cells and 'C1' in self.user_chosen_cells))
        and 'B1' in self.available_cells):
      self.cpu_choice = 'B1'
    elif (
        (('B1' in self.user_chosen_cells and 'B3' in self.user_chosen_cells) or
         ('A2' in self.user_chosen_cells and 'C2' in self.user_chosen_cells) or
         ('A1' in self.user_chosen_cells and 'C3' in self.user_chosen_cells))
        and 'B2' in self.available_cells):
      self.cpu_choice = 'B2'
    elif (
        (('B1' in self.user_chosen_cells and 'B2' in self.user_chosen_cells) or
         ('A3' in self.user_chosen_cells and 'C3' in self.user_chosen_cells))
        and 'B3' in self.available_cells):
      self.cpu_choice = 'B3'
    # C block
    elif (
        (('C2' in self.user_chosen_cells and 'C3' in self.user_chosen_cells) or
         ('A1' in self.user_chosen_cells and 'B1' in self.user_chosen_cells) or
         ('B2' in self.user_chosen_cells and 'A3' in self.user_chosen_cells))
        and 'C1' in self.available_cells):
      self.cpu_choice = 'C1'
    elif (
        (('C1' in self.user_chosen_cells and 'C3' in self.user_chosen_cells) or
         ('A2' in self.user_chosen_cells and 'B2' in self.user_chosen_cells))
        and 'C2' in self.available_cells):
      self.cpu_choice = 'C2'
    elif (
        (('C1' in self.cpu_chosen_cells and 'C2' in self.user_chosen_cells) or
         ('B3' in self.user_chosen_cells and 'C3' in self.user_chosen_cells) or
         ('C1' in self.user_chosen_cells and 'B2' in self.user_chosen_cells))
        and 'C3' in self.available_cells):
      self.cpu_choice = 'C3'

    # Take winning moves for cpu
    # A block
    elif (
        (('A2' in self.cpu_chosen_cells and 'A3' in self.cpu_chosen_cells) or
         ('B1' in self.cpu_chosen_cells and 'C1' in self.cpu_chosen_cells) or
         ('B2' in self.cpu_chosen_cells and 'C3' in self.cpu_chosen_cells)) and
        'A1' in self.available_cells):
      self.cpu_choice = 'A1'
    elif (
        (('A1' in self.cpu_chosen_cells and 'A3' in self.cpu_chosen_cells) or
         ('B2' in self.cpu_chosen_cells and 'C2' in self.cpu_chosen_cells)) and
        'A2' in self.available_cells):
      self.cpu_choice = 'A2'
    elif (
        (('A1' in self.cpu_chosen_cells and 'A2' in self.cpu_chosen_cells) or
         ('B3' in self.cpu_chosen_cells and 'C3' in self.cpu_chosen_cells) or
         ('C1' in self.cpu_chosen_cells and 'B2' in self.cpu_chosen_cells)) and
        'A3' in self.available_cells):
      self.cpu_choice = 'A3'
    # B block
    elif (
        (('B2' in self.cpu_chosen_cells and 'B3' in self.cpu_chosen_cells) or
         ('A1' in self.cpu_chosen_cells and 'C1' in self.cpu_chosen_cells)) and
        'B1' in self.available_cells):
      self.cpu_choice = 'B1'
    elif (
        (('B1' in self.cpu_chosen_cells and 'B3' in self.cpu_chosen_cells) or
         ('A2' in self.cpu_chosen_cells and 'C2' in self.cpu_chosen_cells) or
         ('A1' in self.cpu_chosen_cells and 'C3' in self.cpu_chosen_cells)) and
        'B2' in self.available_cells):
      self.cpu_choice = 'B2'
    elif (
        (('B1' in self.cpu_chosen_cells and 'B2' in self.cpu_chosen_cells) or
         ('A3' in self.cpu_chosen_cells and 'C3' in self.cpu_chosen_cells)) and
        'B3' in self.available_cells):
      self.cpu_choice = 'B3'
    # C block
    elif (
        (('C2' in self.cpu_chosen_cells and 'C3' in self.cpu_chosen_cells) or
         ('A1' in self.cpu_chosen_cells and 'B1' in self.cpu_chosen_cells) or
         ('B2' in self.cpu_chosen_cells and 'A3' in self.cpu_chosen_cells)) and
        'C1' in self.available_cells):
      self.cpu_choice = 'C1'
    elif (
        (('C1' in self.cpu_chosen_cells and 'C3' in self.cpu_chosen_cells) or
         ('A2' in self.cpu_chosen_cells and 'B2' in self.cpu_chosen_cells)) and
        'C2' in self.available_cells):
      self.cpu_choice = 'C2'
    elif (
        (('C1' in self.cpu_chosen_cells and 'C2' in self.cpu_chosen_cells) or
         ('B3' in self.cpu_chosen_cells and 'C3' in self.cpu_chosen_cells) or
         ('A1' in self.cpu_chosen_cells and 'B2' in self.cpu_chosen_cells)) and
        'C3' in self.available_cells):
      self.cpu_choice = 'C3'

    # Take smart starts
    # User start
    elif len(self.user_chosen_cells) == 1 and not self.cpu_chosen_cells:
      if self.user_chosen_cells[0] == 'B2':
        self.cpu_choice = random.choice(['A1', 'A3', 'C1', 'C3'])
      else:
        self.cpu_choice = 'B2'
    # CPU start
    elif not self.user_chosen_cells:
      self.cpu_choice = random.choices(
          population=['A1', 'A3', 'C1', 'C3', 'B2', 'A2', 'B3', 'C2', 'B1'],
          weights=[.2, .2, .2, .2, .1, .025, .025, .025, .025],
          k=1)[0]

    # If no winning moves for user or cpu, choose at random
    else:
      # First make sure it's not a tie
      if self.available_cells:
        self.cpu_choice = random.choice(self.available_cells)
      # If it's a tie, end the game
      else:
        self.bottom_label['text'] = self.tie_msg
        self.buttons_enabled = False
        return

    # Set cell as chosen based on previous logic
    if self.cpu_choice == 'A1':
      self.btn_a1['text'] = self.cpu_icon
    elif self.cpu_choice == 'A2':
      self.btn_a2['text'] = self.cpu_icon
    elif self.cpu_choice == 'A3':
      self.btn_a3['text'] = self.cpu_icon
    elif self.cpu_choice == 'B1':
      self.btn_b1['text'] = self.cpu_icon
    elif self.cpu_choice == 'B2':
      self.btn_b2['text'] = self.cpu_icon
    elif self.cpu_choice == 'B3':
      self.btn_b3['text'] = self.cpu_icon
    elif self.cpu_choice == 'C1':
      self.btn_c1['text'] = self.cpu_icon
    elif self.cpu_choice == 'C2':
      self.btn_c2['text'] = self.cpu_icon
    elif self.cpu_choice == 'C3':
      self.btn_c3['text'] = self.cpu_icon

    # Set cell as chosen, remove from available
    self.cpu_chosen_cells.append(self.cpu_choice)
    self.available_cells.remove(self.cpu_choice)

    # Check to see if computer has won
    if self.has_won(self.cpu_icon):
      self.bottom_label['text'] = self.cpu_win_msg
      self.buttons_enabled = False
    else:
      self.bottom_label['text'] = self.user_turn_msg

    # Check for tie
    if (not self.available_cells and
        self.bottom_label['text'] not in [self.cpu_win_msg, self.user_win_msg]):
      self.bottom_label['text'] = self.tie_msg
      self.buttons_enabled = False

  def has_won(self, icon: str) -> bool:
    """Check if user/CPU won."""
    winning_scenarios = [
        [self.btn_a1['text'], self.btn_a2['text'], self.btn_a3['text']],
        [self.btn_b1['text'], self.btn_b2['text'], self.btn_b3['text']],
        [self.btn_c1['text'], self.btn_c2['text'], self.btn_c3['text']],
        [self.btn_a1['text'], self.btn_b1['text'], self.btn_c1['text']],
        [self.btn_a2['text'], self.btn_b2['text'], self.btn_c2['text']],
        [self.btn_a3['text'], self.btn_b3['text'], self.btn_c3['text']],
        [self.btn_a1['text'], self.btn_b2['text'], self.btn_c3['text']],
        [self.btn_c1['text'], self.btn_b2['text'], self.btn_a3['text']],
    ]

    return [icon, icon, icon] in winning_scenarios

  # Set up function to reset game
  def reset_game(self) -> None:
    self.buttons_enabled = True
    self.btn_a1['text'] = ''
    self.btn_a2['text'] = ''
    self.btn_a3['text'] = ''
    self.btn_b1['text'] = ''
    self.btn_b2['text'] = ''
    self.btn_b3['text'] = ''
    self.btn_c1['text'] = ''
    self.btn_c2['text'] = ''
    self.btn_c3['text'] = ''
    self.bottom_label['text'] = self.new_game_msg
    self.user_chosen_cells.clear()
    self.cpu_chosen_cells.clear()
    self.available_cells = [
        'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'
    ]
    # Randomly have cpu start game
    self.cpu_started = random.choice([True, False])
    if self.cpu_started:
      self.take_cpu_turn()


if __name__ == '__main__':
  root = tk.Tk()
  gui = TicTacToe(root)
  root.mainloop()
