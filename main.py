import random

import pygame
import os
import math


pygame.init()
Width, Height = 800, 500
win = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Hagman Game!")

#button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((Width - (RADIUS *2 + GAP)*13)/2)
starty = 400
A = 65
for i in range(26):
  x = startx + ((RADIUS*2 + GAP) * (i%13))
  y = starty + ((i//13) * (GAP + RADIUS * 2))
  letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONTS = pygame.font.SysFont('comicsans', 40)
WORD_FONTS = pygame.font.SysFont('comicsans', 60)
TITLE_FONTS = pygame.font.SysFont('comicsans', 70)
#load images
images = []
for i in range(7):
  image = pygame.image.load("hangman"+str(i)+".png")
  images.append(image)

#game variables
hangman_status = 0
words = ["DEVELOPER", "PREACHER", "WINNER", "STUDENT", "CARNIVORE"]
word = random.choice(words)
guessed = []

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
  win.fill(WHITE)
  text = TITLE_FONTS.render("HANGMAN GAME", 1, BLACK)
  win.blit(text, (Width/2 - text.get_width()/2, 20))

  # draw word
  display_word = ""
  for letter in word:
      if letter in guessed:
          display_word += letter + " "
      else:
          display_word += "_ "
      text = WORD_FONTS.render(display_word, 1, BLACK)
      win.blit(text, (400, 200))
  for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONTS.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
  win.blit(images[hangman_status], (50, 100))
  pygame.display.update()

def display(message):
    win.fill(WHITE)
    text = WORD_FONTS.render(message, 1, BLACK)
    win.blit(text, (Width / 2 - text.get_width() / 2, Height / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)

while run:
  if hangman_status == 7:
      mess = "YOU LOSE"
      display(mess)
      break
  won = True
  for letter in word:
      if letter not in guessed:
          won = False
          break

  if won:
      mess = "YOU WON!!"
      display(mess)
      break

  clock.tick(FPS)
  draw()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      mx, my = pygame.mouse.get_pos()
      for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            dis = math.sqrt((x - mx)**2 + (y - my)**2)
            if dis  <= RADIUS:
              letter[3] = False
              guessed.append(ltr)
              if ltr not in word:
                  hangman_status += 1



pygame.quit()
