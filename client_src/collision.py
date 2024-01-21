# Import packages
from analysis import *
import threading
import sys

# Create semaphore with count = 1
sem = threading.Semaphore(1)

# Define collision for the puck in the left side
def collision1_1(puckSprite, dx1, dy1, dx, dy):
    # Collision of first puck
    # Checks for the collision between puck and player sprite, handles its collision
    if pygame.sprite.groupcollide(puckSprite, player, False, False, pygame.sprite.collide_circle):
        puck2.angle = math.atan2(int(dx1), int(dy1))
        puck2.speed = 15
    # Checks for the collision between the computer and the puck
    if pygame.sprite.groupcollide(puckSprite, playertwo, False, False, pygame.sprite.collide_circle):
        # determining the angle at which the puck should move after collision
        # using basic trigonometry and vector math
        puck2.angle = math.atan2(int(dx), int(dy))
        puck2.speed = -15

    sem.acquire()
    puckSprite.update()
    sem.release()

def collision1_2(puckSprite, dx1, dy1, dx, dy):
    # Collision of first puck
    # Checks for the collision between puck and player sprite, handles its collision
    if pygame.sprite.groupcollide(puckSprite, player, False, False, pygame.sprite.collide_circle):
        puck3.angle = math.atan2(int(dx1), int(dy1))
        puck3.speed = 14
    # Checks for the collision between the computer and the puck
    if pygame.sprite.groupcollide(puckSprite, playertwo, False, False, pygame.sprite.collide_circle):
        # determining the angle at which the puck should move after collision
        # using basic trigonometry and vector math
        puck3.angle = math.atan2(int(dx), int(dy))
        puck3.speed = -14

    sem.acquire()
    puckSprite.update()
    sem.release()

def collision1_3(puckSprite, dx1, dy1, dx, dy):
    # Collision of first puck
    # Checks for the collision between puck and player sprite, handles its collision
    if pygame.sprite.groupcollide(puckSprite, player, False, False, pygame.sprite.collide_circle):
        puck4.angle = math.atan2(int(dx1), int(dy1))
        puck4.speed = 13
    # Checks for the collision between the computer and the puck
    if pygame.sprite.groupcollide(puckSprite, playertwo, False, False, pygame.sprite.collide_circle):
        # determining the angle at which the puck should move after collision
        # using basic trigonometry and vector math
        puck4.angle = math.atan2(int(dx), int(dy))
        puck4.speed = -13

    sem.acquire()
    puckSprite.update()
    sem.release()

def collision1_4(puckSprite, dx1, dy1, dx, dy):
    # Collision of first puck
    # Checks for the collision between puck and player sprite, handles its collision
    if pygame.sprite.groupcollide(puckSprite, player, False, False, pygame.sprite.collide_circle):
        puck5.angle = math.atan2(int(dx1), int(dy1))
        puck5.speed = 12
    # Checks for the collision between the computer and the puck
    if pygame.sprite.groupcollide(puckSprite, playertwo, False, False, pygame.sprite.collide_circle):
        # determining the angle at which the puck should move after collision
        # using basic trigonometry and vector math
        puck5.angle = math.atan2(int(dx), int(dy))
        puck5.speed = -12

    sem.acquire()
    puckSprite.update()
    sem.release()

def collision1_5(puckSprite, dx1, dy1, dx, dy):
    # Collision of first puck
    # Checks for the collision between puck and player sprite, handles its collision
    if pygame.sprite.groupcollide(puckSprite, player, False, False, pygame.sprite.collide_circle):
        puck6.angle = math.atan2(int(dx1), int(dy1))
        puck6.speed = 11
    # Checks for the collision between the computer and the puck
    if pygame.sprite.groupcollide(puckSprite, playertwo, False, False, pygame.sprite.collide_circle):
        # determining the angle at which the puck should move after collision
        # using basic trigonometry and vector math
        puck6.angle = math.atan2(int(dx), int(dy))
        puck6.speed = -11

    sem.acquire()
    puckSprite.update()
    sem.release()

def collision1_6(puckSprite, dx1, dy1, dx, dy):
    # Collision of first puck
    # Checks for the collision between puck and player sprite, handles its collision
    if pygame.sprite.groupcollide(puckSprite, player, False, False, pygame.sprite.collide_circle):
        puck7.angle = math.atan2(int(dx1), int(dy1))
        puck7.speed = 10
    # Checks for the collision between the computer and the puck
    if pygame.sprite.groupcollide(puckSprite, playertwo, False, False, pygame.sprite.collide_circle):
        # determining the angle at which the puck should move after collision
        # using basic trigonometry and vector math
        puck7.angle = math.atan2(int(dx), int(dy))
        puck7.speed = -10

    sem.acquire()
    puckSprite.update()
    sem.release()


