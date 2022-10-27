print('Игра "Крестики-нолики"')

board = list(range(1,10))

def draw(board):
   print('-' * 13)
   for i in range(3):
      print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
      print('-' * 13)

def step(player):
   valid = False
   while not valid:
      player_step = input('Сделайте ход ' + player+'? ')
      try:
         player_step = int(player_step)
      except:
         print('Некорректный ввод. ')
         continue
      if player_step >= 1 and player_step <= 9:
         if(str(board[player_step-1]) not in "XO"):
            board[player_step-1] = player
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check(board):
   victory = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for e in victory:
       if board[e[0]] == board[e[1]] == board[e[2]]:
          return board[e[0]]
   return False

def game(board):
    counter = 0
    win = False
    while not win:
        draw(board)
        if counter % 2 == 0:
           step("X")
        else:
           step("O")
        counter += 1
        if counter > 4:
           tmp = check(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw(board)
game(board)

input("Игра окончена.")
import emoji
print(emoji.emojize('Python is :thumbs_up:'))
