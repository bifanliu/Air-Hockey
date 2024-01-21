# Import packages
from single_player import *
from multi_player import *

# Main function define
def main(number, socket_client, playernumber):
    print("Enter main")
    print(playernumber)
    if number == -1:
        sys.exit()
    pygame.font.init()
    pygame.display.set_caption("Air Hockey")
    win = pygame.display.set_mode((800, 400))
    disp = win
    gameOver = False
    mainM2 = False

    # number = 0 means single player, number = 1 means multiple player
    while number == 0:
        # Check to if game is over i.e 1 minutes have passed
        if number == 0 and gameOver == False and mainM2 == False:
            # if timeout
            if timeKeeper.min == -1:
                gameOver = True
            mainM2 = STrace(disp=disp)
        elif gameOver:
            gameOver = SGameOver(disp=disp)

        # Check to see if user has pressed the main menu button
        elif mainM2:
            mainM2 = SmainM2(disp=disp)
    #multiple players single puck
    while number == 2:
        total2 = puck2.player2Score
        player2Text = player2Score.render(str(total2), False, (0, 0, 0))
        if gameOver == False and mainM2 == False:
            if timeKeeper.min == -1:
                msg = "gameover"
                socket_client.send(str.encode(str(msg)))
                pos2 = socket_client.recv(1024).decode('utf8')  # Client receives blue player's position from server
                gameOver = True
            else:
                total = puck2.playerScore
                # Updating the scores
                playerText = player2Score.render(str(total), False, (0, 0, 0))

                # Checking the most recent coordinates of the computer
                disp.blit(background.image, (0, 0))

                # Checking the updating the clock
                timeElapsed = clock.tick(60)
                timeKeeper.update(timeElapsed)
                timeText = timeKeeper.displayTime()
                # This flag is for the odd case where the computer gets stuck at a corner with the puck
                if playernumber == 1:  # Blue player
                    gameOver = MSUpdateBluePlyer(socket_client=socket_client)

                else:  # Red player
                    gameOver = MSUpdateRedPlyer(socket_client=socket_client)

                if gameOver == False:
                    mainM2 = MSGameNotOver(disp=disp, socket_client=socket_client,  playerText=playerText, 
                                            player2Text=player2Text, timeText=timeText)

        elif gameOver:
            # Returns you to the main menu if the game is over. i.e 1 minutes have passed
            MSGameOver(disp=disp, playernumber=playernumber)

        # Check to see if user has pressed the main menu button
        elif mainM2:
            disp.blit(mainMenu2.image, (0, 0))  # display menu
            pygame.display.flip()  # display menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pos = "over"
                    socket_client.send(str.encode(str(pos)))
                    pygame.quit()
                    sys.exit()
                elif isClicked(144, 273, 115, 65):
                    mainM2 = False
                    continue
                elif isClicked(545, 273, 115, 65):
                    pos = "over"
                    socket_client.send(str.encode(str(pos)))
                    pygame.quit()
                    sys.exit()

    #multiple players multiple pucks
    while number == 1:
        # total score
        total2 = puck2.player2Score + puck3.player2Score + puck4.player2Score + puck5.player2Score + puck6.player2Score  + puck7.player2Score
        # plyer2 score
        player2Text = player2Score.render(str(total2), False, (0, 0, 0))
        if gameOver == False and mainM2 == False:
            if timeKeeper.min == -1:
                msg = "gameover"
                socket_client.send(str.encode(str(msg)))
                pos2 = socket_client.recv(1024).decode('utf8')  # Client receives blue player's position from server
                gameOver = True
            else:
                # total score
                total = puck2.playerScore + puck3.playerScore + puck4.playerScore + puck5.playerScore + puck6.playerScore + puck7.playerScore

                # Updating the scores
                playerText = player2Score.render(str(total), False, (0, 0, 0))

                # Checking the most recent coordinates of the computer
                disp.blit(background.image, (0, 0))

                # Checking the updating the clock
                timeElapsed = clock.tick(60)  # Update clock
                timeKeeper.update(timeElapsed)
                timeText = timeKeeper.displayTime()

                # Record time
                seconds = timeKeeper.recordtime(timeElapsed)
                # print("seconds = {}".format(seconds))

                # This flag is for the odd case where the computer gets stuck at a corner with the puck
                if playernumber == 1:  # Blue player
                    gameOver = MMUpdateBluePlyer(socket_client=socket_client, seconds=seconds)
                    
                else:  # Red player
                    gameOver = MMUpdateRedPlyer(socket_client=socket_client, seconds=seconds)

                if gameOver == False:
                    mainM2 = MMGameNotOver(socket_client=socket_client, disp=disp, seconds=seconds, 
                                    playerText=playerText, player2Text=player2Text, timeText=timeText)

        elif gameOver:
            MMGameOver(disp=disp, playernumber=playernumber)

        # Check to see if user has pressed the main menu button
        elif mainM2:
            disp.blit(mainMenu2.image, (0, 0))  # display menu
            pygame.display.flip()  # display menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pos = "over"
                    socket_client.send(str.encode(str(pos)))
                    pygame.quit()
                    sys.exit()

                elif isClicked(144, 273, 115, 65):
                    mainM2 = False
                    continue
                elif isClicked(545, 273, 115, 65):
                    pos = "over"
                    socket_client.send(str.encode(str(pos)))
                    pygame.quit()
                    sys.exit()

    pygame.display.update()

