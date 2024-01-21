# Import packages
from collision import *

def MSUpdateBluePlyer(socket_client):
    gameOver = False
    pos = player1.mouseMove1()  # Get blue player's position
    socket_client.send(str.encode(str(pos)))  # Client send red player's position to server
    pos2 = socket_client.recv(1024).decode('utf8')  # Client receives red player's position from server
    if pos2[0] == 'g':
        print("gameover")
        gameOver = True
    elif pos2[0] == 'o':
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("player leave", True, (255, 0, 0), True)
        win.blit(text, (700 / 2 - text.get_width() / 2, 300 / 2 - text.get_height() / 2))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
    else:
        pos3 = pos2.split(",")
        dx = pos3[0][1:]
        pos4 = pos3[1]
        pos5 = pos4.split(")")
        dy = pos5[0]
        player2.mouseMove2(int(dx), int(dy))
        (dx1, dy1) = pos

        # Create thread for each puck
        t1 = threading.Thread(target=collision1_1, args=(puckSprite2, dx1, dy1, dx, dy))

        # Thread execution
        t1.start()
    return gameOver

def MSUpdateRedPlyer(socket_client):
    gameOver = False
    pos = player2.mouseMove1()  # Get blue player's position
    socket_client.send(str.encode(str(pos)))  # Client send blue player's position to server
    pos2 = socket_client.recv(1024).decode('utf8')  # Client receives blue player's position from server
    if pos2[0] == 'g':
        gameOver = True
    elif pos2[0] == 'o':
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("player leave", True, (255, 0, 0), True)
        win.blit(text, (700 / 2 - text.get_width() / 2, 300 / 2 - text.get_height() / 2))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
    else:
        pos3 = pos2.split(",")
        dx = pos3[0][1:]
        pos4 = pos3[1]
        pos5 = pos4.split(")")
        dy = pos5[0]
        player1.mouseMove2(int(dx), int(dy))
        (dx1, dy1) = pos

        # Create thread for each puck
        t1 = threading.Thread(target=collision2_1, args=(puckSprite2, dx1, dy1, dx, dy))

        # Thread execution
        t1.start()
    return gameOver

def MSGameNotOver(disp, socket_client, playerText, player2Text, timeText):
    mainM2 = False
    # Places the puck back in the
    if puck2.goal:
        puck2.goal = False
        puck2.rect.center = puck2.area.center

    if isClicked(340, 0, 90, 50):
        mainM2 = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pos = "over"
            socket_client.send(str.encode(str(pos)))
            pygame.quit()
            sys.exit()

    # Blits all the objects on to the display every frame
    disp.blit(background.image, puck2.rect, puck2.rect)
    disp.blit(playerText, (220, 175))
    disp.blit(player2Text, (550, 175))
    disp.blit(timeText, (340, 180))

    # Updates the sprites
    player.update()
    playertwo.update()

    player.draw(disp)
    playertwo.draw(disp)
    puckSprite2.draw(disp)
    pygame.display.flip()
    return mainM2

