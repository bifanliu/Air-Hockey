# (1) Import packages
import pygame
import math
from pygame.locals import *
import time

# (2) Load images into a variable name, returns an image surface and image rect
def load_img(name):
    image = pygame.image.load(name)
    return image, image.get_rect()

# (3) Initiates a background for the display, Air Hockey is the image
class Background(pygame.sprite.Sprite):
    def __init__(self, image):
        self.image, self.rect = load_img(image)

# (4) Display scores during the game
class Scores(pygame.font.Font):
    def __init__(self, fontType, size, score):
        pygame.font.Font.__init__(self, fontType, size)
        self.score = score
    def scoreUpdate(self, newScore):
        # this methods updates the time on the display
        self.score = newScore 

# (5) Keeps track of the time during the game, each game lasts for 3 minute
class Timer(pygame.font.Font):
    def __init__(self, fontType, size):
        # instanctiating the relevant variables
        pygame.font.Font.__init__(self, fontType, size)
        self.min = 0
        self.seconds = 60
     
        # accumulates the total time in milliseconds
        self.milliseconds = 0
        
    def update(self, delTime):
        # updates the time. the logic for the timer
        self.milliseconds += delTime
        if self.milliseconds > 1000:
            self.seconds -= 1
            self.milliseconds = 0
        if self.seconds == 0:
            self.seconds = 60
            self.min -= 1

    def recordtime(self, delTime):
        self.milliseconds += delTime
        if self.milliseconds > 1000:
            self.seconds -= 1
            self.milliseconds = 0
        if self.seconds == 0:
            self.seconds = 60
            self.min -= 1

        return self.seconds
            
    def displayTime(self):
        # this methods displays the time on the table
        if self.seconds == 60:
            label = self.render('{:0>2}:{:0>2}'.format(self.min+1, 0), False, (0, 0, 0))
        else: 
            label = self.render('{:0>2}:{:0>2}'.format(self.min, self.seconds), False, (0, 0, 0))
        return label

