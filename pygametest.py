import pygame
import sys
import random
import time
from pygame.locals import *

#Initialize Pygame
pygame.init()

#Set up the display
screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokemon Clone")

#Load the image sprite
#sprite_image = pygame.transform.scale(pygame.image.load("images/EagleSprite.jpg"),(100,100))
#sprite_rect = sprite_image.get_rect()
#sprite_speed = 5

#Set the initial position of the sprite
#sprite_rect.x = screen_width // 2 - sprite_rect.width // 2
#sprite_rect.y = screen_height // 2 - sprite_rect.height // 2


#do display image - need sprite and rectagnle/rect



class UI:
  def __init__(self, image, scale, type = "main", text = ["Fight", "Bag", "Run", ""])  :
    self.sprite = pygame.transform.scale(pygame.image.load("images/GUI/"+image),scale)
    self.image = image
    self.rect = self.sprite.get_rect()
    self.type = type
    self.text = text
    self.notif = ""
    self.notif2 = ''


  


  def displayUI(self):
    display_text(screen, self.notif, 500, 300, (0,0,0))
    display_text(screen, self.notif2, 500, 200, (0,0,0))
    display_text(screen, self.text[0], 250, 785, (0,0,0))
    display_text(screen, self.text[1], 750, 785, (0,0,0))
    display_text(screen, self.text[2], 250, 935, (0,0,0))
    display_text(screen, self.text[3], 750, 935, (0,0,0))
    

  def moveUI(self, image,x,y):
    self.sprite = pygame.transform.scale(pygame.image.load("images/GUI/"+image),(1000,300))
    self.rect = self.sprite.get_rect()
    self.rect.x = x
    self.rect.y = y

  def onClick(self, x, y, poke, otherpoke):
    num = random.randint(0,3)
    if(self.type == "main" and y<=850 and y>=700 and x >=0 and x <= 500):
              #fight
      self.type = "fight"
      ui.text = [poke.moves[0].name, poke.moves[1].name, poke.moves[2].name, poke.moves[3].name]
      
    elif(self.type == "main" and y<=850 and y>=700 and x >=500 and x <= 1000):
               #potion
      self.type = "bag"
      ui.text = ["Potion", "", "", ""]
       
    elif(self.type == "main" and y<=1000 and y >= 850 and x >=0 and x <= 500):
               #run
      pygame.quit()
      sys.exit()
    elif(self.type == "bag" and y<=850 and y>=700 and x >=0 and x <= 500):
      if(poke.potions>0):
        print('potion used')
        ui.text = ["Fight", "Bag", "Run", ""]
        self.type = 'main'
        poke.hp += 20
        poke.potions -=1
        self.notif = f"Potion Used. Potions left: {poke.potions}"

        hp1.sprite = pygame.transform.scale(pygame.image.load("images/GUI/HPBarSelf.png"),(max(0, poke.hp*2), 20))
        hp1.rect = hp1.sprite.get_rect()
        hp1.rect.x = 0
        hp1.rect.y = 0
        hp2.sprite = pygame.transform.scale(pygame.image.load("images/GUI/HPBarOther.png"),(max(0, otherpoke.hp*2), 20))
        hp2.rect = hp2.sprite.get_rect()
        hp2.rect.x = 0
        hp2.rect.y = 50
      else:
         self.notif = "No potions"


      
    elif(self.type == "fight" and y<=850 and y>=700 and x >=0 and x <= 500):
      print('top left attack')
      ui.text = ["Fight", "Bag", "Run", ""]
      self.type = 'main'

      fattack =poke.attack(otherpoke, poke.moves[0])
      self.notif2 = fattack
      sattack = otherpoke.attack(poke,otherpoke.moves[num])
      self.notif = sattack

      hp1.sprite = pygame.transform.scale(pygame.image.load("images/GUI/HPBarSelf.png"),(max(0, poke.hp*2), 20))
      hp1.rect = hp1.sprite.get_rect()
      hp1.rect.x = 0
      hp1.rect.y = 0
      hp2.sprite = pygame.transform.scale(pygame.image.load("images/GUI/HPBarOther.png"),(max(0, otherpoke.hp*2), 20))
      hp2.rect = hp2.sprite.get_rect()
      hp2.rect.x = 0
      hp2.rect.y = 50

      
      
      print('lion attacked')
      
    elif(self.type == 'fight' and y<=850 and y>=700 and x >=500 and x <= 1000):  
      print('top right attack')  
      ui.text = ["Fight", "Bag", "Run", ""]
      self.type ='main'
      fattack =poke.attack(otherpoke, poke.moves[1])
      self.notif2 = fattack
      print(otherpoke.hp)
      sattack =otherpoke.attack(poke,otherpoke.moves[num])
      self.notif = sattack

      hp1.sprite = pygame.transform.scale(pygame.image.load("images/GUI/HPBarSelf.png"),(max(0, poke.hp*2), 20))
      hp1.rect = hp1.sprite.get_rect()
      hp1.rect.x = 0
      hp1.rect.y = 0
      hp2.sprite = pygame.transform.scale(pygame.image.load("images/GUI/HPBarOther.png"),(max(0, otherpoke.hp*2), 20))
      hp2.rect = hp2.sprite.get_rect()
      hp2.rect.x = 0
      hp2.rect.y = 50
      

      print('lion attacked')
      return [fattack, sattack]
    elif(self.type == 'fight' and y<=1000 and y >= 850 and x >=0 and x <= 500):
       print('bottom left attack')
       ui.text = ["Fight", "Bag", "Run", ""]
       self.type = 'main'
       fattack = poke.attack(otherpoke, poke.moves[2])
       self.notif2 = fattack
       print(otherpoke.hp)
       sattack =otherpoke.attack(poke,otherpoke.moves[num])
       self.notif = sattack

       hp1.sprite = pygame.transform.scale(pygame.image.load("images/GUI/HPBarSelf.png"),(max(0, poke.hp*2), 20))
       hp1.rect = hp1.sprite.get_rect()
       hp1.rect.x = 0
       hp1.rect.y = 0
       hp2.sprite = pygame.transform.scale(pygame.image.load("images/GUI/HPBarOther.png"),(max(0, otherpoke.hp*2), 20))
       hp2.rect = hp2.sprite.get_rect()
       hp2.rect.x = 0
       hp2.rect.y = 50
       

       print('lion attacked')
       
    elif(self.type == 'fight' and y<=1000 and y >= 850 and x >=500 and x <= 1000):
       print('bottom right attack')
       ui.text = ["Fight", "Bag", "Run", ""]
       self.type ='main'
       fattack = poke.attack(otherpoke, poke.moves[3])
       self.notif2 = fattack
       print(otherpoke.hp)
       sattack = Lion.attack(poke,otherpoke.moves[num])
       self.notif = sattack

       hp1.sprite = pygame.transform.scale(pygame.image.load("images/GUI/HPBarSelf.png"),(max(0, poke.hp*2), 20))
       hp1.rect = hp1.sprite.get_rect()
       hp1.rect.x = 0
       hp1.rect.y = 0
       hp2.sprite = pygame.transform.scale(pygame.image.load("images/GUI/HPBarOther.png"),(max(0, otherpoke.hp*2), 20))
       hp2.rect = hp2.sprite.get_rect()
       hp2.rect.x = 0
       hp2.rect.y = 50
         
        
       print('lion attacked')
       
    
       
    
       

