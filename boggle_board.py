import string
import random

class BoggleBoard:
  '''FOR RANDOM LETTER IN ALPHABET:
  @staticmethod
  def letter_generator():
    letter = random.choice(string.ascii_uppercase)
    return letter
  '''
  #FOR DICE SELECTED LETTERS
  @staticmethod
  def letter_generator():
    letter = random.choice(BoggleBoard.roll_dice())
    return letter

  @staticmethod
  def roll_dice():
    dice = []
    for i, die in enumerate(BoggleBoard.boggle_dice):
      dice.append(die[random.randint(0,5)])
    return dice  

#ChatGBT generated list of lists containing all boggle dice
  boggle_dice = [
      ['A', 'A', 'E', 'E', 'G', 'N'],
      ['A', 'B', 'B', 'J', 'O', 'O'],
      ['A', 'C', 'H', 'O', 'P', 'S'],
      ['A', 'F', 'F', 'K', 'P', 'S'],
      ['A', 'O', 'O', 'T', 'T', 'W'],
      ['C', 'I', 'M', 'O', 'T', 'U'],
      ['D', 'E', 'I', 'L', 'R', 'X'],
      ['D', 'E', 'L', 'R', 'V', 'Y'],
      ['D', 'I', 'S', 'T', 'T', 'Y'],
      ['E', 'E', 'G', 'H', 'N', 'W'],
      ['E', 'E', 'I', 'N', 'S', 'U'],
      ['E', 'H', 'R', 'T', 'V', 'W'],
      ['E', 'I', 'O', 'S', 'S', 'T'],
      ['E', 'L', 'R', 'T', 'T', 'Y'],
      ['H', 'I', 'M', 'N', 'U', 'Qu'],
      ['H', 'L', 'N', 'N', 'R', 'Z']
  ]

  starting_board = [['-','-','-','-'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-'],]

  def __init__(self):
    self._board = BoggleBoard.starting_board

  def shake(self):
    self._board = BoggleBoard.starting_board
    
    for i, arr in enumerate(self._board):
      for j, val in enumerate(arr):
        self._board[i][j] = BoggleBoard.letter_generator()
        
    print(self._board)

game = BoggleBoard()
game.shake()
