# Import packages
from classes import *
pygame.font.init()

# Background, Time, Puck, Player, Computer Create
# Set screen 設定視窗
width = 800
height = 400
pygame.font.init()
pygame.display.set_caption("Air Hockey")
win = pygame.display.set_mode((800, 400))

# Creates the background table (Air Hockey 背景)
background = Background('component/table.png')
background.image = background.image.convert()
pygame.display.flip()

# Menu continue (遊戲初始背景)
mainMenu2 = Background('component/menu.png')
mainMenu2.image = mainMenu2.image.convert()

# Game over (遊戲結束背景)
mainMenu3 = Background('component/gameover.png')
mainMenu3.image = mainMenu3.image.convert()

# Starts the game clock (遊戲時間紀錄)
clock = pygame.time.Clock()
timeKeeper = Timer('tool/digital-7.ttf', 60)

# Creating puck sprite and setting it into a sprite group (創建球)
# puck1 is for between player and computer
puck1 = Puck1(0, 0)
puckSprite1 = pygame.sprite.RenderPlain(puck1)

# first puck for between player1 and player2
puck2 = Puck2_1(0, 0)
puckSprite2 = pygame.sprite.RenderPlain(puck2)
# second puck for between player1 and player2
puck3 = Puck2_2(0, 0)
puckSprite3 = pygame.sprite.RenderPlain(puck3)
# third puck for between player1 and player2
puck4 = Puck2_3(0, 0)
puckSprite4 = pygame.sprite.RenderPlain(puck4)
# fourth puck for between player1 and player2
puck5 = Puck2_4(0, 0)
puckSprite5 = pygame.sprite.RenderPlain(puck5)
# fifth puck for between player1 and player2
puck6 = Puck2_5(0, 0)
puckSprite6 = pygame.sprite.RenderPlain(puck6)
# sixth puck for between player1 and player2
puck7 = Puck2_6(0, 0)
puckSprite7 = pygame.sprite.RenderPlain(puck7)


# Setting up the player and computer sprites and setting them to a group (創建 player1, player2, computer)
player1 = Player()
comp = Comp()
player2 = Player2()
cplayer = CPlayer()

player = pygame.sprite.RenderPlain(player1)
compPlayer = pygame.sprite.RenderPlain(comp)
playertwo = pygame.sprite.RenderPlain(player2)
playercomp = pygame.sprite.RenderPlain(cplayer)

compScore = Scores('tool/digital-7.ttf', 70, 0)
playerScore = Scores('tool/digital-7.ttf', 70, 0)
player2Score = Scores('tool/digital-7.ttf', 70, 0)
cplayerScore = Scores('tool/digital-7.ttf', 70, 0)

# Final message
message = pygame.font.Font('tool/a-bugs-life.ttf', 100)
pygame.display.set_caption("Air Hockey")

mainM = True
# Accumulator for getting the recent coordinates of the computer. helps in
# deciding the movement of the computer
coord = []