def display_text(screen, text, x, y, color):
    font = pygame.font.Font('pokemon_generation_1.ttf', 36)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()  # get bounding rectangle
    text_rect.center = (x, y)  # set the center of the rectangle
    screen.blit(text_surface, text_rect)  # blit using the rectangle
  

    


ui = UI(image = 'GeneralUI.png', type="main", scale = (1000, 300))
hp1 = UI(image = 'HPBarSelf.png', scale = (200, 20))
hp1background = UI(image = 'HPBackground.png', scale = (200, 20))
hp2 = UI(image = 'HPBarOther.png', scale = (200, 20))
hp2background = UI(image = 'HPBackground.png', scale = (200, 20))
ArenaBackground = UI(image = 'Background.png', scale = (1000, 700))
titlescreen = UI(image = 'MainMenu.png', scale = (1000,1000))
pokeball = UI(image = 'ESD_Pokeball.png', scale = (1000,1000))


pokeDisplay1 = Eagle
pokeDisplay2 = Lion

def gameStart(pMon1 = Eagle, pMon2 = Lion):
   pMon1.rect.x = 200
   pMon1.rect.y = 400
   pMon2.rect.x = 700
   pMon2.rect.y = 250
   
   ui.rect.x = 0
   ui.rect.y = 700
   hp1.rect.x = 0
   hp1.rect.y = 0
   hp2.rect.x = 0
   hp2.rect.y = 50
   hp1background.rect.x = 0
   hp1background.rect.y = 0
   hp2background.rect.x = 0
   hp2background.rect.y = 50
   titlescreen.rect.x = 0
   titlescreen.rect.y = 0
   pokeball.rect.x = 0
   pokeball.rect.y = 0


  
