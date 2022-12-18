from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/move', methods=['POST'])
def move():
  global current_player
  row = int(request.form['row'])
  col = int(request.form['col'])
  make_move(current_player, row, col)
  if has_won(current_player):
    return 'win'
  current_player = 'O' if current_player == 'X' else 'X'
  return 'ok'


board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board():
  print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} ')
  print('-----------')
  print(f' {board[1][0]} | {board[1][1]} | {board[1][2]} ')
  print('-----------')
  print(f' {board[2][0]} | {board[2][1]} | {board[2][2]} ')


def make_move(player, row, col):
  if row < 0 or row > 2 or col < 0 or col > 2:
    print('Invalid move')
    return
  if board[row][col] != ' ':
    print('That space is already occupied')
    return
  board[row][col] = player

def has_won(player):
  # check rows
  for row in range(3):
    if board[row][0] == player and board[row][1] == player and board[row][2] == player:
      return True
  # check columns
  for col in range(3):
    if board[0][col] == player and board[1][col] == player and board[2][col] == player:
      return True
  # check diagonals
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  return False

current_player = 'X'

@app.route('/')
def tic_tac_toe():
  return render_template('tic_tac_toe.html')

@app.route('/move', methods=['POST'])
def move():
  row = int(request.form['row'])
  col = int(request.form['col'])
  make_move(current_player, row, col)
  if has_won(current_player):
    return 'win'
  global current_player
  current_player = 'O' if current_player == 'X' else 'X'
  return 'ok'

if __name__ == '__main__':
  app.run()
