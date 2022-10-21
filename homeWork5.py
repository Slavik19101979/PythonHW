Задача 1

import re

string = 'Мы неабв очень любим Питон иабв абв'
letter = 'абв'

words = re.sub(f'[\s\W]*(\w*{letter}\w*)[\s\W]*',' ', string)
print(words)

___________________________________________________
Задача 2
from random import randint

def dialog(total):
    while True:
        answer = input('Сколько конфет вы хотите взять? ')
        if not answer.isdigit():
            print('Нужно ввести число!')
            continue
        answer = int(answer)
        if not answer in range(1, 29):
            print('Вы можете взять от 1 до 28 конфет за ход. Попробуйте еще раз!')
            continue
        if answer > total:
            print(f'На столе осталось {total} конфет! Попробуйте еще раз!')
            continue
        total -= answer
        print(f'Осталось {total} конфет')
        return total
        break

def main(sweets, name1, name2):
  turn = 0
  while sweets !=0:
      sweets = dialog(sweets)
      turn += 1
  if turn % 2 == 0:
    print(f'{name2} победил! Все конфеты достаются ему!')
  else:
    print(f'{name1} победил! Все конфеты достаются ему!')

sweets = 2021
print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. \
\nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\
\nВсе конфеты оппонента достаются сделавшему последний ход. Начинаем игру!')
player1 = input('Как зовут первого игрока? ')
player2 = input('Как зовут второго игрока? ')
lottery = randint(1,2)
if lottery == 2:
  temp = player1
  player1 = player2
  player2 = temp
print(f'Жребий решил, что {player1} ходит первым')
main(sweets, player1, player2)

__________________________________________
Задача 2.2 Игра против бота

from random import randint

def bot(total, max):
  if total < max: max = total
  bot = randint(1, max)
  print(f'Sweet Bot взял {bot} конфет')
  total -= bot
  print(f'Осталось {total} конфет')
  return total

def user(total):
    while True:
        answer = input('Сколько конфет вы хотите взять? ')
        if not answer.isdigit():
            print('Нужно ввести число!')
            continue
        answer = int(answer)
        if not answer in range(1, 29):
            print('Вы можете взять от 1 до 28 конфет за ход. Попробуйте еще раз!')
            continue
        if answer > total:
            print(f'На столе осталось {total} конфет! Попробуйте еще раз!')
            continue
        total -= answer
        print(f'Осталось {total} конфет')
        return total
        break

def main(sweets, name1, name2, firstMove):
  turn = 0
  while sweets !=0:
    if firstMove == 'Sweet Bot':
      sweets = bot(sweets, 28); turn += 1
      sweets = user(sweets); turn += 1
    else:
      sweets = user(sweets); turn += 1
      sweets = bot(sweets, 28); turn +=1
  if turn % 2 == 0:
    print(f'{name2} победил! Все конфеты достаются ему!')
  else:
    print(f'{name1} победил! Все конфеты достаются ему!')

sweets = 2021
print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. \
\nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\
\nВсе конфеты оппонента достаются сделавшему последний ход. \nНачинаем игру!\n')

player1, player2 = input('Как вас зовут? '), 'Sweet Bot'
print(f'\n{player1} вы играете против {player2}')
lottery = randint(1,2)
if lottery == 2:
  temp = player1
  player1 = player2
  player2 = temp
print(f'Жребий решил, что {player1} ходит первым\n')

main(sweets, player1, player2, player1)

______________________________________________________
Задача 2.3 Наделение бота интелектом
from random import randint

def bot(total):
  bot = total % 29
  print(f'Sweet Bot взял {bot} конфет')
  total -= bot
  print(f'Осталось {total} конфет')
  return total

def user(total):
    while True:
        answer = input('Сколько конфет вы хотите взять? ')
        if not answer.isdigit():
            print('Нужно ввести число!')
            continue
        answer = int(answer)
        if not answer in range(1, 29):
            print('Вы можете взять от 1 до 28 конфет за ход. Попробуйте еще раз!')
            continue
        if answer > total:
            print(f'На столе осталось {total} конфет! Попробуйте еще раз!')
            continue
        total -= answer
        print(f'Осталось {total} конфет')
        return total
        break