# Define collision for the puck in the right side
def collision2_1(puckSprite, dx1, dy1, dx, dy):
    # Collision of second puck
    # Checks for the collision between the computer and the puck
    if pygame.sprite.groupcollide(puckSprite, playertwo, False, False, pygame.sprite.collide_circle):
        # determining the angle at which the puck should move after collision
        # using basic trigonometry and vector math
        puck2.angle = math.atan2(int(dx1), int(dy1))
        puck2.speed = -15
    # Checks for the collision between puck and player sprite, handles its collision
    if pygame.sprite.groupcollide(puckSprite, player, False, False, pygame.sprite.collide_circle):
        puck2.angle = math.atan2(int(dx), int(dy))
        puck2.speed = 15

    sem.acquire()
    puckSprite.update()
    sem.release()

def collision2_2(puckSprite, dx1, dy1, dx, dy):
    # Collision of second puck
    # Checks for the collision between the computer and the puck
    if pygame.sprite.groupcollide(puckSprite, playertwo, False, False, pygame.sprite.collide_circle):
        # determining the angle at which the puck should move after collision
        # using basic trigonometry and vector math
        puck3.angle = math.atan2(int(dx1), int(dy1))
        puck3.speed = -14
    # Checks for the collision between puck and player sprite, handles its collision
    if pygame.sprite.groupcollide(puckSprite, player, False, False, pygame.sprite.collide_circle):
        puck3.angle = math.atan2(int(dx), int(dy))
        puck3.speed = 14

    sem.acquire()
    puckSprite.update()
    sem.release()

def collision2_3(puckSprite, dx1, dy1, dx, dy):
    # Collision of second puck
    # Checks for the collision between the computer and the puck
    if pygame.sprite.groupcollide(puckSprite, playertwo, False, False, pygame.sprite.collide_circle):
        # determining the angle at which the puck should move after collision
        # using basic trigonometry and vector math
        puck4.angle = math.atan2(int(dx1), int(dy1))
        puck4.speed = -13
    # Checks for the collision between puck and player sprite, handles its collision
    if pygame.sprite.groupcollide(puckSprite, player, False, False, pygame.sprite.collide_circle):
        puck4.angle = math.atan2(int(dx), int(dy))
        puck4.speed = 13

    sem.acquire()
    puckSprite.update()
    sem.release()

def collision2_4(puckSprite, dx1, dy1, dx, dy):
    # Collision of second puck
    # Checks for the collision between the computer and the puck
    if pygame.sprite.groupcollide(puckSprite, playertwo, False, False, pygame.sprite.collide_circle):
        # determining the angle at which the puck should move after collision
        # using basic trigonometry and vector math
        puck5.angle = math.atan2(int(dx1), int(dy1))
        puck5.speed = -12
    # Checks for the collision between puck and player sprite, handles its collision
    if pygame.sprite.groupcollide(puckSprite, player, False, False, pygame.sprite.collide_circle):
        puck5.angle = math.atan2(int(dx), int(dy))
        puck5.speed = 12

    sem.acquire()
    puckSprite.update()
    sem.release()

def collision2_5(puckSprite, dx1, dy1, dx, dy):
    # Collision of second puck
    # Checks for the collision between the computer and the puck
    if pygame.sprite.groupcollide(puckSprite, playertwo, False, False, pygame.sprite.collide_circle):
        # determining the angle at which the puck should move after collision
        # using basic trigonometry and vector math
        puck6.angle = math.atan2(int(dx1), int(dy1))
        puck6.speed = -11
    # Checks for the collision between puck and player sprite, handles its collision
    if pygame.sprite.groupcollide(puckSprite, player, False, False, pygame.sprite.collide_circle):
        puck6.angle = math.atan2(int(dx), int(dy))
        puck6.speed = 11

    sem.acquire()
    puckSprite.update()
    sem.release()

def collision2_6(puckSprite, dx1, dy1, dx, dy):
    # Collision of second puck
    # Checks for the collision between the computer and the puck
    if pygame.sprite.groupcollide(puckSprite, playertwo, False, False, pygame.sprite.collide_circle):
        # determining the angle at which the puck should move after collision
        # using basic trigonometry and vector math
        puck7.angle = math.atan2(int(dx1), int(dy1))
        puck7.speed = -10
    # Checks for the collision between puck and player sprite, handles its collision
    if pygame.sprite.groupcollide(puckSprite, player, False, False, pygame.sprite.collide_circle):
        puck7.angle = math.atan2(int(dx), int(dy))
        puck7.speed = 10

    sem.acquire()
    puckSprite.update()
    sem.release()
