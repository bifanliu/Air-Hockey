# Import packages
from collision import *


def STrace(disp):
    mainM2 = False
    # Updating the scores
    compText = compScore.render(str(puck1.compScore), False, (0, 0, 0))
    playerText = cplayerScore.render(str(puck1.playerScore), False, (0, 0, 0))

    # Checking the most recent coordinates of the computer
    coord.append(comp.rect.center)
    disp.blit(background.image, (0, 0))

    # Checking the updating the clock
    timeElapsed = clock.tick(60)
    timeKeeper.update(timeElapsed)
    timeText = timeKeeper.displayTime()

    # This flag is for the odd case where the computer gets stuck at a corner
    # with the puck
    comp.stagnant = False
    if isClicked(340, 0, 90, 50):
        mainM2 = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            cplayer.mouseMove1()

    # Checks for the collision between puck and player sprite, handles its collision
    if pygame.sprite.groupcollide(puckSprite1, playercomp, False, False,
                                    pygame.sprite.collide_circle_ratio(0.8)):
        time.sleep(0.01)
        (dx, dy) = pygame.mouse.get_rel()
        puck1.angle = math.atan2(dy, dx)
        puck1.speed = 15

    # Checks for the collision between the computer and the puck
    elif pygame.sprite.groupcollide(puckSprite1, compPlayer, False, False,
                                    pygame.sprite.collide_circle_ratio(0.8)) and len(coord) > 1:
        # determining the angle at which the puck should move after collision
        # using basic trigonometry and vector math
        time.sleep(0.01)
        dx = coord[-1][0] - coord[-2][0]
        dy = coord[-1][1] - coord[-2][1]

        if coord[-1][1] == coord[-2][1]:
            puck1.calcNewPos(puck1.rect, math.pi, 30)
            puck1.angle = math.pi
            comp.stagnant = True
        else:
            puck1.angle = math.atan2(dy, dx)
            puck1.speed = 15

    # Checking to see if the puck is in the computer half, the computer
    # follows the puck only if it is in its half
    if puck1.courtHalf() == 'right':
        comp.calculateNewPos(puck1.rect.center)
    elif puck1.courtHalf() == 'left':
        coord.clear()

    # Places the puck back in the center
    if puck1.goal:
        puck1.goal = False
        puck1.rect.center = puck1.area.center

    # Blits all the objects on to the display every frame
    disp.blit(background.image, puck1.rect, puck1.rect)
    disp.blit(background.image, cplayer.rect, cplayer.rect)
    disp.blit(background.image, comp.rect, comp.rect)
    disp.blit(compText, (550, 175))
    disp.blit(playerText, (220, 175))
    disp.blit(timeText, (340, 180))

    # Updates the sprites
    playercomp.update()
    compPlayer.update()
    puckSprite1.update()

    playercomp.draw(disp)
    puckSprite1.draw(disp)
    compPlayer.draw(disp)

    pygame.display.flip()

    return mainM2

def SGameOver(disp):
    gameOver = True
    # Returns you to the main menu if the game is over. i.e 1 minutes have passed
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif isClicked(120, 290, 130, 70):
            # Resetting all variables for another game
            gameOver = False
            puck1.compScore = 0
            puck1.playerScore = 0
            timeKeeper.min = 0  # min
            timeKeeper.seconds = 60
            puck1.rect.center = puck1.area.center

        # Check to see if the user pressed the quit button
        elif isClicked(540, 290, 130, 70):
            pygame.quit()
        # Check to see if player wins or computer wins or if it is a draw
        if puck1.compScore > puck1.playerScore:
            msg = message.render('Computer Wins', False, (0, 0, 0))
        elif puck1.compScore == puck1.playerScore:
            msg = message.render('It is a draw!', False, (0, 0, 0))
        else:
            msg = message.render('Player wins', False, (0, 0, 0))
        msgcent = msg.get_rect()
        msgcent.center = (400,200)
        disp.blit(mainMenu3.image, (0, 0))
        disp.blit(msg, msgcent)
    return gameOver

def SmainM2(disp):
    mainM2 = True
    disp.blit(mainMenu2.image, (0, 0))  # display menu
    pygame.display.flip()  # display menu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif isClicked(144, 273, 115, 65):
            mainM2 = False
            continue
        elif isClicked(545, 273, 115, 65):
            pygame.quit()
            sys.exit()
    return mainM2