import pygame
import random
from pygame import mixer

pygame.init()

screen=pygame.display.set_mode((800,600))
#-----Title----------------------------------
pygame.display.set_caption("Space Game")
#--Icon--------------------------------------
icone=pygame.image.load("ufo.png")
pygame.display.set_icon(icone)
background=pygame.image.load("background.jpg")
font = pygame.font.Font('freesansbold.ttf', 32)

#--Player----------------------------------------
playerImg=pygame.image.load("player.png")
playerX=400
playerY=480
#--Enemy---------------------------------
enemyImg=[]
enemyX=[]
enemyY=[]
dirtX=[]
#################################################################
num_of_enemies=6
for i in range(num_of_enemies):
   alien=['alien1.png','alien2.png','alien3.png','alien4.png','alien5.png','alien6.png','alien7.png','alien8.png','alien9.png','alien10.png']
   f=random.randint(0,9)
   enemyImg.append(pygame.image.load(alien[f]))
   enemyX.append(random.randint(0,700))
   enemyY.append(random.randint(0,100))
   dirtX.append(1)
steps=1
#----Bullet------------------------------------------------------
BImg=pygame.image.load("bullet.png")
BY=480
BX=370
state='ready'
#-----------------------------5------------------------------------
# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)
def game_over_text(score):
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def isCollision(enemyX,enemyY,BX,BY):
   distance=(((BX-enemyX)**2)+((BY-enemyY)**2))**0.5
   if distance<27:
      return True
   return False

def bullet(x,y):
   global state
   state='fire'
   screen.blit(BImg,(x+25,y+25))

def show_score(x, y,score):
    score = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score, (x, y))
   
def player(playerX,playerY):
   screen.blit(playerImg,(playerX+10,playerY))

def Enemy(enemyX,enemyY,enemyImg,dirtX):
   screen.blit(enemyImg,(enemyX,enemyY))

vel=6
running=True
score=0
while running:
   screen.fill((0, 0, 0))
   screen.blit(background, (0, 0))
   for event in pygame.event.get():
      if event.type==pygame.QUIT:
         running=False

   keys= pygame.key.get_pressed()
   if keys[pygame.K_LEFT] and playerX>0:
      playerX-=vel
   if keys[pygame.K_RIGHT] and playerX<730:
      playerX+=vel
   if keys[pygame.K_SPACE] and playerY>0:
      if state=='ready':
         bullet(playerX,BY)
         BX=playerX
   if state=='fire':
      BY-=10
      bullet(BX,BY)
      if BY==0:
         state='ready'
         BX=playerX+10
         BY=playerY
   #---------------------------------
   for i in range(num_of_enemies):
      # Game Over
      if enemyY[i] > 440:
         for j in range(num_of_enemies):
             enemyY[j] = 2000
             playerX=2000
             playerY=2000

         game_over_text(score)
         break

      if dirtX[i]==1:
         enemyX[i]+=5
         if enemyX[i]>=700:
            dirtX[i]=-1
            enemyY[i]+=40
      if dirtX[i]==-1:
         enemyX[i]-=5
         if enemyX[i]<=0:
            dirtX[i]=1
            enemyY[i]+=40
      #collistion
      collision=isCollision(enemyX[i],enemyY[i],BX,BY)
      if collision:
         bulletSound = mixer.Sound("laser.wav")
         bulletSound.play()

         BY=100
         state="ready"
         score+=1
         alien=['alien1.png','alien2.png','alien3.png','alien4.png','alien5.png','alien6.png','alien7.png','alien8.png','alien9.png','alien10.png']
         rdm=random.randint(0,9)
         enemyImg[i]=pygame.image.load(alien[rdm])
         enemyX[i]=random.randint(10,730)
         enemyY[i]=random.randint(10,200)
         d=[-1,1]
         dirtX[i]=d[random.randint(0,1)]
      Enemy(enemyX[i],enemyY[i],enemyImg[i],dirtX[i])

   show_score(10,10,score)   
   player(playerX,playerY)
   pygame.display.update()

pygame.quit()
