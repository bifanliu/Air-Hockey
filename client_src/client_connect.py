# Import packages
from client_main import *
import socket


# thread job
waiting = True
playernumber = 0
port = 16902

def monitor():
    global waiting, playernumber
    i = 0
    while waiting == True:
        player2pos = socket_client.recv(1024).decode(encoding='utf8')
        socket_client.send(player2pos.encode('utf8'))

        # 這裡第一個連線到 server 的 client 會收到 player2pos == "wait the other player"
        # 然後再收到 player2pos == "start"
        # 第二個連線到 server 的 client 只會收到 player2pos == "start"

        # player2pos == "start"
        if player2pos[5] == '1':
            print("game start")
            waiting = False
            # Red player is player2
            playernumber = 2
        elif player2pos[5] == '2':
            print("game start")
            waiting = False
            # Blue player is player1
            playernumber = 1

# connect to server
while True:
    pygame.font.init()

    # 設定視窗
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Air Hockey")

    # 建立畫布 bg
    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0, 0, 0))

    # (4.1) Main background and font setting
    # 繪製矩形圖形 : pygame.draw.rect(畫布, 顏色, [x坐標, y坐標, 寬度, 高度], 線寬)
    pygame.draw.rect(bg, (255, 255, 255), (0, 0, 800, 5), 0)
    pygame.draw.rect(bg, (255, 255, 255), (0, 0, 5, 400), 0)
    pygame.draw.rect(bg, (255, 255, 255), (0, 395, 800, 400), 0)
    pygame.draw.rect(bg, (255, 255, 255), (795, 0, 800, 400), 0)
    pygame.draw.circle(bg, (255, 255, 255), (0, 200), 200, 4)
    pygame.draw.circle(bg, (255, 255, 255), (800, 200), 200, 4)
    pygame.draw.rect(bg, (255, 255, 255), (398, 0, 4, 400), 0)
    pygame.draw.rect(bg, (255, 255, 255), [0, 160, 40, 80], 4)
    pygame.draw.rect(bg, (255, 255, 255), [760, 160, 40, 80], 4)
    # 設定字體
    font = pygame.font.SysFont("simhei", 100)
    text = font.render("Air Hockey", True, (255, 48, 48), (0, 0, 0))
    bg.blit(text, (230, 50))

    # (4.2) Single background and font setting
    pygame.draw.rect(bg, (0, 0, 255), (125, 275, 125, 58), 0)
    font = pygame.font.SysFont("simhei", 40)
    text = font.render("Single", True, (255, 215, 0), (0, 0, 255))
    bg.blit(text, (145, 290))

    # (4.3) Multiple background and font setting
    pygame.draw.rect(bg, (0, 0, 255), (350, 275, 125, 58), 0)
    text2 = font.render("Multiple", True, (255, 215, 0), (0, 0, 255))
    bg.blit(text2, (360, 290))

    # (4.4) Over background and font setting
    pygame.draw.rect(bg, (0, 0, 255), (575, 275, 125, 58), 0)
    text = font.render("Finish", True, (255, 215, 0), (0, 0, 255))
    bg.blit(text, (595, 290))

    # (4.5) 最終顯示
    screen.blit(bg, (0, 0))
    pygame.display.update()
    screen.blit(bg, (0, 0))
    pygame.display.update()
    while True:
        # 從 Pygame 的事件佇列中取出事件，並從佇列中刪除該事件
        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Single player
            elif isClicked(125, 275, 100, 50):
                number = 0  # number = 0 means single player
                main(number,0,0)

            # Multiple player
            elif isClicked(350, 275, 100, 50):
                # 設定視窗
                screen = pygame.display.set_mode((800, 400))
                pygame.display.set_caption("Air Hockey")

                # 建立畫布 bg
                bg = pygame.Surface(screen.get_size())
                bg = bg.convert()
                bg.fill((0, 0, 0))
                    # (4.1) Main background and font setting
                # 繪製矩形圖形 : pygame.draw.rect(畫布, 顏色, [x坐標, y坐標, 寬度, 高度], 線寬)
                pygame.draw.rect(bg, (255, 255, 255), (0, 0, 800, 5), 0)
                pygame.draw.rect(bg, (255, 255, 255), (0, 0, 5, 400), 0)
                pygame.draw.rect(bg, (255, 255, 255), (0, 395, 800, 400), 0)
                pygame.draw.rect(bg, (255, 255, 255), (795, 0, 800, 400), 0)
                pygame.draw.circle(bg, (255, 255, 255), (0, 200), 200, 4)
                pygame.draw.circle(bg, (255, 255, 255), (800, 200), 200, 4)
                pygame.draw.rect(bg, (255, 255, 255), (398, 0, 4, 400), 0)
                pygame.draw.rect(bg, (255, 255, 255), [0, 160, 40, 80], 4)
                pygame.draw.rect(bg, (255, 255, 255), [760, 160, 40, 80], 4)
                    # 設定字體
                font = pygame.font.SysFont("simhei", 100)
                text = font.render("Air Hockey", True, (255, 48, 48), (0, 0, 0))
                textcent = text.get_rect()
                textcent.center = (400,100)
                bg.blit(text, textcent)
                    # (4.2) Single Puck
                # pygame.draw.rect(bg, (0, 0, 255), (125, 300, 125, 0), 0)
                font = pygame.font.SysFont("simhei", 40)
                text = font.render("Single Puck", True, (255, 215, 0), (0, 0, 255))
                textcent = text.get_rect()
                textcent.center = (200,300)
                bg.blit(text, textcent)

                # (4.3) Multiple Pucks
                # pygame.draw.rect(bg, (0, 0, 255), (575, 275, 125, 58), 0)
                text2 = font.render("Multi Pucks", True, (255, 215, 0), (0, 0, 255))
                text2cent = text2.get_rect()
                text2cent.center = (600,300)
                bg.blit(text2, text2cent)
                
                #最終顯示
                screen.blit(bg, (0, 0))
                pygame.display.update()

                # which mode is player chose
                chose = True
                number = 0
                while chose:
                    for event in pygame.event.get():
                            # Quit the game
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif isClicked(90, 280, 220,40):
                            chose = False
                            number = 2  # number = 2 means multiple players single pucks
                        elif isClicked(490,280,220,40):
                            chose = False
                            number = 1 #number = 1 means multiple players multiple pucks
                    pygame.display.update()

                # Set socket
                socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server = "172.20.247.10"
                socket_client.connect((server, port))
                socket_client.send(str(number).encode('utf8'))

                # update screen
                win.fill((128, 128, 128))
                font = pygame.font.SysFont("comicsans", 80)
                text = font.render("Waiting for Player...", True, (255, 0, 0), True)
                win.blit(text, (800 / 2 - text.get_width() / 2, 400 / 2 - text.get_height() / 2))
                pygame.display.update()
                # wait game start
                t = threading.Thread(target = monitor)
                t.start()
                
                while waiting == True:
                    for event in pygame.event.get():
                            # Quit the game
                        if event.type == pygame.QUIT:
                            pos = "over"
                            socket_client.send(str.encode(str(pos)))
                            waiting = False
                            number = -1
                            pygame.quit()
                    if number != -1:
                        pygame.display.update()
                t.join()
                main(number=number, socket_client=socket_client, playernumber=playernumber)
            elif isClicked(575, 275, 100, 50):
                sys.exit()
                pygame.quit()