def main(sweets, name1, name2):
  turn = 0
  while sweets !=0:
    if name1 == 'Super Smart Bot':
      sweets = bot(sweets); turn += 1
      sweets = user(sweets); turn += 1
    else:
      sweets = user(sweets); turn += 1
      sweets = bot(sweets); turn +=1
  if turn % 2 == 0:
    print(f'{name2} победил! Все конфеты достаются ему!')
  else:
    print(f'{name1} победил! Все конфеты достаются ему!')

sweets = 2021
print(f'На столе лежит {sweets} конфета. Играют два игрока делая ход друг после друга. \
\nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\
\nВсе конфеты оппонента достаются сделавшему последний ход. \nНачинаем игру!\n')

player1, player2 = input('Как вас зовут? '), 'Super Smart Bot'
print(f'\n{player1} вы играете против {player2}')
lottery = randint(1,2)
if lottery == 2:
  temp = player1
  player1 = player2
  player2 = temp
print(f'Жребий решил, что {player1} ходит первым\n')

main(sweets, player1, player2)

______________________________
Задача 3 Крестики-нолики

from tkinter import *
from tkinter import messagebox
import tkinter.font as font

window = Tk()
window.title("Крестики-нолики")

def chose_winner(mylist):
    winning_position = [[0,1,2], [3,4,5], [6,7,8],[0,3,6],\
                       [1,4,7], [2,5,8],[6,4,2], [0,4,8]]
    for position in winning_position:
        if mylist[position[0]] == mylist[position[1]] == mylist[position[2]]\
         and mylist[position[0]] in ('X0'):
            if mylist[position[0]] == 'X':
                messagebox.showinfo("Congrats!", 'Победили крестики!') 
                window.destroy()
            if mylist[position[0]] == '0':
                messagebox.showinfo("Congrats!", 'Победили нолики!') 
                window.destroy()
    if ' ' not in mylist:
        messagebox.showinfo("Congrats!", 'Ничья!') 
        window.destroy()

def push(board, cell):
    global turn
    if turn % 2 == 0:
        board[cell] = 'X'
        button[cell].config(text='X', state = 'disabled')
        turn += 1
    else:
        board[cell] = '0'
        button[cell].config(text='0', state = 'disabled')
        turn += 1
    if turn > 3:
        chose_winner(board)


mylist = [" "] * 9
turn = 0

myFont = font.Font(size = 42)
button = [Button( width = 2, height = 1, font = myFont, \
                 command = lambda x = i: push(mylist,x)) for i in range (9)]

row = 1; col = 0
for i in range(9):
    button[i].grid(row = row, column = col, sticky=W+E)
    col += 1
    if col == 3:
        row += 1; col = 0

label_1 = Label(height=3, text = 'Делайте ход')
label_1.grid(row = 4, column = 0, columnspan=3)

window.mainloop()


_____________________________________
Задача 4 RLE Алгоритм

import re

def compression(string):
  count = 1
  result = ''
  for i in range(0, len(string) - 1):
      if string[i] == string[i+1]:
          count += 1
      else: 
          result += str(count)+string[i]
          count = 1
  return (result + str(count)+string[-1])

def decompression(string):
  nums = re.findall(r'\d+', string)
  letters = re.findall(r'[A-Z]', string)
  return(''.join(list(map(lambda x, y: int(x)*y, nums, letters))))

with open('myFile', 'w') as f:
     f.write('RRUUUUUUUUUUXXXKHHHHHHMMMMMMGGGLLLLLLLJJJJ')


with open('myFile', 'r') as f, open('compressed', 'w+') as f2, open('decompressed', 'w+') as f3:
    compressed = compression(f.read())
    f2.write(compressed)
print(compressed)


with open('compressed', 'r') as f2, open('decompressed', 'w+') as f3:
    decompressed = decompression(f2.read())
    f3.write(decompressed)
print(decompressed)