def MSGameOver(disp, playernumber):
    pygame.display.flip()
    for event in pygame.event.get():
        if isClicked(120, 290, 130, 70):
            # resetting all variables for another game
            mainM = False
            gameOver = False
            puck2.player2Score = 0
            timeKeeper.min = 0  # min
            timeKeeper.seconds = 60
            puck2.rect.center = puck2.area.center

        # Check to see if the user pressed the quit button
        elif isClicked(540, 290, 130, 70):
            pygame.quit()
            sys.exit()

        # Check to see if player1 wins or player2 wins or if it is a draw
        if (puck2.player2Score + puck3.player2Score + puck4.player2Score + puck5.player2Score + puck6.player2Score + puck7.player2Score) > (puck2.playerScore + puck3.playerScore + puck4.playerScore + puck5.playerScore + puck6.playerScore + puck7.playerScore):
            if playernumber == 1:
                msg = message.render('Lose', False, (0, 0, 0))
            else:
                msg = message.render('Win', False, (0, 0, 0))
        elif (puck2.player2Score + puck3.player2Score + puck4.player2Score + puck5.player2Score + puck6.player2Score + puck7.player2Score) == (puck2.playerScore + puck3.playerScore + puck4.playerScore + puck5.playerScore + puck6.playerScore + puck7.playerScore):
            msg = message.render('It is a draw!', False, (0, 0, 0))
        else:
            if playernumber == 1:
                msg = message.render('Win', False, (0, 0, 0))
            else:
                msg = message.render('Lose', False, (0, 0, 0))
        #將文字致中
        msgrect = msg.get_rect()
        msgrect.center = (400,200)
        disp.blit(mainMenu3.image, (0, 0))
        disp.blit(msg, msgrect)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def MMUpdateBluePlyer(socket_client, seconds):
    gameOver = False
    pos = player1.mouseMove1()  # Get blue player's position
    socket_client.send(str.encode(str(pos)))  # Client send red player's position to server
    pos2 = socket_client.recv(1024).decode('utf8')  # Client receives red player's position from server
    if pos2[0] == 'g':
        gameOver = True
    elif pos2[0] == 'o':
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("player leave", True, (255, 0, 0), True)
        win.blit(text, (700 / 2 - text.get_width() / 2, 300 / 2 - text.get_height() / 2))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
    elif pos2[0] == '(':
        pos3 = pos2.split(",")
        dx = pos3[0][1:]
        pos4 = pos3[1]
        pos5 = pos4.split(")")
        dy = pos5[0]
        player2.mouseMove2(int(dx), int(dy))
        dx1, dy1 = pos

        # Create thread for each puck
        t1 = threading.Thread(target=collision1_1, args=(puckSprite2, dx1, dy1, dx, dy))
        t2 = threading.Thread(target=collision1_2, args=(puckSprite3, dx1, dy1, dx, dy))
        t3 = threading.Thread(target=collision1_3, args=(puckSprite4, dx1, dy1, dx, dy))
        t4 = threading.Thread(target=collision1_4, args=(puckSprite5, dx1, dy1, dx, dy))
        t5 = threading.Thread(target=collision1_5, args=(puckSprite6, dx1, dy1, dx, dy))
        t6 = threading.Thread(target=collision1_6, args=(puckSprite7, dx1, dy1, dx, dy))

        # Thread execution
        t1.start()
        if seconds <= 50:
            t2.start()
        if seconds <= 40:
            t3.start()
        if seconds <= 30:
            t4.start()
        if seconds <= 20:
            t5.start()
        if seconds <= 10:
            t6.start()
    return gameOver

def MMUpdateRedPlyer(socket_client, seconds):
    gameOver = False
    pos = player2.mouseMove1()  # Get blue player's position
    socket_client.send(str.encode(str(pos)))  # Client send blue player's position to server
    pos2 = socket_client.recv(1024).decode('utf8')  # Client receives blue player's position from server
    if pos2[0] == 'g':
        gameOver = True
    elif pos2[0] == '0':
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("player leave", True, (255, 0, 0), True)
        win.blit(text, (700 / 2 - text.get_width() / 2, 300 / 2 - text.get_height() / 2))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
    elif pos2[0] == '(':
        pos3 = pos2.split(",")
        dx = pos3[0][1:]
        pos4 = pos3[1]
        pos5 = pos4.split(")")
        dy = pos5[0]
        player1.mouseMove2(int(dx), int(dy))
        dx1, dy1 = pos

        # Create thread for each puck
        t1 = threading.Thread(target=collision2_1, args=(puckSprite2, dx1, dy1, dx, dy))
        t2 = threading.Thread(target=collision2_2, args=(puckSprite3, dx1, dy1, dx, dy))
        t3 = threading.Thread(target=collision2_3, args=(puckSprite4, dx1, dy1, dx, dy))
        t4 = threading.Thread(target=collision2_4, args=(puckSprite5, dx1, dy1, dx, dy))
        t5 = threading.Thread(target=collision2_5, args=(puckSprite6, dx1, dy1, dx, dy))
        t6 = threading.Thread(target=collision2_6, args=(puckSprite7, dx1, dy1, dx, dy))

        # Thread execution
        t1.start()
        if seconds <= 50:
            t2.start()
        if seconds <= 40:
            t3.start()
        if seconds <= 30:
            t4.start()
        if seconds <= 20:
            t5.start()
        if seconds <= 10:
            t6.start()
    return gameOver