if(input("Would you like to use a custom-generated pokemon? (y/n) ") == "y"):
  nameAI = input("What type of pokemon would you like to generate?")
  moves = poke_gen.makePokemon(nameAI).split(", ")
  print(moves)
  AIMoves = [Attack(accuracy = 95, damage = 20, name = moves[0]), Attack(accuracy = 70, damage = 40, name = moves[1]), Attack(accuracy = 85, damage = 30, name = moves[2]), Attack(accuracy = 90, damage = 25, name = moves[3])]
  AIPoke = Pokemon(hp = random.randint(80,120), name = nameAI, moves = AIMoves, sprite = pygame.transform.scale(pygame.image.load(f"images/AISprites/{nameAI}Sprite.png"),(250,250)),potions = 2)
  gameStart(pMon1 = AIPoke, pMon2 = Lion)
  pokeDisplay1, pokeDisplay2 = AIPoke, Lion
else:
  gameStart()
  pokeDisplay1, pokeDisplay2 = Eagle, Lion

text_appear_time = None
textapprtime2 = None


screen.fill((255, 255, 255))
screen.blit(pokeball.sprite, pokeball.rect)
screen.blit(titlescreen.sprite, titlescreen.rect)

pygame.display.flip()
time.sleep(10)
while True:
    screen.fill((255, 255, 255))
    # display_text(screen, '', 500, 200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
           keys = pygame.key.get_pressed()
           if keys[K_BACKSPACE]:
              ui.text = ["Fight", "Bag", "Run", ""]
              ui.type = "main"
              
           
        if event.type == pygame.MOUSEBUTTONDOWN:
          mouse_presses = pygame.mouse.get_pressed()
          if mouse_presses[0]:
            pos = pygame.mouse.get_pos()
            print(pos)
            ui.onClick(pos[0],pos[1],pokeDisplay1, pokeDisplay2)
            # display_text(screen, ui.notif2, 500,200,(0,0,0))
            #   textapprtime2 = pygame.time.get_ticks()
            
            # if textapprtime2 is not None and pygame.time.get_ticks() - textapprtime2 >= 2000:
            #   # If they have, hide the text and reset textapprtime2
            #   ui.notif2 = ''
            #   textapprtime2 = None
          ui.displayUI()
          if(ui.notif != ''):
            ui.displayUI()
            # Save the time when the text appears 
            text_appear_time = pygame.time.get_ticks()
            
    if text_appear_time is not None and pygame.time.get_ticks() - text_appear_time >= 5000:
        # If they have, hide the text and reset text_appear_time
        ui.notif = ''
        ui.notif2 = ''
        text_appear_time = None
        ui.displayUI()
    endtime = None
    
    if(pokeDisplay1.hp <= 0):
       display_text(screen, pokeDisplay1.name + " fainted!", 500, 100, (0,0,0))
       
       endtime = pygame.time.get_ticks()
       

    if(pokeDisplay2.hp <= 0):
       display_text(screen, pokeDisplay2.name + " fainted!", 500, 200, (0,0,0))
       endtime = pygame.time.get_ticks()
       
    if endtime is not None and pygame.time.get_ticks() - text_appear_time >= 5000:
       pygame.quit()
       sys.exit()
    screen.blit(ArenaBackground.sprite, ArenaBackground.rect)
    screen.blit(pokeDisplay1.sprite, pokeDisplay1.rect)
    screen.blit(pokeDisplay2.sprite, pokeDisplay2.rect)
    screen.blit(ui.sprite, ui.rect)
    screen.blit(hp1background.sprite, hp1background.rect)
    screen.blit(hp2background.sprite, hp2background.rect)
    screen.blit(hp1.sprite, hp1.rect)
    screen.blit(hp2.sprite, hp2.rect)
    
    
    ui.displayUI()
    pygame.display.flip()