# This class deals with the interaction of the puck in the game. It has all relevant
# (6) Variables like angles, speeds scores instantiated.
class Puck1(pygame.sprite.Sprite):
    def __init__(self, angle, speed):
        # Variable instantiation
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_img('component/puck.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.angle = angle
        self.speed = speed
        self.compScore = 0
        self.playerScore = 0 
        self.goal = False 
        self.rect.center = self.area.center 
        
    def calcNewPos(self, rect, angle, speed):
        # Calculates new position for the puck every frame of the game. uses basic trigonometry
        dx, dy = speed*math.cos(angle), speed*math.sin(angle)
        return rect.move(dx, dy)
    
    def update(self):
        # Updates the position of the puck from the position in the last frame
        newpos = self.calcNewPos(self.rect, self.angle, self.speed, )
        # Implementing friction for the puck
        if self.speed > 0:
            self.speed -= 0.03
        self.rect = newpos

        # The logic below checks for collisions in the edges of the display and
        # implements proper collisions
        if not self.area.contains(newpos) and not self.goal:
       
            xl = self.rect.left
            xr = self.rect.right
            yt = self.rect.top
            yb = self.rect.bottom

            if xl < self.area.left:
                if 275 > self.rect.midleft[1] > 125:
                    self.compScore += 1
                    self.rect.center = (400,200)
                    self.goal = True
                    time.sleep(0.1)
                    self.speed = 0
                else: 
                    self.rect.midleft = (self.area.left, self.rect.centery) 
                    self.angle = math.pi - self.angle
                    
            elif xr > self.area.right:
                if 275 > self.rect.midright[1] > 125 :
                    self.playerScore += 1
                    self.speed = 0
                    self.rect.center = (400,200)
                    self.goal = True 
                    time.sleep(0.1)

                else:     
                    self.rect.midright = (self.area.right, self.rect.centery)
                    self.angle = math.pi - self.angle

            elif yt < self.area.top:
                self.rect.midtop = (self.rect.centerx, self.area.top) 
                self.angle = -self.angle

            elif yb > self.area.bottom:
                self.rect.midbottom = (self.rect.centerx, self.area.bottom) 
                self.angle = -self.angle

        return newpos

    def courtHalf(self):
        # This method check which half the puck is on
        if self.rect.midright[0] < self.area.centerx:
            return 'left'
        else:
            return 'right'

class Puck2_1(pygame.sprite.Sprite):
    def __init__(self, angle, speed):
        # Variable instantiation
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_img('component/puck2.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.angle = angle
        self.speed = speed
        self.player2Score = 0
        self.playerScore = 0
        self.goal = False
        self.rect.center = self.area.center

    def calcNewPos(self, rect, angle, speed):
        # Calculates new position for the puck every frame of the game. uses basic trigonometry
        dx, dy = speed * math.cos(angle), speed * math.sin(angle)
        return rect.move(dx, dy)

    def update(self):
        # Updates the position of the puck from the position in the last frame
        newpos = self.calcNewPos(self.rect, self.angle, self.speed, )
        # Implementing friction for the puck
        # if self.speed > 0:
        #     self.speed -= 0.03
        self.rect = newpos

        # The logic below checks for collisions in the edges of the display and
        # implements proper collisions
        if not self.area.contains(newpos) and not self.goal:

            xl = self.rect.left
            xr = self.rect.right
            yt = self.rect.top
            yb = self.rect.bottom

            if xl < self.area.left:
                if 275 > self.rect.midleft[1] > 125:
                    self.player2Score += 1
                    self.rect.center = (400, 200)
                    self.goal = True
                    time.sleep(0.1)
                    self.speed = 0
                else:
                    self.rect.midleft = (self.area.left, self.rect.centery)
                    self.angle = math.pi - self.angle

            elif xr > self.area.right:
                if 275 > self.rect.midright[1] > 125:
                    self.playerScore += 1
                    self.speed = 0
                    self.rect.center = (400, 200)
                    self.goal = True
                    time.sleep(0.1)

                else:
                    self.rect.midright = (self.area.right, self.rect.centery)
                    self.angle = math.pi - self.angle

            elif yt < self.area.top:
                self.rect.midtop = (self.rect.centerx, self.area.top)
                self.angle = -self.angle

            elif yb > self.area.bottom:
                self.rect.midbottom = (self.rect.centerx, self.area.bottom)
                self.angle = -self.angle

        return newpos

    def courtHalf(self):
        # This method check which half the puck is on
        if self.rect.midright[0] < self.area.centerx:
            return 'left'
        else:
            return 'right'

class Puck2_2(pygame.sprite.Sprite):
    def __init__(self, angle, speed):
        # Variable instantiation
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_img('component/puck3.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.angle = angle
        self.speed = speed
        self.player2Score = 0
        self.playerScore = 0
        self.goal = False
        self.rect.center = self.area.center

    def calcNewPos(self, rect, angle, speed):
        # Calculates new position for the puck every frame of the game. uses basic trigonometry
        dx, dy = speed * math.cos(angle), speed * math.sin(angle)
        return rect.move(dx, dy)

    def update(self):
        # Updates the position of the puck from the position in the last frame
        newpos = self.calcNewPos(self.rect, self.angle, self.speed, )
        # Implementing friction for the puck
        # if self.speed > 0:
        #     self.speed -= 0.03
        self.rect = newpos

        # The logic below checks for collisions in the edges of the display and
        # implements proper collisions
        if not self.area.contains(newpos) and not self.goal:

            xl = self.rect.left
            xr = self.rect.right
            yt = self.rect.top
            yb = self.rect.bottom

            if xl < self.area.left:
                if 275 > self.rect.midleft[1] > 125:
                    self.player2Score += 1
                    self.rect.center = (400, 200)
                    self.goal = True
                    time.sleep(0.1)
                    self.speed = 0
                else:
                    self.rect.midleft = (self.area.left, self.rect.centery)
                    self.angle = math.pi - self.angle

            elif xr > self.area.right:
                if 275 > self.rect.midright[1] > 125:
                    self.playerScore += 1
                    self.speed = 0
                    self.rect.center = (400, 200)
                    self.goal = True
                    time.sleep(0.1)

                else:
                    self.rect.midright = (self.area.right, self.rect.centery)
                    self.angle = math.pi - self.angle

            elif yt < self.area.top:
                self.rect.midtop = (self.rect.centerx, self.area.top)
                self.angle = -self.angle

            elif yb > self.area.bottom:
                self.rect.midbottom = (self.rect.centerx, self.area.bottom)
                self.angle = -self.angle

        return newpos

    def courtHalf(self):
        # This method check which half the puck is on
        if self.rect.midright[0] < self.area.centerx:
            return 'left'
        else:
            return 'right'

class Puck2_3(pygame.sprite.Sprite):
    def __init__(self, angle, speed):
        # Variable instantiation
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_img('component/puck4.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.angle = angle
        self.speed = speed
        self.player2Score = 0
        self.playerScore = 0
        self.goal = False
        self.rect.center = self.area.center

    def calcNewPos(self, rect, angle, speed):
        # Calculates new position for the puck every frame of the game. uses basic trigonometry
        dx, dy = speed * math.cos(angle), speed * math.sin(angle)
        return rect.move(dx, dy)

    def update(self):
        # Updates the position of the puck from the position in the last frame
        newpos = self.calcNewPos(self.rect, self.angle, self.speed, )
        # Implementing friction for the puck
        # if self.speed > 0:
        #     self.speed -= 0.03
        self.rect = newpos

        # The logic below checks for collisions in the edges of the display and
        # implements proper collisions
        if not self.area.contains(newpos) and not self.goal:

            xl = self.rect.left
            xr = self.rect.right
            yt = self.rect.top
            yb = self.rect.bottom

            if xl < self.area.left:
                if 275 > self.rect.midleft[1] > 125:
                    self.player2Score += 1
                    self.rect.center = (400, 200)
                    self.goal = True
                    time.sleep(0.1)
                    self.speed = 0
                else:
                    self.rect.midleft = (self.area.left, self.rect.centery)
                    self.angle = math.pi - self.angle

            elif xr > self.area.right:
                if 275 > self.rect.midright[1] > 125:
                    self.playerScore += 1
                    self.speed = 0
                    self.rect.center = (400, 200)
                    self.goal = True
                    time.sleep(0.1)

                else:
                    self.rect.midright = (self.area.right, self.rect.centery)
                    self.angle = math.pi - self.angle

            elif yt < self.area.top:
                self.rect.midtop = (self.rect.centerx, self.area.top)
                self.angle = -self.angle

            elif yb > self.area.bottom:
                self.rect.midbottom = (self.rect.centerx, self.area.bottom)
                self.angle = -self.angle

        return newpos

    def courtHalf(self):
        # This method check which half the puck is on
        if self.rect.midright[0] < self.area.centerx:
            return 'left'
        else:
            return 'right'

class Puck2_4(pygame.sprite.Sprite):
    def __init__(self, angle, speed):
        # Variable instantiation
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_img('component/puck5.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.angle = angle
        self.speed = speed
        self.player2Score = 0
        self.playerScore = 0
        self.goal = False
        self.rect.center = self.area.center

    def calcNewPos(self, rect, angle, speed):
        # Calculates new position for the puck every frame of the game. uses basic trigonometry
        dx, dy = speed * math.cos(angle), speed * math.sin(angle)
        return rect.move(dx, dy)

    def update(self):
        # Updates the position of the puck from the position in the last frame
        newpos = self.calcNewPos(self.rect, self.angle, self.speed, )
        # Implementing friction for the puck
        # if self.speed > 0:
        #     self.speed -= 0.03
        self.rect = newpos

        # The logic below checks for collisions in the edges of the display and
        # implements proper collisions
        if not self.area.contains(newpos) and not self.goal:

            xl = self.rect.left
            xr = self.rect.right
            yt = self.rect.top
            yb = self.rect.bottom

            if xl < self.area.left:
                if 275 > self.rect.midleft[1] > 125:
                    self.player2Score += 1
                    self.rect.center = (400, 200)
                    self.goal = True
                    time.sleep(0.1)
                    self.speed = 0
                else:
                    self.rect.midleft = (self.area.left, self.rect.centery)
                    self.angle = math.pi - self.angle

            elif xr > self.area.right:
                if 275 > self.rect.midright[1] > 125:
                    self.playerScore += 1
                    self.speed = 0
                    self.rect.center = (400, 200)
                    self.goal = True
                    time.sleep(0.1)

                else:
                    self.rect.midright = (self.area.right, self.rect.centery)
                    self.angle = math.pi - self.angle

            elif yt < self.area.top:
                self.rect.midtop = (self.rect.centerx, self.area.top)
                self.angle = -self.angle

            elif yb > self.area.bottom:
                self.rect.midbottom = (self.rect.centerx, self.area.bottom)
                self.angle = -self.angle

        return newpos

    def courtHalf(self):
        # This method check which half the puck is on
        if self.rect.midright[0] < self.area.centerx:
            return 'left'
        else:
            return 'right'

class Puck2_5(pygame.sprite.Sprite):
    def __init__(self, angle, speed):
        # Variable instantiation
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_img('component/puck8.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.angle = angle
        self.speed = speed
        self.player2Score = 0
        self.playerScore = 0
        self.goal = False
        self.rect.center = self.area.center

    def calcNewPos(self, rect, angle, speed):
        # Calculates new position for the puck every frame of the game. uses basic trigonometry
        dx, dy = speed * math.cos(angle), speed * math.sin(angle)
        return rect.move(dx, dy)

    def update(self):
        # Updates the position of the puck from the position in the last frame
        newpos = self.calcNewPos(self.rect, self.angle, self.speed, )
        # Implementing friction for the puck
        # if self.speed > 0:
        #     self.speed -= 0.03
        self.rect = newpos

        # The logic below checks for collisions in the edges of the display and
        # implements proper collisions
        if not self.area.contains(newpos) and not self.goal:

            xl = self.rect.left
            xr = self.rect.right
            yt = self.rect.top
            yb = self.rect.bottom

            if xl < self.area.left:
                if 275 > self.rect.midleft[1] > 125:
                    self.player2Score += 1
                    self.rect.center = (400, 200)
                    self.goal = True
                    time.sleep(0.1)
                    self.speed = 0
                else:
                    self.rect.midleft = (self.area.left, self.rect.centery)
                    self.angle = math.pi - self.angle

            elif xr > self.area.right:
                if 275 > self.rect.midright[1] > 125:
                    self.playerScore += 1
                    self.speed = 0
                    self.rect.center = (400, 200)
                    self.goal = True
                    time.sleep(0.1)

                else:
                    self.rect.midright = (self.area.right, self.rect.centery)
                    self.angle = math.pi - self.angle

            elif yt < self.area.top:
                self.rect.midtop = (self.rect.centerx, self.area.top)
                self.angle = -self.angle

            elif yb > self.area.bottom:
                self.rect.midbottom = (self.rect.centerx, self.area.bottom)
                self.angle = -self.angle

        return newpos

    def courtHalf(self):
        # This method check which half the puck is on
        if self.rect.midright[0] < self.area.centerx:
            return 'left'
        else:
            return 'right'

class Puck2_6(pygame.sprite.Sprite):
    def __init__(self, angle, speed):
        # Variable instantiation
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_img('component/puck9.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.angle = angle
        self.speed = speed
        self.player2Score = 0
        self.playerScore = 0
        self.goal = False
        self.rect.center = self.area.center

    def calcNewPos(self, rect, angle, speed):
        # Calculates new position for the puck every frame of the game. uses basic trigonometry
        dx, dy = speed * math.cos(angle), speed * math.sin(angle)
        return rect.move(dx, dy)

    def update(self):
        # Updates the position of the puck from the position in the last frame
        newpos = self.calcNewPos(self.rect, self.angle, self.speed, )
        # Implementing friction for the puck
        # if self.speed > 0:
        #     self.speed -= 0.03
        self.rect = newpos

        # The logic below checks for collisions in the edges of the display and
        # implements proper collisions
        if not self.area.contains(newpos) and not self.goal:

            xl = self.rect.left
            xr = self.rect.right
            yt = self.rect.top
            yb = self.rect.bottom

            if xl < self.area.left:
                if 275 > self.rect.midleft[1] > 125:
                    self.player2Score += 1
                    self.rect.center = (400, 200)
                    self.goal = True
                    time.sleep(0.1)
                    self.speed = 0
                else:
                    self.rect.midleft = (self.area.left, self.rect.centery)
                    self.angle = math.pi - self.angle

            elif xr > self.area.right:
                if 275 > self.rect.midright[1] > 125:
                    self.playerScore += 1
                    self.speed = 0
                    self.rect.center = (400, 200)
                    self.goal = True
                    time.sleep(0.1)

                else:
                    self.rect.midright = (self.area.right, self.rect.centery)
                    self.angle = math.pi - self.angle

            elif yt < self.area.top:
                self.rect.midtop = (self.rect.centerx, self.area.top)
                self.angle = -self.angle

            elif yb > self.area.bottom:
                self.rect.midbottom = (self.rect.centerx, self.area.bottom)
                self.angle = -self.angle

        return newpos

    def courtHalf(self):
        # This method check which half the puck is on
        if self.rect.midright[0] < self.area.centerx:
            return 'left'
        else:
            return 'right'


# This class deals with the interaction of the player in the game. It allows the
# (7) player to move his striker with the aid of the mouse controller. It also handles
# collisions with the puck
class Player(pygame.sprite.Sprite):
    def __init__(self ):
        # instantiates variables
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_img('component/player.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect() 
        self.newpos = (0,0)  
        self.start()
        
    def start(self):
        # start position of the player
        self.rect.midleft = self.area.midleft

    def mouseMove1(self):
        # this method check the mouse position for the player striker to follow
        self.newpos = pygame.mouse.get_pos()
        temp_newpos = list(self.newpos)
        if temp_newpos[0] < 70:
            temp_newpos[0] = 70
        if temp_newpos[0] > 322:
            temp_newpos[0] = 322
        if temp_newpos[1] < 70:
            temp_newpos[1] = 70
        if temp_newpos[1] > 330:
            temp_newpos[1] = 330
        self.newpos = tuple(temp_newpos)
        return self.newpos

    def mouseMove2(self, dx, dy):
        # this method check the mouse position for the player striker to follow
        self.newpos = tuple((dx, dy))

    def update(self):
        # this method updates the position of the puck in the game
        self.rect.center = self.newpos 
        # contain player in his area
        if self.rect.centerx > self.area.centerx:
            self.rect.midright = (self.area.centerx, self.rect.centery)
        pygame.event.pump()

# (8) This class deals with the interaction of the player in the game. It allows the
# player to move his striker with the aid of the mouse controller. It also handles
# collisions with the puck
class Player2(pygame.sprite.Sprite):
    def __init__(self ):
        # instantiates variables
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_img('component/comp.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect() 
        self.newpos = (0,0)  
        self.start()
        
    def start(self):
        # start position of the player
        self.rect.midright = self.area.midright

    def mouseMove1(self):
        # this method check the mouse position for the player striker to follow
        self.newpos = pygame.mouse.get_pos()
        temp_newpos = list(self.newpos)
        # if temp_newpos[0] < 487:
        #     temp_newpos[0] = 487
        if temp_newpos[0] < 478:
            temp_newpos[0] = 478
        if temp_newpos[0] > 730:
            temp_newpos[0] = 730
        if temp_newpos[1] < 70:
            temp_newpos[1] = 70
        if temp_newpos[1] > 330:
            temp_newpos[1] = 330
        self.newpos = tuple(temp_newpos)
        return self.newpos

    def mouseMove2(self, dx, dy):
        # this method check the mouse position for the player striker to follow
        self.newpos = tuple((dx, dy))

    def update(self):
        # this method updates the mouse position of the puck in the game
        self.rect.center = self.newpos
        # contain player in his area
        if self.rect.centerx < self.area.centerx:
            self.rect.midleft = (self.area.centerx, self.rect.centery)
        pygame.event.pump()

# (9) This class deals with the interaction of the player in the game. It allows the
# player to move his striker with the aid of the mouse controller. It also handles
# collisions with the puck
class CPlayer(pygame.sprite.Sprite):
    def __init__(self):
        # instantiates variables
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_img('component/player.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.newpos = (0, 0)
        self.start()

    def start(self):
        # start position of the player
        self.rect.midleft = self.area.midleft

    def mouseMove1(self):
        # this method check the mouse position for the player striker to follow
        self.newpos = pygame.mouse.get_pos()
        return self.newpos

    def mouseMove2(self, dx, dy):
        # this method check the mouse position for the player striker to follow
        self.newpos = tuple((dx, dy))

    def update(self):
        # this method updates the position of the puck in the game
        self.rect.center = self.newpos
        # contain player in his area
        if self.rect.centerx > self.area.centerx:
            self.rect.midright = (self.area.centerx, self.rect.centery)
        pygame.event.pump()


# (10) This class deals with the interaction of the computer striker in the game.
# It is very similar to the player class. The only difference is the calculateNewPos method
# which is designed make the computer follow the puck on its own
class Comp(pygame.sprite.Sprite):
    def __init__(self):
        # variable intantiation
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_img('component/comp.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.start()
        self.speed = 5
        self.angle = 0
        self.stagnant = False # computer stuck in the corner

    def start(self):
        self.rect.midright = self.area.midright
        
    def calculateNewPos(self, target):
        # this method uses basic vector and trigonometry to figure out the position of the
        # puck and make the computer move accordingly
        if not self.stagnant: 
            dx, dy = target[0] - self.rect.centerx, target[1] - self.rect.centery
            self.angle = math.atan2(dy, dx)
            dx, dy = self.speed*math.cos(self.angle), self.speed*math.sin(self.angle)
            self.rect= self.rect.move(dx, dy)

    def update(self):
        newpos = self.rect
    
        if not self.area.contains(newpos):

            tl = not self.area.collidepoint(newpos.topleft)
            tr = not self.area.collidepoint(newpos.topright)
            bl = not self.area.collidepoint(newpos.bottomleft)
            br = not self.area.collidepoint(newpos.bottomright)

            if tr and tl:
                self.rect.midtop = (self.rect.centerx, self.area.top) 
                self.angle = -self.angle
            if br and bl:
                self.rect.midbottom = (self.rect.centerx, self.area.bottom) 
                self.angle = -self.angle
            elif tr and br:
                self.rect.midright = (self.area.right, self.rect.centery) 
                self.angle = math.pi - self.angle

        elif self.rect.centerx < self.area.centerx:
            self.rect.midleft = (self.area.centerx, self.rect.centery)

    def movefaster(self):
        # Puck becomes faster when
        self.speed = self.speed + 0.001


# (11) Detect user clicks on the buttons of the menu.
def isClicked(x, y, w, h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0]:
            return True