def MMGameNotOver(socket_client, disp, seconds, playerText, player2Text, timeText):
    mainM2 = False
    if puck2.goal:
        puck2.goal = False
        puck2.rect.center = puck2.area.center
    if puck3.goal:
        puck3.goal = False
        puck3.rect.center = puck3.area.center
    if puck4.goal:
        puck4.goal = False
        puck4.rect.center = puck4.area.center
    if puck5.goal:
        puck5.goal = False
        puck5.rect.center = puck5.area.center
    if puck6.goal:
        puck6.goal = False
        puck6.rect.center = puck6.area.center
    if puck7.goal:
        puck7.goal = False
        puck7.rect.center = puck7.area.center

    if isClicked(340, 0, 90, 50):
        mainM2 = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pos = "over"
            socket_client.send(str.encode(str(pos)))
            pygame.quit()
            sys.exit()

    # Blits all the objects on to the display every frame
    disp.blit(background.image, puck2.rect, puck2.rect)
    disp.blit(background.image, puck3.rect, puck3.rect)
    disp.blit(background.image, puck4.rect, puck4.rect)
    disp.blit(background.image, puck5.rect, puck5.rect)
    disp.blit(background.image, puck6.rect, puck6.rect)
    disp.blit(background.image, puck7.rect, puck7.rect)
    disp.blit(background.image, player1.rect, player1.rect)
    disp.blit(background.image, comp.rect, comp.rect)
    disp.blit(playerText, (220, 175))
    disp.blit(player2Text, (550, 175))
    disp.blit(timeText, (340, 180))

    # Updates the sprites
    player.update()
    playertwo.update()

    player.draw(disp)
    playertwo.draw(disp)
    puckSprite2.draw(disp)
    if seconds <= 50:
        puckSprite3.draw(disp)
    if seconds <= 40:
        puckSprite4.draw(disp)
    if seconds <= 30:
        puckSprite5.draw(disp)
    if seconds <= 20:
        puckSprite6.draw(disp)
    if seconds <= 10:
        puckSprite7.draw(disp)
    pygame.display.flip()
    return mainM2

def MMGameOver(disp, playernumber):
    gameOver = True
    # Returns you to the main menu if the game is over. i.e 1 minutes have passed
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif isClicked(120, 290, 130, 70):
            # resetting all variables for another game
            gameOver = False
            puck2.player2Score = 0
            puck2.playerScore = 0
            puck3.player2Score = 0
            puck3.playerScore = 0
            puck4.player2Score = 0
            puck4.playerScore = 0
            puck5.player2Score = 0
            puck5.playerScore = 0
            puck6.player2Score = 0
            puck6.playerScore = 0
            puck7.player2Score = 0
            puck7.playerScore = 0
            timeKeeper.min = 0  # min
            timeKeeper.seconds = 60
            puck2.rect.center = puck2.area.center
            puck3.rect.center = puck3.area.center
            puck4.rect.center = puck4.area.center
            puck5.rect.center = puck5.area.center
            puck6.rect.center = puck6.area.center
            puck7.rect.center = puck7.area.center

        # Check to see if the user pressed the quit button
        elif isClicked(540, 290, 130, 70):
            pygame.quit()

        # Check to see if player1 wins or player2 wins or if it is a draw
        if (puck2.player2Score + puck3.player2Score + puck4.player2Score + puck5.player2Score + puck6.player2Score + puck7.player2Score) > (puck2.playerScore + puck3.playerScore + puck4.playerScore + puck5.playerScore + puck6.playerScore + puck7.playerScore):
            if playernumber == 1:
                msg = message.render('Lose', False, (0, 0, 0))
            else:
                msg = message.render('Win', False, (0, 0, 0))
        elif (puck2.player2Score + puck3.player2Score + puck4.player2Score + puck5.player2Score + puck6.player2Score + puck7.player2Score) == (puck2.playerScore + puck3.playerScore + puck4.playerScore + puck5.playerScore + puck6.playerScore + puck7.playerScore):
            msg = message.render('It is a draw!', False, (0, 0, 0))
        else:
            if playernumber == 1:
                msg = message.render('Win', False, (0, 0, 0))
            else:
                msg = message.render('Lose', False, (0, 0, 0))
        msgrect = msg.get_rect()
        msgrect.center = (400, 200)
        disp.blit(mainMenu3.image, (0, 0))
        disp.blit(msg, msgrect)
    return gameOver